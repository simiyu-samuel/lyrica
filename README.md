<div align="center">

# 🎵 Lyrica

<img src="assets/banner.svg" alt="Lyrica animated banner" width="100%">

### Every word of your favorite song, beautifully presented.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Genius](https://img.shields.io/badge/Genius-API-FFFF64?style=for-the-badge&logo=genius&logoColor=black)](https://genius.com/)
[![License](https://img.shields.io/badge/License-MIT-7C55D9?style=for-the-badge)](LICENSE)

<br>

<a href="#-quick-start">
  <img src="https://img.shields.io/badge/Get_Started-7C55D9?style=for-the-badge" alt="Get started">
</a>
<a href="#-features">
  <img src="https://img.shields.io/badge/Explore_Features-EEE8FB?style=for-the-badge&logoColor=7C55D9" alt="Explore features">
</a>

</div>

---

## ✨ Features

| | |
|:---:|:---|
| 🔍 **Instant Search** | Find lyrics by both song title and artist. |
| 🎬 **Animated Reveal** | Watch every line appear with a smooth, staggered entrance. |
| 🌙 **Dark Mode** | Switch between light and dark themes with a persistent preference. |
| 📋 **Copy Lyrics** | Copy the complete result to your clipboard in one click. |
| 📱 **Responsive Design** | A fluid interface designed for desktop, tablet, and mobile. |
| 🔐 **Secure Token Handling** | Your Genius token stays in environment variables or a local `.env` file. |

---

## 🖼️ Interface

<div align="center">

> Search for a song, choose it, and let the words unfold.

</div>

The interface uses a soft glass surface, ambient gradients, animated equalizer branding, loading bars, animated lyric lines, and a clean serif reading experience.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/simiyu-samuel/lyrica.git
cd lyrica
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Genius

1. Visit <https://genius.com/api-clients>.
2. Create an API client.
3. Generate an access token.
4. Copy `.env.example` to `.env`.
5. Add your token:

```env
GENIUS_ACCESS_TOKEN=your_genius_access_token_here
```

> `.env` is ignored by Git. Never commit or share your access token.

### 5. Run the app

```bash
python app.py
```

Open <http://127.0.0.1:5000>.

---

## 🧱 Project Structure

```text
lyrica/
├── app.py                 # Flask routes and API
├── lyrics.py              # Genius lookup and CLI helpers
├── requirements.txt       # Python dependencies
├── .env.example           # Safe environment template
├── static/
│   ├── script.js          # Search and animations
│   └── style.css          # Interface and themes
├── templates/
│   └── index.html         # Main web page
└── assets/
    └── banner.svg         # Animated README banner
```

---

## 🔌 API

### `POST /api/lyrics`

**Request**

```json
{
  "title": "Bohemian Rhapsody",
  "artist": "Queen"
}
```

**Success**

```json
{
  "title": "Bohemian Rhapsody",
  "artist": "Queen",
  "lyrics": "..."
}
```

---

## 🛠️ Technology

- **Python** for server-side application logic
- **Flask** for routing and JSON responses
- **lyricsgenius** for Genius API access
- **HTML, CSS, and JavaScript** for the animated interface
- **Git & GitHub** for source control and collaboration

---

## 🗺️ Roadmap

- [ ] Add album artwork
- [ ] Add playback audio preview
- [ ] Add song favorites
- [ ] Add lyric search history
- [ ] Deploy publicly

---

<div align="center">

Made with <img src="https://img.shields.io/badge/♪-7C55D9?style=flat-square" alt="music"> and Python.

</div>
