# Contributing

Thank you for helping improve the AI Maturity Assessment kit. This project
follows the [code of conduct](CODE_OF_CONDUCT.md).

## Before you start

- Open an issue first for a large change, a new question or a change to
  scoring rules, so the approach can be agreed.
- Never commit client data. Use the mock data. See [SECURITY.md](SECURITY.md).

## Branches

- Work on a feature branch created from `develop`.
- Open the pull request against `develop`.
- `main` moves forward from `develop` only. Every push to `main` deploys the
  site and publishes a `kits-<run>` release with the language ZIPs.

## Rules for changes

- **Deterministic scripts only.** Scores, gaps, recommendations, imports,
  workbooks, comparisons, evidence checks and reports come from the
  scripts in `scripts/` and `reports/scripts/`. Do not add hand-computed
  values to docs or examples.
- **Framework v2 source.** Edit the English spec
  `collection/AI-Maturity-Form-Questions_v2.md`, run `make generate-v2`,
  then update the prose of the `.pt-br.md` and `.es.md` spec copies. Do not
  edit `framework.v2.json` or the generated banks and HTML helpers by hand.
- **Framework v1 is archived.** Do not change v1 scoring or migrate v1
  inputs by hand.
- **Three languages.** Every doc `X.md` has `X.pt-br.md` and `X.es.md`
  copies with the same headings and a language switcher line. Change the
  three together. HTML helpers follow the same rule. Files in `.github/`
  stay in English only.
- **English names.** Every file and folder name is English. Language copies
  add `.pt-br` or `.es` before the extension.
- **Style.** Plain, short, direct sentences. Do not use em dashes or en
  dashes.
- **Changelog.** Add your change to `CHANGELOG.md`, `CHANGELOG.pt-br.md`
  and `CHANGELOG.es.md`.

## Validate before you push

```bash
make test
make validate-docs
make smoke
make smoke-cross
make demo
```

When you change the framework, also run `make validate-v2` and
`make examples-v2`. CI runs the same checks on every push and pull request
to `main` and `develop`.
