# provider-screening

Vendor screening pipeline (checklist-driven, evidence-cited) for two domains:
`bsg/` and `microsegmentation/`. Built on `.claude/skills/deep-research`.

## Setup

```
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

Requires the `claude` CLI on PATH.

## Chạy thử 1 provider (standard mode)

```
venv/Scripts/python.exe scripts/run_batch.py --domain bsg --mode standard \
  --only zoneguard --timeout 3600 --model deepseek-v4-pro \
  --dangerously-skip-permissions
```

Thêm `--dry-run` để xem lệnh sẽ chạy mà chưa gọi Claude thật.

## Chi tiết

Xem `bsg/GUIDE.md` hoặc `microsegmentation/GUIDE.md` cho từng domain.
