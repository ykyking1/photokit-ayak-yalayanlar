---
name: New Filter Request
about: Request a new image filter for PhotoKit
title: "Add <filter-name> filter"
labels: enhancement
---

## Filter Name
<!-- e.g. blur, sepia, invert -->

## Description
<!-- Ne yapacak? Hangi görsel efekti üretecek? -->

## CLI Usage
<!-- Nasıl çağrılacak? -->
```bash
uv run photokit apply <filter> input.jpg output.jpg [options]
```

## Parameters
<!-- Options var mı? (örn. --radius, --width) -->

## Acceptance Criteria
- [ ] Filtre `src/photokit/filters/<name>.py` altında
- [ ] `registry.py`'ye kaydedildi
- [ ] En az 2 unit test yazıldı
- [ ] `uv run photokit apply <name> ...` çalışıyor
