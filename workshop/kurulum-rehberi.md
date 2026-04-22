# Workshop Öncesi Kurulum Rehberi

Workshop'a başlamadan **önce** lütfen aşağıdaki adımları tamamlayın. Kurulumlar herkes kendi bilgisayarında yapılacak (Windows / macOS / Linux). Sorun yaşarsanız workshop gününe kadar grup kanalından yardım isteyin.

Toplamda yapacaklarınız:

1. GitHub hesabı oluşturmak
2. Git kurmak
3. GitHub CLI (`gh`) kurmak
4. Git'i yapılandırmak (isim, e-posta)
5. GitHub hesabınıza `gh` ile giriş yapmak (auth)
6. Kurulumun doğru olduğunu test etmek

---

## 1. GitHub Hesabı Oluşturma

Zaten hesabınız varsa bu adımı atlayın.

1. https://github.com/signup adresine gidin
2. E-posta, kullanıcı adı ve şifre belirleyin
3. E-postanızı doğrulayın
4. İki faktörlü kimlik doğrulamayı (2FA) aktif etmenizi öneririz: Settings → Password and authentication → Two-factor authentication

**Not:** Kullanıcı adını meslek hayatınızda da kullanacağınız için profesyonel bir isim seçin (örn. `ahmet-yilmaz`, `ayildiz-dev`).

---

## 2. Git Kurulumu

### Windows

**Önerilen yöntem: Git for Windows**

1. https://git-scm.com/download/win adresine gidin
2. İndirdiğiniz installer'ı çalıştırın
3. Kurulum sırasında varsayılan ayarlarla devam edebilirsiniz. Dikkat edilecekler:
   - Default editor: VS Code seçebilirsiniz (kuruluysa)
   - "Git from the command line and also from 3rd-party software" seçili olsun
   - Line endings: "Checkout Windows-style, commit Unix-style" (varsayılan)

**Alternatif (winget ile):**

```powershell
winget install --id Git.Git -e --source winget
```

### macOS

**Önerilen yöntem: Homebrew**

Homebrew yüklü değilse önce onu kurun:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Sonra Git'i kurun:

```bash
brew install git
```

**Alternatif:** Xcode Command Line Tools ile de gelir:

```bash
xcode-select --install
```

### Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install git
```

### Linux (Fedora / RHEL)

```bash
sudo dnf install git
```

### Linux (Arch)

```bash
sudo pacman -S git
```

### Kurulumu Doğrula

Terminal / PowerShell açıp çalıştırın:

```bash
git --version
```

`git version 2.x.x` gibi bir çıktı görmelisiniz.

---

## 3. GitHub CLI (`gh`) Kurulumu

GitHub CLI, komut satırından repo açma, PR oluşturma, auth gibi işlemleri kolaylaştırır.

### Windows

```powershell
winget install --id GitHub.cli
```

Veya https://cli.github.com/ adresinden installer indirin.

### macOS

```bash
brew install gh
```

### Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install gh
```

Eski Ubuntu sürümlerinde `gh` paketi yoksa:

```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

### Linux (Fedora / RHEL)

```bash
sudo dnf install gh
```

### Linux (Arch)

```bash
sudo pacman -S github-cli
```

### Kurulumu Doğrula

```bash
gh --version
```

---

## 4. Git Yapılandırması (Name & Email)

Bu bilgiler her commit'te görünecek, **GitHub hesabınızdaki e-posta ile aynı olmalı.**

```bash
git config --global user.name "Ad Soyad"
git config --global user.email "sizin@email.com"
```

Varsayılan branch ismini `main` yapın:

```bash
git config --global init.defaultBranch main
```

Varsayılan editörü ayarlayın (VS Code kullananlar için):

```bash
git config --global core.editor "code --wait"
```

Ayarları kontrol edin:

```bash
git config --list
```

---

## 5. GitHub'a Auth (Giriş)

En kolay yöntem `gh auth login` kullanmak. Bu komut hem Git'i GitHub ile yetkilendirir hem de SSH anahtarını oluşturmak isterseniz size yardım eder.

```bash
gh auth login
```

Sorulanlara şu cevapları verin:

1. **What account do you want to log into?** → `GitHub.com`
2. **What is your preferred protocol for Git operations?** → `HTTPS` (başlangıç için daha kolay) veya `SSH` (daha güvenli)
3. **Authenticate Git with your GitHub credentials?** → `Yes`
4. **How would you like to authenticate?** → `Login with a web browser`
5. Ekranda çıkan **one-time code**'u kopyalayın
6. Tarayıcı otomatik açılacak, kodu yapıştırın, GitHub'a giriş yapın ve izin verin

Doğrula:

```bash
gh auth status
```

`Logged in to github.com as KULLANICI_ADI` görmelisiniz.

---

## 6. Son Test

Hepsinin çalıştığını kontrol etmek için küçük bir test repo oluşturun:

```bash
gh repo create workshop-test --public --clone
cd workshop-test
echo "# Test" > README.md
git add README.md
git commit -m "ilk commit"
git push origin main
```

GitHub profiliniz altında `workshop-test` reposunu görüyorsanız, **her şey hazır**.

İsterseniz test repo'yu silin:

```bash
cd ..
gh repo delete workshop-test --yes
```

---

## Opsiyonel Öneriler

- **VS Code** veya tercih ettiğiniz bir kod editörü kurulu olsun: https://code.visualstudio.com/
- VS Code kullananlar için faydalı eklenti: **GitLens**
- Terminal'i biraz kullanmaya aşina olmak iyi olur (`cd`, `ls`, `mkdir`, `pwd`)

---

## Kontrol Listesi (Workshop Günü İçin Hazır Mıyım?)

- [ ] GitHub hesabım var ve e-postamı doğruladım
- [ ] `git --version` çalışıyor
- [ ] `gh --version` çalışıyor
- [ ] `git config --list` çıktısında `user.name` ve `user.email` doğru
- [ ] `gh auth status` "Logged in" diyor
- [ ] Test repo'yu oluşturup push edebildim
- [ ] Bir kod editörüm var (VS Code önerilir)

---

## Sorun Yaşarsanız

Aşağıdaki bilgileri ekleyerek grup kanalından yazın:

- İşletim sisteminiz (Windows 11 / macOS Sonoma / Ubuntu 22.04 vb.)
- Hangi adımda takıldığınız
- Aldığınız hata mesajının tamamı (screenshot veya kopya)

Workshop gününe kadar herkes bu adımları tamamlamış olmalı. Görüşürüz!
