# Sample Images

Workshop boyunca filtre testleri için hazır resimler. Hepsi **Picsum Photos** (picsum.photos) tarafından sağlanan, ücretsiz ve workshop kullanımına uygun görseller.

## Mevcut Resimler

| Dosya | Boyut | Kullanım |
|-------|-------|----------|
| `test.jpg` | 1200×800 | Varsayılan test resmi — README örneklerinde geçen dosya |
| `landscape.jpg` | 1600×800 | Yatay resim — resize ve crop testleri |
| `portrait.jpg` | 600×900 | Dikey resim — aspect ratio testleri |
| `colorful.jpg` | 800×800 | Renkli/kare — sepia ve invert görsel için |

## Kullanım Örnekleri

```bash
# Grayscale
uv run photokit apply grayscale sample_images/test.jpg out_gray.jpg

# Blur — landscape üzerinde dene
uv run photokit apply blur sample_images/landscape.jpg out_blur.jpg --radius 8

# Sepia — renkli resimde etki belirgin
uv run photokit apply sepia sample_images/colorful.jpg out_sepia.jpg

# Invert — portrait'te dramatik
uv run photokit apply invert sample_images/portrait.jpg out_inv.jpg

# Resize — küçült
uv run photokit apply resize sample_images/landscape.jpg out_small.jpg --width 400
```

## Kendi Resmini Eklemek

Kendi test resimlerini buraya atabilirsin. Öneriler:

- 500×500 ile 2000×1500 arasında boyut
- JPG veya PNG formatı
- Telif hakkı olmayan kaynaklar: [Unsplash](https://unsplash.com), [Pexels](https://pexels.com), [Picsum](https://picsum.photos)
- Çok büyük dosyaları (>2 MB) repo'ya commit etme — `.gitignore`'a ekle

## Kaynak

Resimler `picsum.photos` API'sinden çekildi:

```bash
curl -o test.jpg      "https://picsum.photos/seed/photokit1/1200/800"
curl -o landscape.jpg "https://picsum.photos/seed/landscape/1600/800"
curl -o portrait.jpg  "https://picsum.photos/seed/portrait/600/900"
curl -o colorful.jpg  "https://picsum.photos/seed/colorful/800/800"
```

Picsum Photos, Unsplash'ten ücretsiz ve CC0 lisanslı resimleri serve eder.
