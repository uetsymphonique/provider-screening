# provider-screening

Vendor screening pipeline (checklist-driven, evidence-cited) for two domains:
`bsg/` and `microsegmentation/`. Built on `.claude/skills/deep-research`.

## Setup

```
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python -m patchright install chromium
```

Requires the `claude` CLI (subcommand `claude`) or the `pi` CLI (subcommand
`pi`) on PATH, depending on which agent you drive.

`python -m patchright install chromium` downloads the patched Chromium build
used by `scripts/htmlstage`'s `stealthy` fetch method (Scrapling's
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

Xem `bsg/GUIDE.md` hoặc `microsegmentation/GUIDE.md` cho từng domain.
