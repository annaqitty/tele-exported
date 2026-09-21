# 🚀 Telegram Channel File Exporter

A fast and lightweight Python tool for **exporting files from Telegram channels** based on selected file extensions.

Simply provide a Telegram channel username or link, choose the extensions you want, and the tool automatically scans the channel and downloads matching files.

> ⚡ Built with Python + Telethon
> 🎯 Extension-based filtering
> 📥 Automatic file downloading
> 🔐 Uses Telegram's official API
> 🧩 Simple CLI interface

---

## ✨ Features

* 🚀 Fast Telegram channel scanning
* 🔎 Filter files by extension
* 📂 Custom output directory
* 🔗 Supports Telegram usernames and links
* 📄 Preserves original filenames when available
* ♻️ Handles duplicate filenames automatically
* 📊 Displays download progress
* 🛡️ Uses Telegram API authentication
* 💻 Works on Windows, Linux, and macOS
* 🐍 Simple Python implementation
* 📦 No Telegram bot required

---

## 📋 Supported Input

You can provide a Telegram channel in several formats:

```text
@channelname
```

or:

```text
https://t.me/channelname
```

or:

```text
https://telegram.me/channelname
```

---

## 📁 Supported Extensions

You can specify one or multiple extensions.

### Single extension

```text
jpg
```

### Multiple extensions

```text
jpg,png,webp
```

### Mixed file types

```text
jpg,png,mp4,pdf,zip,mp3
```

The extension filter is case-insensitive.

For example:

```text
JPG
jpg
Jpg
```

are treated as the same extension.

---

# ⚙️ Requirements

* Python **3.9+**
* Telegram account
* Telegram API ID
* Telegram API Hash

Required Python package:

```bash
pip install telethon
```

---

# 🔑 Telegram API Credentials

You need your own Telegram API credentials.

Go to:

**https://my.telegram.org**

Sign in with your Telegram account and open:

```text
API Development Tools
```

Create an application and obtain:

```text
API_ID
API_HASH
```

Then configure them inside:

```python
API_ID = 12345678
API_HASH = "YOUR_API_HASH"
```

> ⚠️ Never publish your `API_HASH` or Telegram session file in a public repository.

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/telegram-channel-file-exporter.git
```

Enter the directory:

```bash
cd telegram-channel-file-exporter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install Telethon directly:

```bash
pip install telethon
```

---

# ▶️ Usage

Start the program:

```bash
python telegram_export.py
```

You will be asked for the Telegram channel:

```text
Telegram channel username/link:
```

Example:

```text
https://t.me/examplechannel
```

Then select the extensions:

```text
Extensions to download (example: jpg,png,mp4,pdf): jpg,png,mp4
```

Finally choose the output directory:

```text
Output folder [telegram_export]: downloads
```

---

# 🖥️ Example

```text
Telegram channel username/link: https://t.me/examplechannel

Extensions to download (example: jpg,png,mp4,pdf): jpg,png,mp4

Output folder [telegram_export]: downloads

Connected to Telegram.
Channel : https://t.me/examplechannel
Extensions: jpg, mp4, png
Output  : downloads
============================================================

[1] Downloading: image_001.jpg
[2] Downloading: image_002.png
[3] Downloading: video_001.mp4
[4] Downloading: image_003.jpg

============================================================
Finished
Messages scanned : 1250
Files downloaded : 4
Skipped          : 1246
Output folder    : /path/to/downloads
```

---

# 📂 Output

Downloaded files are stored in the selected directory:

```text
downloads/
├── image_001.jpg
├── image_002.png
├── image_003.jpg
└── video_001.mp4
```

If two files have the same filename, the program automatically adds the Telegram message ID:

```text
image.jpg
image_123456.jpg
image_987654.jpg
```

---

# 🧠 How It Works

```text
             ┌─────────────────────┐
             │   Telegram Channel  │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │  Scan Channel       │
             │  Messages          │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Has File?           │
             └──────────┬──────────┘
                        │
                   ┌────┴────┐
                   │         │
                  YES        NO
                   │         │
                   ▼         ▼
          ┌─────────────┐   SKIP
          │ Check       │
          │ Extension   │
          └──────┬──────┘
                 │
            ┌────┴────┐
            │         │
           MATCH     OTHER
            │         │
            ▼         ▼
       DOWNLOAD      SKIP
```

---

# ⚡ Performance

The exporter is designed to avoid unnecessary downloads.

Instead of downloading every file and filtering afterward, the program:

1. Reads the Telegram message
2. Checks whether it contains a document
3. Detects the file extension
4. Compares it against your selected extensions
5. Downloads only matching files

This significantly reduces unnecessary network traffic when working with channels containing many different file types.

---

# 🔐 Authentication

On the first run, Telethon will request your Telegram login information.

A local session file will be created:

```text
telegram_session.session
```

This allows subsequent executions to reuse the authenticated session.

### Important

Do **not** upload this file to GitHub.

Add it to `.gitignore`:

```gitignore
*.session
*.session-journal
__pycache__/
*.pyc
.env
```

---

# 🛡️ Security Recommendations

Never commit credentials such as:

```text
API_ID
API_HASH
Telegram session files
Passwords
Authentication tokens
```

For production usage, consider environment variables:

```bash
TELEGRAM_API_ID=12345678
TELEGRAM_API_HASH=your_api_hash
```

Then load them from Python:

```python
import os

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
```

---

# 📄 requirements.txt

Create:

```text
requirements.txt
```

with:

```text
telethon>=1.36.0
```

Install:

```bash
pip install -r requirements.txt
```

---

# 🗂️ Recommended Project Structure

```text
telegram-channel-file-exporter/
│
├── telegram_export.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
└── downloads/
```

---

# 🐧 Linux

Install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run:

```bash
python3 telegram_export.py
```

---

# 🪟 Windows

Install dependencies:

```powershell
py -m pip install -r requirements.txt
```

Run:

```powershell
py telegram_export.py
```

---

# 🍎 macOS

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run:

```bash
python3 telegram_export.py
```

---

# 🧩 Roadmap

Planned improvements:

* [ ] Concurrent downloads
* [ ] Download progress bars
* [ ] Resume interrupted downloads
* [ ] Date-range filtering
* [ ] Message ID filtering
* [ ] Maximum file-size filtering
* [ ] Download speed display
* [ ] Separate folders by extension
* [ ] Regex filename filtering
* [ ] Duplicate detection
* [ ] Export channel metadata
* [ ] Multi-channel support
* [ ] Config file support
* [ ] CLI arguments
* [ ] Docker support
* [ ] GUI version

---

# ⚠️ Disclaimer

This project is intended for legitimate file-management and archival purposes.

Use it only with Telegram content that you are authorized to access and download. Respect Telegram's Terms of Service, copyright, privacy, and the rights of content owners.

The project is not affiliated with or endorsed by Telegram.

---

# 📜 License

This project is released under the **MIT License**.

See:

```text
LICENSE
```

for details.

---

# ⭐ Support

If this project is useful to you:

⭐ Star the repository
🍴 Fork the project
🐛 Report bugs
💡 Suggest features
🔧 Submit pull requests

---

## 👨‍💻 Author

**YOUR NAME**

Built with ❤️ and Python.

---

## ⭐ GitHub Topics

Recommended repository topics:

```text
telegram
telegram-api
telethon
telegram-downloader
telegram-channel
python
python3
file-downloader
telegram-exporter
telegram-tools
automation
cli
```
