"""Deterministic AI maturity rubric for the Developer Survey v2.0.

Maps individual answers to levels L0-L4 across 7 dimensions. The team
result is the average score plus the distribution (% of devs per level).

Principles:
- Deterministic: the same answer always yields the same level
- Auditable: every rule is documented
- Conservative: when in doubt, score lower (avoids inflating maturity)
- Anonymous: scored per respondent, but only aggregates reach the report

Each `score_DX(responses)` returns a float in [0.0, 4.0], or None when
coverage is insufficient.

Match strings are the canonical Portuguese options. Answers exported from
the English or Spanish Forms, or from older Portuguese Forms whose options
used dashes, are first mapped back to the canonical option with
survey-devs/options.json (canonical_responses), so every language scores
the same way.
"""
import json
import re
import unicodedata
from pathlib import Path
from typing import Optional

SUPPORTED_LANGS = ("en", "pt-br", "es")
OPTIONS_PATH = Path(__file__).resolve().parents[1] / "options.json"

LEVEL_LABELS = {
    "en": [
        "L0 Initial",
        "L1 Developing",
        "L2 Defined",
        "L3 Managed",
        "L4 Optimizing",
    ],
    "pt-br": [
        "L0 Inicial",
        "L1 Em Desenvolvimento",
        "L2 Definido",
        "L3 Gerenciado",
        "L4 Otimizando",
    ],
    "es": [
        "L0 Inicial",
        "L1 En desarrollo",
        "L2 Definido",
        "L3 Gestionado",
        "L4 Optimizando",
    ],
}

NO_DATA_LABEL = {"en": "No data", "pt-br": "Sem dados",
                 "es": "Sin datos"}
OVERALL_NAME = {"en": "Overall Maturity", "pt-br": "Maturidade Overall",
                "es": "Madurez general"}


def _lang(lang: str) -> str:
    return lang if lang in SUPPORTED_LANGS else "en"


def fold(text: Optional[str]) -> str:
    """Lowercase, drop accents and separator punctuation for matching.

    "Sim, trato como par" and "Sim, trato como par" fold to the same
    text, so option wording can change without breaking older exports.
    """
    value = unicodedata.normalize("NFKD", str(text or "").lower())
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[\u2014\u2013:,;.!?()\[\]\"'/-]+", " ", value)
    return " ".join(value.split())


def _load_options() -> dict:
    if not OPTIONS_PATH.exists():
        return {}
    return json.loads(OPTIONS_PATH.read_text(encoding="utf-8"))


OPTIONS = _load_options()
_CANONICAL = {
    qid: {fold(opt[lang]): opt["pt"] for opt in opts
          for lang in ("pt", "en", "es") if opt.get(lang)}
    for qid, opts in OPTIONS.items()
}


def canonical_value(qid: str, value) -> Optional[str]:
    """Map one exported answer (any language) to the canonical option."""
    if value is None:
        return None
    table = _CANONICAL.get(qid)
    text = str(value).strip()
    if not table or not text:
        return text
    if ";" in text:
        parts = [p.strip() for p in text.split(";") if p.strip()]
        sep = "; " if "; " in text else ";"
        return sep.join(table.get(fold(p), p) for p in parts)
    return table.get(fold(text), text)


def canonical_responses(responses: dict) -> dict:
    """Copy of a respondent's responses with canonical option values."""
    out = {}
    for qid, entry in (responses or {}).items():
        if isinstance(entry, dict) and "value" in entry:
            out[qid] = {**entry,
                        "value": canonical_value(qid, entry["value"])}
        else:
            out[qid] = entry
    return out


def display_option(qid: str, value: str, lang: str = "en") -> str:
    """The canonical option in the report language (falls back to it)."""
    key = {"pt-br": "pt", "en": "en", "es": "es"}.get(_lang(lang), "en")
    target = fold(value)
    for opt in OPTIONS.get(qid, []):
        if fold(opt["pt"]) == target:
            return opt.get(key) or opt["pt"]
    return value


# =========================================================
# Helpers
# =========================================================

def _ans(responses: dict, qid: str) -> Optional[str]:
    """Returns answer string for qid, or None if not answered."""
    r = responses.get(qid)
    if r is None or r.get("value") is None:
        return None
    val = str(r["value"]).strip()
    return val if val else None


def _multi(responses: dict, qid: str) -> list[str]:
    """Returns list of selected options for multi-choice answers."""
    val = _ans(responses, qid)
    if not val:
        return []
    return [opt.strip() for opt in val.split(";") if opt.strip()]


def _matches(answer: Optional[str], *patterns: str) -> bool:
    """Folded substring match: answer contains ANY pattern."""
    if not answer:
        return False
    a = fold(answer)
    return any(fold(p) in a for p in patterns)


def _multi_count(items: list[str], *patterns: str) -> int:
    """Count how many items match any of the patterns."""
    return sum(1 for item in items if _matches(item, *patterns))


# =========================================================
# DS-D2: Copilot Adoption Maturity
# =========================================================
# Signals: license + frequency + mode breadth + features + perceived gain

def score_D2(responses: dict) -> Optional[float]:
    """Copilot Adoption Maturity (L0-L4)."""
    license_ans = _ans(responses, "S2-Q1")
    if license_ans is None:
        return None

    # Hard L0: no license, or has one but does not use it
    if (_matches(license_ans, "Não tenho licença")
            or _matches(license_ans, "Tenho licença mas não uso")):
        return 0.0

    freq = _ans(responses, "S2-Q2")
    if _matches(freq, "Nunca"):
        return 0.0
    if _matches(freq, "Raramente"):
        return 1.0

    modes = _multi(responses, "S2-Q3")
    n_modes = sum(
        1 for m in modes if not _matches(m, "Não conheço", "Não uso")
    )
    uses_agent = any(
        _matches(m, "Agent (autônomo no IDE", "Coding Agent")
        for m in modes
    )
    uses_coding_agent = any(
        _matches(m, "Coding Agent (autônomo no GitHub") for m in modes
    )

    features = _multi(responses, "S2-Q5")
    n_features = len(features)
    uses_spaces = any(_matches(f, "Spaces") for f in features)
    uses_pr_review = any(_matches(f, "PR review") for f in features)

    gain = _ans(responses, "S2-Q7")
    high_gain = _matches(gain, "+40", "+60") if gain else False
    low_gain = _matches(gain, "Negativo", "Neutro") if gain else False

    # L4: Coding Agent + Spaces + high measured gain + 5+ features
    if (uses_coding_agent and uses_spaces and high_gain
            and n_features >= 5):
        return 4.0

    # L3: Agent or Coding Agent + breadth (3+ modes or 4+ features)
    # + positive gain
    if ((uses_agent or uses_coding_agent)
            and (n_modes >= 3 or n_features >= 4) and not low_gain):
        return 3.0

    # L2: daily use + Ask/Edit + 2+ features
    if _matches(freq, "Diariamente") and n_modes >= 1 and n_features >= 2:
        return 2.0

    # L1: licensed, weekly+ use, no breadth
    return 1.0


# =========================================================
# DS-D3: MS/GH Tooling Breadth
# =========================================================
# Counts advanced tools in USE (Foundry, Spaces, Coding Agent, MCP, etc.)

ADVANCED_MS_GH_TOOLS = [
    "Microsoft Foundry",
    "Foundry Agent Service",
    "Azure OpenAI",
    "Microsoft 365 Copilot",
    "GitHub Copilot Spaces",
    "GitHub Copilot Coding Agent",
    "GitHub Codespaces",
    "GitHub Models",
    "GitHub Advanced Security",
    "GitHub Actions com Copilot",
    "Visual Studio com Copilot",
]


def score_D3(responses: dict) -> Optional[float]:
    """MS/GitHub Tooling Breadth (L0-L4)."""
    tools = _multi(responses, "S3-Q1")
    if not tools:
        return None
    if any(_matches(t, "Nenhuma das acima") for t in tools):
        return 0.0

    # Count MS/GH tools used (excluding "none")
    n_tools = sum(1 for t in tools if not _matches(t, "Nenhuma"))

    # Bonus signals: uses specific advanced features
    coding_agent_use = _ans(responses, "S3-Q3")
    spaces_use = _ans(responses, "S3-Q4")
    mcp_use = _ans(responses, "S3-Q6")
    foundry_use = _multi(responses, "S3-Q2")

    advanced_count = 0
    if _matches(coding_agent_use, "Uso ativamente"):
        advanced_count += 1
    if _matches(spaces_use, "Uso e crio Spaces"):
        advanced_count += 1
    if _matches(mcp_use, "Uso servidores MCP", "Configurei algum MCP"):
        advanced_count += 1
    if any(
        _matches(f, "MCP", "Multi-agent", "agentes autônomos")
        for f in foundry_use
    ):
        advanced_count += 1

    # Mapping: tool count + advanced signals -> level
    score = n_tools + advanced_count

    if score >= 8: return 4.0  # 5+ tools + 3+ advanced signals
    if score >= 5: return 3.0  # ~4 tools + some advanced
    if score >= 3: return 2.0  # ~3 tools, basic adoption
    if score >= 1: return 1.0  # 1-2 tools
    return 0.0


# =========================================================
# DS-D4: AI Dev Practices Maturity
# =========================================================
# TDD with AI + SDD + pair programming + AI across all dev phases

def score_D4(responses: dict) -> Optional[float]:
    """AI Dev Practices Maturity (L0-L4)."""
    tdd = _ans(responses, "S4-Q1")
    sdd = _ans(responses, "S4-Q2")
    moments = _multi(responses, "S4-Q3")
    pair = _ans(responses, "S4-Q4")
    refactor = _ans(responses, "S4-Q5")
    debug = _ans(responses, "S4-Q7")
    onboarding = _ans(responses, "S4-Q8")

    if all(x is None for x in [tdd, sdd, pair, refactor]):
        return None

    score = 0

    # TDD with AI
    if _matches(tdd, "Sempre que possível"): score += 2
    elif _matches(tdd, "Frequentemente"): score += 1.5
    elif _matches(tdd, "Às vezes"): score += 1
    elif _matches(tdd, "Não sei o que é TDD"): score -= 1

    # SDD
    if _matches(sdd, "Uso ativamente"): score += 2
    elif _matches(sdd, "Já testei"): score += 1
    elif _matches(sdd, "Nunca ouvi falar"): score -= 0.5

    # Breadth of moments (max 7)
    n_moments = len(moments)
    score += min(n_moments * 0.4, 2.0)  # cap 2.0

    # Pair programmer mindset
    if _matches(pair, "Sim, trato como par"): score += 1.5
    elif _matches(pair, "Às vezes"): score += 0.5

    # Refactoring
    if _matches(refactor, "Toda semana"): score += 1
    elif _matches(refactor, "Algumas vezes"): score += 0.5

    # Debugging with AI first
    if _matches(debug, "Pergunto ao Copilot"): score += 0.5

    # Onboarding with AI
    if _matches(onboarding, "Sempre"): score += 1
    elif _matches(onboarding, "Frequentemente"): score += 0.5

    # Cap and map (range 0-10 -> 0-4)
    score = max(0, min(score, 10))
    return round(score / 10 * 4, 2)


# =========================================================
# DS-D5: Agent Concepts Mastery
# =========================================================
# Knowledge of key concepts + created primitives + tests agents

def score_D5(responses: dict) -> Optional[float]:
    """Agent Concepts Mastery (L0-L4)."""
    # Key concepts (S5 Q1-Q8 + Q9 personas)
    concept_questions = [
        ("S5-Q1", ["Sim, explico claramente"]),         # AI agent
        ("S5-Q2", ["Sim, uso conscientemente"]),        # Modes
        ("S5-Q3", ["Já criei", "Já usei"]),              # Custom agents
        ("S5-Q4", ["Conheço e uso", "Conheço mas não uso"]),  # Skills
        ("S5-Q5", ["Sim, várias", "Sim, uma ou duas"]),  # Prompt files
        ("S5-Q6", ["Uso", "Conheço o conceito"]),        # A2A
        ("S5-Q7", ["Uso", "Conheço o conceito"]),        # Handoffs
        ("S5-Q8", ["Uso", "Conheço o conceito"]),        # Subagents
        ("S5-Q9", ["Sim, adoto", "Conheço o conceito"]),  # Personas
    ]

    answered = 0
    knowledge_score = 0
    for qid, deep_keywords in concept_questions:
        ans = _ans(responses, qid)
        if ans is None:
            continue
        answered += 1
        # Strong knowledge (use/explain) = 1.0
        if any(_matches(ans, k) for k in deep_keywords):
            knowledge_score += 1.0

    if answered < 5:
        return None  # insufficient coverage

    # Coverage ratio (0-1)
    coverage = knowledge_score / len(concept_questions)

    # Bonus: created primitives (S5-Q11 multi)
    primitives = _multi(responses, "S5-Q11")
    n_primitives = sum(
        1 for p in primitives if not _matches(p, "Nenhum dos acima")
    )

    # Bonus: tests agents (S5-Q10)
    tests = _ans(responses, "S5-Q10")
    test_bonus = 0
    if _matches(tests, "Sempre, tenho test suite"): test_bonus = 1.0
    elif _matches(tests, "Frequentemente"): test_bonus = 0.5
    elif _matches(tests, "Não crio agents"): test_bonus = 0  # neutral

    # Combined: 60% coverage + 25% primitives + 15% testing
    raw = (
        (coverage * 0.6 * 4)
        + min(n_primitives * 0.25, 1.0)
        + (test_bonus * 0.15 * 4 / 1.0 * 0.6)
    )

    return round(min(raw, 4.0), 2)


# =========================================================
# DS-D6: Instructions Files Maturity
# =========================================================

def score_D6(responses: dict) -> Optional[float]:
    """Instructions / Memory Maturity (L0-L4)."""
    files = _multi(responses, "S6-Q1")
    maintainer = _ans(responses, "S6-Q2")
    freq = _ans(responses, "S6-Q3")
    content = _multi(responses, "S6-Q4")
    library = _ans(responses, "S6-Q5")

    if not files and maintainer is None:
        return None

    # Hard L0: no instruction files
    if any(_matches(f, "Nenhum") for f in files) or len(files) == 0:
        return 0.0

    score = 0

    # Files breadth
    n_files = sum(1 for f in files if not _matches(f, "Nenhum"))
    if n_files >= 4: score += 2
    elif n_files >= 2: score += 1.5
    elif n_files >= 1: score += 1

    # Maintainer
    if _matches(maintainer, "Time inteiro contribui"): score += 2
    elif _matches(maintainer, "1-2 pessoas dedicadas"): score += 1.5
    elif _matches(maintainer, "Eu mantenho sozinho"): score += 1
    elif _matches(maintainer, "Ninguém mantém"): score -= 1
    elif _matches(maintainer, "Não temos"): score -= 1

    # Update frequency
    if _matches(freq, "Toda semana"): score += 1
    elif _matches(freq, "Mensalmente"): score += 0.7
    elif _matches(freq, "Trimestralmente"): score += 0.4
    elif _matches(freq, "Nunca atualizo"): score -= 0.5

    # Content richness (max ~7 types)
    n_content = sum(1 for c in content if not _matches(c, "Não tenho"))
    score += min(n_content * 0.3, 2.0)

    # Shared prompt library
    if _matches(library, "Copilot Space compartilhado", "repo dedicado"):
        score += 1
    elif _matches(library, "wiki/Confluence"): score += 0.5
    elif _matches(library, "Não compartilhamos"): score -= 0.5

    # Map to 0-4 (raw range ~0-9)
    score = max(0, min(score, 9))
    return round(score / 9 * 4, 2)


# =========================================================
# DS-D7: Best Practices
# =========================================================

def score_D7(responses: dict) -> Optional[float]:
    """Usability and Best Practices (L0-L4)."""
    learning = _multi(responses, "S7-Q1")
    champion = _ans(responses, "S7-Q2")
    channel = _ans(responses, "S7-Q3")
    metrics = _multi(responses, "S7-Q4")
    iterations = _ans(responses, "S7-Q5")
    sharing = _ans(responses, "S7-Q9")

    if not learning and champion is None:
        return None

    score = 0

    # Learning sources breadth
    n_sources = len(learning)
    score += min(n_sources * 0.3, 1.5)

    # Champion
    if _matches(champion, "Sim, eu sou", "Sim, outra pessoa"):
        score += 1.5
    elif _matches(champion, "Não, mas precisava"): score += 0
    elif _matches(champion, "Não, cada um se vira"): score -= 0.5

    # Internal channel
    if _matches(channel, "ativo (>5"): score += 1
    elif _matches(channel, "pouco ativo"): score += 0.5

    # Metrics measurement
    rich_metrics = sum(1 for m in metrics if any(
        _matches(m, k) for k in ["DORA", "DX", "SPACE", "Copilot"]
    ))
    score += min(rich_metrics * 0.5, 2.0)
    if any(_matches(m, "Não medimos") for m in metrics): score -= 1

    # Iteration efficiency (proxy for skill)
    if _matches(iterations, "Acerta na 1ª", "2-3 iterações"): score += 1
    elif _matches(iterations, "7+"): score -= 0.5

    # Sharing prompts
    if _matches(sharing, "Frequentemente"): score += 1
    elif _matches(sharing, "Às vezes"): score += 0.5
    elif _matches(sharing, "Nunca"): score -= 0.5

    # Map to 0-4 (raw range ~-2 to 8)
    score = max(0, min(score, 8))
    return round(score / 8 * 4, 2)


# =========================================================
# DS-D8: Security & Governance Maturity
# =========================================================
# Critical: red flags weigh negatively

def score_D8(responses: dict) -> Optional[float]:
    """Security & Governance Maturity (L0-L4), conservative scoring."""
    policy = _ans(responses, "S8-Q1")
    knows_data = _ans(responses, "S8-Q2")
    forbidden = _multi(responses, "S8-Q3")
    sec_tools = _multi(responses, "S8-Q4")
    scan_in_pr = _ans(responses, "S8-Q5")
    sbom = _ans(responses, "S8-Q6")
    review = _ans(responses, "S8-Q7")
    red_lines = _ans(responses, "S8-Q8")
    jit = _ans(responses, "S8-Q9")
    dlp = _ans(responses, "S8-Q10")
    audit = _ans(responses, "S8-Q11")
    training = _ans(responses, "S8-Q12")

    if policy is None and not sec_tools:
        return None

    # Hard L0: no policy + no tools
    no_policy = (_matches(policy, "Não temos política")
                 or _matches(policy, "Não sei"))
    no_tools = (any(_matches(t, "Nenhuma") for t in sec_tools)
                or not sec_tools)
    if no_policy and no_tools:
        return 0.0

    score = 0

    # Policy
    if _matches(policy, "política formal e clara"): score += 2
    elif _matches(policy, "pouco clara"): score += 1
    elif _matches(policy, "informal"): score += 0.5

    # Knows which data is allowed
    if _matches(knows_data, "Sei claramente"): score += 1
    elif _matches(knows_data, "Tenho ideia geral"): score += 0.5

    # Forbidden data list (good if multiple)
    n_forbidden = sum(
        1 for f in forbidden if not _matches(f, "Nenhuma restrição")
    )
    score += min(n_forbidden * 0.2, 1.0)
    if any(_matches(f, "Nenhuma restrição") for f in forbidden):
        score -= 1

    # Security tools breadth
    n_tools = sum(1 for t in sec_tools if not _matches(t, "Nenhuma"))
    score += min(n_tools * 0.3, 2.0)

    # Code scanning gate
    if _matches(scan_in_pr, "gate obrigatório"): score += 1
    elif _matches(scan_in_pr, "Sim, opcional"): score += 0.5

    # SBOM
    if _matches(sbom, "automatizado"): score += 0.5

    # Review process
    if _matches(review, "obrigatório por outro humano + scanner"):
        score += 1
    elif _matches(review, "Review humano obrigatório"): score += 0.5

    # Red-lines for agents (critical for advanced)
    if _matches(red_lines, "Sempre"): score += 1
    elif _matches(red_lines, "Frequentemente"): score += 0.5

    # JIT permissions
    if _matches(jit, "JIT obrigatório"): score += 1
    elif _matches(jit, "Sim, opcional"): score += 0.5

    # DLP
    if _matches(dlp, "bloqueia ativamente"): score += 0.5
    elif _matches(dlp, "alerta"): score += 0.25

    # Audit
    if _matches(audit, "logs ativos e revisados"): score += 0.5
    elif _matches(audit, "ativos mas não revisados"): score += 0.25

    # Training
    if _matches(training, "obrigatório anual"): score += 0.5
    elif _matches(training, "uma vez"): score += 0.25

    # Map to 0-4 (raw range ~0-12)
    score = max(0, min(score, 12))
    return round(score / 12 * 4, 2)


# =========================================================
# Public API
# =========================================================

# (id, name, scorer, English description). The DS- prefix keeps these
# Developer Survey dimensions apart from the v2 assessment dimensions
# D1 to D9, which have different meanings.
DIMENSIONS = [
    ("DS-D2", "Copilot Adoption", score_D2,
     "Adoption and depth of GitHub Copilot use: frequency, modes "
     "(Ask/Edit/Agent/Coding Agent), features, and measured gain"),
    ("DS-D3", "MS/GH Tooling Breadth", score_D3,
     "Breadth of Microsoft/GitHub ecosystem use: Foundry, Spaces, "
     "Coding Agent, MCP, Spec Kit, and GHAS"),
    ("DS-D4", "AI Dev Practices", score_D4,
     "Structured AI practices: TDD, SDD, pair programming, debugging, "
     "and onboarding"),
    ("DS-D5", "Agent Concepts Mastery", score_D5,
     "Knowledge of advanced concepts (agents, MCP, A2A, handoffs, "
     "subagents, and Agentic DevOps personas), primitive creation, "
     "and testing"),
    ("DS-D6", "Instructions Maturity", score_D6,
     "Instructions file maturity: copilot-instructions.md, AGENTS.md, "
     "CLAUDE.md, maintenance, and a shared prompt library"),
    ("DS-D7", "Best Practices", score_D7,
     "Culture and usability: Champions, DORA/DX metrics, community, "
     "and sharing"),
    ("DS-D8", "Security & Governance", score_D8,
     "AI policy, GHAS, scanners, SBOM, agent scope and red-lines, JIT "
     "permissions, audit, and training"),
]

DIMENSION_DESCRIPTIONS_PT = {
    "DS-D2": "Adoção e profundidade de uso do GitHub Copilot: frequência, "
          "modos (Ask/Edit/Agent/Coding Agent), features, ganho mensurado",
    "DS-D3": "Amplitude de uso do ecossistema Microsoft/GitHub: Foundry, "
          "Spaces, Coding Agent, MCP, Spec Kit, GHAS",
    "DS-D4": "Práticas estruturadas com IA: TDD, SDD, pair programming, "
          "debugging, onboarding",
    "DS-D5": "Conhecimento de conceitos avançados: agentes, MCP, A2A, "
          "handoffs, subagentes, personas Agentic DevOps + criação de "
          "primitives + testes",
    "DS-D6": "Maturidade de instructions files: copilot-instructions.md, "
          "AGENTS.md, CLAUDE.md, manutenção, prompt library compartilhada",
    "DS-D7": "Cultura e usabilidade: Champions, métricas DORA/DX, "
          "comunidade, compartilhamento",
    "DS-D8": "Política de IA, GHAS, scanners, SBOM, escopo+red-lines de "
          "agents, JIT permissions, audit, treinamento",
}


DIMENSION_DESCRIPTIONS_ES = {
    "DS-D2": "Adopción y profundidad de uso de GitHub Copilot: frecuencia, "
             "modos (Ask/Edit/Agent/Coding Agent), funcionalidades y ganancia "
             "medida",
    "DS-D3": "Amplitud de uso del ecosistema Microsoft/GitHub: Foundry, "
             "Spaces, Coding Agent, MCP, Spec Kit y GHAS",
    "DS-D4": "Prácticas estructuradas de IA: TDD, SDD, programación en "
             "pareja, depuración y onboarding",
    "DS-D5": "Conocimiento de conceptos avanzados (agentes, MCP, A2A, "
             "handoffs, subagentes y personas de Agentic DevOps), creación de "
             "primitivas y pruebas",
    "DS-D6": "Madurez de archivos de instrucciones: copilot-instructions.md, "
             "AGENTS.md, CLAUDE.md, mantenimiento y una biblioteca compartida "
             "de prompts",
    "DS-D7": "Cultura y usabilidad: Champions, métricas DORA/DX, comunidad y "
             "compartir conocimiento",
    "DS-D8": "Política de IA, GHAS, scanners, SBOM, alcance y límites rojos "
             "de agentes, permisos JIT, auditoría y capacitación",
}


def dimension_description(did: str, desc_en: str, lang: str = "en") -> str:
    if _lang(lang) == "pt-br":
        return DIMENSION_DESCRIPTIONS_PT.get(did, desc_en)
    if _lang(lang) == "es":
        return DIMENSION_DESCRIPTIONS_ES.get(did, desc_en)
    return desc_en


def label_for(score: Optional[float], lang: str = "en") -> str:
    """Maps score 0-4 to an L0-L4 label (the v1 assessment bands)."""
    lang = _lang(lang)
    if score is None:
        return NO_DATA_LABEL[lang]
    labels = LEVEL_LABELS[lang]
    if score < 0.5: return labels[0]
    if score < 1.5: return labels[1]
    if score < 2.5: return labels[2]
    if score < 3.5: return labels[3]
    return labels[4]


def score_respondent(responses: dict, lang: str = "en") -> dict:
    """Compute all 7 dimensions for a single respondent."""
    responses = canonical_responses(responses)
    out = {}
    for did, name, fn, _ in DIMENSIONS:
        s = fn(responses)
        out[did] = {
            "name": name,
            "score": s,
            "label": label_for(s, lang),
        }
    # Overall: average of non-null dimensions
    valid = [d["score"] for d in out.values() if d["score"] is not None]
    overall = round(sum(valid) / len(valid), 2) if valid else None
    out["overall"] = {
        "name": OVERALL_NAME[_lang(lang)],
        "score": overall,
        "label": label_for(overall, lang),
        "dimensions_scored": len(valid),
    }
    return out


def aggregate_team(respondent_scores: list[dict],
                   lang: str = "en") -> dict:
    """Aggregate individual scores into team averages and distribution."""
    n = len(respondent_scores)
    if n == 0:
        return {"error": "No respondents"}

    # Per-dimension team aggregation
    dims = {}
    for did, name, _, desc_en in DIMENSIONS:
        desc = dimension_description(did, desc_en, lang)
        scores = [
            r[did]["score"] for r in respondent_scores
            if r[did]["score"] is not None
        ]
        if not scores:
            dims[did] = {
                "name": name, "description": desc, "team_score": None,
                "label": label_for(None, lang),
                "respondents_with_score": 0, "distribution": {},
            }
            continue

        avg = round(sum(scores) / len(scores), 2)
        # Distribution by L0-L4
        dist = {"L0": 0, "L1": 0, "L2": 0, "L3": 0, "L4": 0}
        for s in scores:
            if s < 0.5: dist["L0"] += 1
            elif s < 1.5: dist["L1"] += 1
            elif s < 2.5: dist["L2"] += 1
            elif s < 3.5: dist["L3"] += 1
            else: dist["L4"] += 1
        dist_pct = {
            k: round(100 * v / len(scores), 1) for k, v in dist.items()
        }

        dims[did] = {
            "name": name,
            "description": desc,
            "team_score": avg,
            "label": label_for(avg, lang),
            "respondents_with_score": len(scores),
            "distribution_count": dist,
            "distribution_pct": dist_pct,
        }

    # Overall team score (average of respondent overall scores)
    overalls = [
        r["overall"]["score"] for r in respondent_scores
        if r["overall"]["score"] is not None
    ]
    team_overall = (
        round(sum(overalls) / len(overalls), 2) if overalls else None
    )

    return {
        "team_overall_score": team_overall,
        "team_overall_label": label_for(team_overall, lang),
        "n_respondents": n,
        "n_with_overall": len(overalls),
        "dimensions": dims,
    }
