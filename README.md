# 📥 VD Downloader

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows/Linux/MacOS-lightgrey.svg)

Un'applicazione per scaricare video da YouTube e tutti i principali social media.

## ✨ Caratteristiche

- 📺 **YouTube** - Video, playlist, canali
- 📷 **Instagram** - Reels, post, storie
- 🎵 **TikTok** - Video
- 🐦 **Twitter/X** - Video
- 📘 **Facebook** - Video
- 💼 **LinkedIn** - Video

- Interfaccia grafica moderna e intuitiva
- Supporto multi-piattaforma (Windows, Linux, macOS)
- Opzioni di qualità e formato
- Download multipli in coda

## 🖥️ Anteprima

```
<img width="650" height="587" alt="Schermata da 2026-02-18 17-41-08" src="https://github.com/user-attachments/assets/c5573dbf-d838-4584-8546-61ac13bda692" />

```

## 📦 Installazione

### Da PyPI (futuro)
```bash
pip install vddownloader
vddownloader
```

### Da sorgente
```bash
# Clona il repository
git clone https://github.com/YOUR_USERNAME/video-downloader.git
cd video-downloader

# Installa le dipendenze
pip install -r requirements.txt

# Esegui
python vddownloader/app.py
```

### Per sviluppatori
```bash
# Clona
git clone https://github.com/YOUR_USERNAME/video-downloader.git

# Installa in modalità sviluppo
pip install -e .

# Esegui
vddownloader
```

## 🐳 Docker (opzionale)

```bash
# Build
docker build -t vddownloader .

# Esegui
docker run -v ~/Downloads:/home/user/Downloads vddownloader
```

## 📋 Requisiti

- Python 3.8+
- yt-dlp
- tkinter (incluso in Python su Windows, da installare su Linux)

### Linux
```bash
sudo apt install python3-tk
```

### macOS
```bash
brew install python-tk
```

## ⚠️ Note

- Alcuni video potrebbero richiedere l'accesso al browser per i cookie
- Usa `--cookies-from-browser chrome` con yt-dlp per Instagram
- YouTube potrebbe bloccare alcuni download con restrizioni

## 🤝 Contribuire

1. Fork il progetto
2. Crea un branch (`git checkout -b feature/nuova-funzione`)
3. Commita le modifiche (`git commit -m 'Aggiunta nuova funzione'`)
4. Pusha sul branch (`git push origin feature/nuova-funzione`)
5. Apri una Pull Request

## 📝 License

MIT License - vedi [LICENSE](LICENSE) per dettagli.

---

⭐ Se ti piace questo progetma, lasci una stella!
