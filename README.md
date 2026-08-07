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

## Chạy full toàn trình (screen → promote → standard → render → aggregate)

```
venv/Scripts/python.exe scripts/run_pipeline.py --domain bsg
venv/Scripts/python.exe scripts/run_pipeline.py --domain microsegmentation
```

Chỉ nhận `--domain`. Model/timeout/permission dùng cho mọi bước được cố định
trong `PIPELINE_*` ở đầu `scripts/run_pipeline.py`.

## Chạy thử 1 provider (standard mode)

```
venv/Scripts/python.exe scripts/run_batch.py --domain bsg --mode standard \
  --only zoneguard --timeout 3600 --model deepseek-v4-pro \
  --dangerously-skip-permissions
```

Đổi `--mode standard` thành `--mode screen` để chạy nhanh 6 item gate thay vì
full 24 item checklist. Thêm `--dry-run` để xem lệnh sẽ chạy mà chưa gọi
Claude thật.

## Chi tiết

Xem `bsg/GUIDE.md` hoặc `microsegmentation/GUIDE.md` cho từng domain.
