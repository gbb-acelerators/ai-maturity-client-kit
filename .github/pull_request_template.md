## Summary

<!-- What changed and why. Link the issue: Fixes #123 -->

## Checklist

- [ ] The pull request targets `develop`.
- [ ] No client data (responses, Forms or survey exports, metrics,
      `output/`) is included.
- [ ] Docs changed in the three languages (`X.md`, `X.pt-br.md`,
      `X.es.md`), or no doc changed.
- [ ] Framework changes were made in the English spec and regenerated
      with `make generate-v2`.
- [ ] `CHANGELOG.md`, `CHANGELOG.pt-br.md` and `CHANGELOG.es.md` updated.
- [ ] `make test`, `make validate-docs`, `make smoke`, `make smoke-cross`
      and `make demo` pass locally.
- [ ] No em dashes or en dashes added.
