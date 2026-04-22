## Ne?
<!-- Bu PR ne yapıyor? 2-3 cümle -->

## Neden?
<!-- Hangi problemi çözer? Hangi issue'yu kapatır? -->

## Nasıl Test Edeyim?
<!-- Adım adım, reviewer'ın makineye kopyalayabileceği komutlar -->

```bash
# örnek:
uv sync
uv run photokit apply <filter> sample_images/test.jpg out.jpg
```

## Ekran Görüntüsü (Opsiyonel)
<!-- Filtre etkisini gösteren önce/sonra resimleri -->

## Checklist
- [ ] Testler eklendi veya güncellendi
- [ ] `uv run pytest` yeşil
- [ ] `uv run ruff check src tests` yeşil
- [ ] Yeni filtre registry.py'ye kaydedildi
- [ ] Breaking change varsa notlandı

Closes #
