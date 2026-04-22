# Git & GitHub Workshop — PhotoKit Starter

Bu repo, **Git, GitHub ve Proje Yönetimi Workshop'u** için starter projedir. PhotoKit adında komut satırından resimlere filtre uygulayan bir Python aracıdır. Workshop boyunca takımlar halinde bu repo'ya yeni filtreler ekleyeceksiniz.

## Workshop Dokümanı

Tüm workshop içeriği `workshop/photokit-workshop.html` dosyasındadır. Tarayıcıda açın, sol taraftaki TOC ile bölümler arasında gezinin.

```bash
# macOS
open workshop/photokit-workshop.html

# Linux
xdg-open workshop/photokit-workshop.html

# Windows
start workshop/photokit-workshop.html
```

## Hızlı Başlangıç

### 1. Ön-koşullar

Workshop öncesi `workshop/kurulum-rehberi.md` dosyasını takip edip şunları kurmuş olmalısın:

- **Git** — `git --version`
- **GitHub CLI** — `gh --version` + `gh auth status` (Logged in)
- **UV** — `uv --version`

### 2. Repo'yu Klonla

```bash
gh repo clone <your-team>/git-github-workshop
cd git-github-workshop
```

### 3. Bağımlılıkları Kur

```bash
uv sync
```

Bu komut `.venv/` içine Pillow, click, rich, pytest ve ruff'ı kurar (uv.lock dosyası sayesinde herkeste aynı sürümler).

### 4. CLI'yi Dene

```bash
uv run photokit list
# Ciktida: grayscale

uv run photokit apply grayscale sample_images/test.jpg out.jpg
# out.jpg olusturuldu — gri tonlama uygulandi
```

## Proje Yapısı

```
git-github-workshop/
├── pyproject.toml           # UV projesi ve dependency'ler
├── README.md
├── .gitignore
├── .python-version
├── src/
│   └── photokit/
│       ├── __init__.py
│       ├── cli.py           # click tabanli CLI
│       ├── registry.py      # Filtre kaydi (CONFLICT NOKTASI)
│       ├── filters/
│       │   ├── __init__.py
│       │   ├── base.py      # Filter base class
│       │   └── grayscale.py # Tek hazir filtre (referans)
│       └── utils/
│           └── io.py
├── tests/
│   ├── __init__.py
│   └── test_grayscale.py
├── sample_images/
│   └── README.md            # Test resimleri burada
├── workshop/
│   ├── photokit-workshop.html
│   └── kurulum-rehberi.md
└── .github/
    ├── workflows/
    │   └── ci.yml           # pytest + ruff
    └── pull_request_template.md
```

## Workshop Boyunca Eklenecek Filtreler

| # | Filter | Sorumlu Rol |
|---|--------|-------------|
| 1 | Blur (Gaussian) | 🟢 Contributor 1 |
| 2 | Sepia | 🔵 Contributor 2 |
| 3 | Invert | 🟡 Contributor 3 |
| 4 | Resize | 🟠 Contributor 4 |

Detaylı adımlar için `workshop/photokit-workshop.html` → Bölüm 06.

## Test Çalıştırma

```bash
uv run pytest -v           # Tüm testler
uv run ruff check src tests # Lint
```

## Commit ve PR Kuralları

- Commit mesajları **İngilizce, imperative mood**: `feat: add blur filter`
- Conventional Commits prefix'i: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
- Her PR bir issue'yu kapatsın: `Closes #N`
- PR açıklaması için `.github/pull_request_template.md` şablonu otomatik dolacak

## Lisans

MIT — eğitim amaçlı. Katılımcılar workshop sonrası bu repo'yu kendi projelerine fork edebilir.
