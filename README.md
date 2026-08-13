# provider-screening

Vendor screening pipeline (checklist-driven, evidence-cited). Each domain
(`bsg`, `microsegmentation`, `ngfw`, ...) lives under `providers-workspace/`.
Built on `.claude/skills/deep-research`.

## Setup

```
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pip install -e . --no-deps
python -m patchright install chromium
```

`pip install -e .` (editable install, driven by `pyproject.toml`) is what
makes `scripts.*`, `tools.*`, and `provider_assessment.*` (the
provider-assessment skill's scripts) importable from anywhere in this venv
without manual `sys.path` edits -- required before running anything under
`scripts/batch/`, `tools/`, or `.claude/skills/provider-assessment/scripts/`.
It only wires up this repo's own modules; runtime dependencies still come
from `requirements.txt` (`--no-deps` skips re-resolving them).

Requires the `claude` CLI (subcommand `claude`) or the `pi` CLI (subcommand
`pi`) on PATH, depending on which agent you drive.

`python -m patchright install chromium` downloads the patched Chromium build
used by `tools/htmlstage`'s `stealthy` fetch method (Scrapling's
`StealthyFetcher`) -- separate from any Chromium `pip install` alone gets
you, and separate from plain Playwright's own build, so it needs its own
install step.

## Chạy thử 1 provider (standard mode)

```
venv/Scripts/python.exe scripts/batch/run_batch.py pi --domain bsg --mode standard \
  --only zoneguard --timeout 3600 --model deepseek/deepseek-v4-pro
```

Thêm `--dry-run` để xem lệnh sẽ chạy mà chưa gọi Claude thật.

## Chi tiết

Xem `providers-workspace/<domain>/GUIDE.md` cho từng domain (`bsg`,
`microsegmentation`, `ngfw`, ...).
