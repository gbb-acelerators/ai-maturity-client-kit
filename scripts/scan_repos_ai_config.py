#!/usr/bin/env python3
"""Scan repositories for committed AI configuration (D4 cross-check).

Implements the repository cross-check recommended in section 8 of the v2
spec: find the AI configuration committed to each repository and place
the repository on the four RAMP levels (Repository AI Maturity Profile)
of Denisov-Blanch et al. [47]:

    L1 Unconfigured   no AI configuration artifacts
    L2 Grounded       rules, instructions, tool or MCP configuration
    L3 Agent          custom agents, prompt files or commands, skills
    L4 Orchestration  multi-agent flows, agent session logs

A repository gets the highest level at which it has at least one
artifact. This is a pattern-based approximation: RAMP also classifies
files by their content, while this scan only matches the documented
file conventions of common AI coding tools. It can miss non-standard
files and says nothing about their quality.

For local clones it also counts how many instruction files were
committed once and never changed; D4-Q4 at L3 expects files that are
"updated when the codebase changes rather than committed once".

Sources:
    --path DIR        a repository, or a folder whose subfolders are
                      repositories (repeatable)
    --github-org ORG  every repository of a GitHub organization, read
                      through the REST API with GITHUB_TOKEN or GH_TOKEN
                      (default branch only)

Writes output/repo-scan.json. The v2 reports compare it with the D4-Q4
and D4-Q5 answers when the file is present.

Usage:
    python3 scripts/scan_repos_ai_config.py --path ~/src [--out output]
    python3 scripts/scan_repos_ai_config.py --github-org contoso
"""
from __future__ import annotations

import argparse
import datetime
import fnmatch
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (glob on the repository-relative POSIX path, category, RAMP level)
PATTERNS: list[tuple[str, str, int]] = [
    # L2 Grounded: rules and instructions
    (".github/copilot-instructions.md", "rules", 2),
    (".github/instructions/*.instructions.md", "rules", 2),
    (".github/instructions/**/*.instructions.md", "rules", 2),
    ("AGENTS.md", "rules", 2),
    ("**/AGENTS.md", "rules", 2),
    ("CLAUDE.md", "rules", 2),
    ("**/CLAUDE.md", "rules", 2),
    ("GEMINI.md", "rules", 2),
    (".cursorrules", "rules", 2),
    (".cursor/rules/*", "rules", 2),
    (".cursor/rules/**/*", "rules", 2),
    (".windsurfrules", "rules", 2),
    (".windsurf/rules/*", "rules", 2),
    (".clinerules", "rules", 2),
    (".clinerules/*", "rules", 2),
    (".roo/rules/*", "rules", 2),
    (".junie/guidelines.md", "rules", 2),
    (".aiassistant/rules/*", "rules", 2),
    (".idx/airules.md", "rules", 2),
    (".kiro/steering/*", "rules", 2),
    (".openhands/microagents/repo.md", "rules", 2),
    # L2 Grounded: tool and MCP configuration
    (".vscode/mcp.json", "config", 2),
    (".mcp.json", "config", 2),
    ("mcp.json", "config", 2),
    (".cursor/mcp.json", "config", 2),
    (".claude/settings.json", "config", 2),
    (".gemini/settings.json", "config", 2),
    (".aider.conf.yml", "config", 2),
    (".github/workflows/copilot-setup-steps.yml", "config", 2),
    (".github/workflows/copilot-setup-steps.yaml", "config", 2),
    # L3 Agent: custom agents, prompt files and commands, skills
    (".github/agents/*.md", "agents", 3),
    (".github/chatmodes/*.chatmode.md", "agents", 3),
    (".claude/agents/*.md", "agents", 3),
    (".claude/agents/**/*.md", "agents", 3),
    (".github/prompts/*.prompt.md", "commands", 3),
    (".claude/commands/*.md", "commands", 3),
    (".claude/commands/**/*.md", "commands", 3),
    (".cursor/commands/*", "commands", 3),
    (".gemini/commands/*.toml", "commands", 3),
    (".windsurf/workflows/*.md", "commands", 3),
    ("**/SKILL.md", "skills", 3),
    ("SKILL.md", "skills", 3),
    (".openhands/microagents/*.md", "skills", 3),
    # L4 Orchestration: multi-agent flows and agent session logs
    (".claude-flow/*", "flows", 4),
    (".claude-flow/**/*", "flows", 4),
    ("claude-flow.config.json", "flows", 4),
    (".swarm/*", "flows", 4),
    (".hive-mind/*", "flows", 4),
    (".specstory/history/*", "session-logs", 4),
    (".aider.chat.history.md", "session-logs", 4),
]
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build",
             "__pycache__"}
LEVEL_NAMES = {1: "Unconfigured", 2: "Grounded", 3: "Agent",
               4: "Orchestration"}


def classify(path: str) -> tuple[str, int] | None:
    """Category and RAMP level of one file, or None."""
    best = None
    for pattern, category, level in PATTERNS:
        if fnmatch.fnmatchcase(path, pattern):
            if best is None or level > best[1]:
                best = (category, level)
    return best


def git_files(repo: Path) -> list[str] | None:
    try:
        out = subprocess.run(["git", "-C", str(repo), "ls-files"],
                             capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return [line for line in out.stdout.splitlines() if line]


def walk_files(repo: Path) -> list[str]:
    files = []
    for base, dirs, names in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in names:
            rel = Path(base, name).relative_to(repo)
            files.append(rel.as_posix())
    return files


def commit_count(repo: Path, path: str) -> int | None:
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "log", "--follow", "--format=%H",
             "--", path], capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return len([line for line in out.stdout.splitlines() if line])


def scan_file_list(name: str, files: list[str],
                   repo: Path | None = None) -> dict:
    artifacts = []
    for path in sorted(files):
        hit = classify(path)
        if not hit:
            continue
        entry = {"path": path, "category": hit[0], "level": hit[1]}
        if repo is not None and hit[0] == "rules":
            entry["commits"] = commit_count(repo, path)
        artifacts.append(entry)
    level = max((a["level"] for a in artifacts), default=1)
    has_l2 = any(a["level"] == 2 for a in artifacts)
    return {
        "name": name,
        "level": f"L{level}",
        "level_name": LEVEL_NAMES[level],
        "coherence_warning": level > 2 and not has_l2,
        "artifacts": artifacts,
    }


def local_repositories(paths: list[str]) -> list[Path]:
    repos = []
    for raw in paths:
        base = Path(raw).expanduser().resolve()
        if (base / ".git").exists():
            repos.append(base)
            continue
        if base.is_dir():
            repos += sorted(p for p in base.iterdir()
                            if p.is_dir() and (p / ".git").exists())
    return repos


def scan_local(paths: list[str]) -> list[dict]:
    out = []
    for repo in local_repositories(paths):
        files = git_files(repo)
        use_git = files is not None
        out.append(scan_file_list(repo.name, files if use_git
                                  else walk_files(repo),
                                  repo if use_git else None))
    return out


def _api(url: str, token: str) -> object:
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "ai-maturity-client-kit"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def scan_github(org: str, token: str, max_repos: int,
                include_archived: bool) -> list[dict]:
    base = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    repos, page = [], 1
    while len(repos) < max_repos:
        batch = _api(f"{base}/orgs/{org}/repos?per_page=100&page={page}"
                     f"&type=all", token)
        if not batch:
            break
        repos += [r for r in batch
                  if include_archived or not r.get("archived")]
        page += 1
    out = []
    for repo in repos[:max_repos]:
        branch = repo.get("default_branch") or "main"
        try:
            tree = _api(f"{base}/repos/{org}/{repo['name']}/git/trees/"
                        f"{branch}?recursive=1", token)
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 409):  # empty repository
                out.append(scan_file_list(repo["name"], []))
                continue
            raise
        files = [t["path"] for t in tree.get("tree", [])
                 if t.get("type") == "blob"]
        entry = scan_file_list(repo["name"], files)
        entry["truncated"] = bool(tree.get("truncated"))
        out.append(entry)
    return out


def summarize(repos: list[dict]) -> dict:
    n = len(repos)
    levels = {f"L{i}": 0 for i in range(1, 5)}
    for r in repos:
        levels[r["level"]] += 1
    rules = [a for r in repos for a in r["artifacts"]
             if a["category"] == "rules" and a.get("commits") is not None]
    once = sum(1 for a in rules if a["commits"] <= 1)

    def share(k: int) -> float | None:
        return round(k / n, 3) if n else None

    return {
        "repositories": n,
        "levels": levels,
        "share_l2_or_higher": share(n - levels["L1"]),
        "share_l3_or_higher": share(levels["L3"] + levels["L4"]),
        "instruction_files_checked": len(rules),
        "instruction_files_committed_once": once,
        "share_committed_once": round(once / len(rules), 3)
        if rules else None,
        "coherence_warnings": sum(1 for r in repos
                                  if r["coherence_warning"]),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--path", action="append", default=[],
                    help="repository or folder of repositories")
    ap.add_argument("--github-org", help="GitHub organization to scan")
    ap.add_argument("--max-repos", type=int, default=500)
    ap.add_argument("--include-archived", action="store_true")
    ap.add_argument("--out", default=str(ROOT / "output"))
    ap.add_argument("--label", help="note stored in the metadata, for "
                    "example 'illustrative fixture repositories'")
    args = ap.parse_args()
    if not args.path and not args.github_org:
        ap.error("give --path or --github-org")
    repos = scan_local(args.path) if args.path else []
    source = "local"
    if args.github_org:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if not token:
            print("✗ Set GITHUB_TOKEN or GH_TOKEN to scan an organization.",
                  file=sys.stderr)
            return 1
        repos += scan_github(args.github_org, token, args.max_repos,
                             args.include_archived)
        source = "github" if not args.path else "local+github"
    if not repos:
        print("✗ No repositories found.", file=sys.stderr)
        return 1
    result = {
        "metadata": {
            "generated_at": datetime.datetime.now(
                datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source": source,
            "organization": args.github_org,
            "method": "Pattern-based approximation of the RAMP levels "
                      "[47]; file content is not classified.",
            "script": "scripts/scan_repos_ai_config.py",
            "label": args.label,
        },
        "summary": summarize(repos),
        "repositories": repos,
    }
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "repo-scan.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    s = result["summary"]
    print(f"✓ {out / 'repo-scan.json'}: {s['repositories']} repositories, "
          f"levels {s['levels']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
