# 🎵 Discord Music Bot

A Discord music bot built with Python that can play music directly from YouTube using a song name or URL.

## ✨ Features

- ▶️ Play music from YouTube using a song name or link
- ⏸️ Pause the current song
- ▶️ Resume paused music
- ⏹️ Stop the music and disconnect from the voice channel
- 🏓 Ping command to check if the bot is online
- 📖 Built-in help command

---

## 🛠️ Technologies Used

- Python 3
- Discord.py
- yt-dlp
- FFmpeg
- Asyncio

---

## 📂 Project Structure

```bash
Discord-Music-Bot/
│── main.py
│── token.txt
│── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Navigate to the project folder:

```bash
cd Discord-Music-Bot
```

### 2. Create a virtual environment (Optional, but recommended)

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install discord.py yt-dlp
```

---

## ⚙️ Installing FFmpeg

This bot requires FFmpeg to play audio.

### Ubuntu / Linux

```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows

Download FFmpeg and add it to your system PATH.

---

## 🔑 Token Configuration

Create a file called `token.txt` in the project root directory and place your bot token inside:

```txt
YOUR_BOT_TOKEN_HERE
```

**Never share your bot token publicly.**

If your token gets exposed, reset it immediately in the Discord Developer Portal.

---

## ▶️ Running the Bot

After installing everything, run:

```bash
python main.py
```

or on Linux:

```bash
python3 main.py
```

If everything is configured correctly, you should see something like:

```bash
YourBotName#0000 is ready to play!
```

---

## 🎮 Bot Commands

| Command | Description |
|----------|-------------|
| `!play <song>` | Plays a song |
| `!pause` | Pauses the current song |
| `!resume` | Resumes paused music |
| `!stop` | Stops music and disconnects |
| `!ping` | Checks if the bot is online |
| `!help` | Shows command list |

### Example Usage

```bash
!play Eminem - Mockingbird
```

or

```bash
!play https://youtube.com/...
```

---

## 🚀 Inviting the Bot to a Server

In the Discord Developer Portal:

1. Go to **OAuth2 > URL Generator**
2. Select:
   - `bot`
3. Enable the following bot permissions:
   - Connect
   - Speak
   - Send Messages
   - Read Message History

Open the generated URL and add the bot to your server.

---

## 📌 Notes

- The bot only plays one song at a time.
- Using `!play` again will replace the currently playing song.
- You must be connected to a voice channel to use `!play`.

---

## 📄 License

This project is open source and can be freely modified for educational purposes.
