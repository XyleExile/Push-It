# 🔔 Discord to Pushover Notification Bot

A Python-based Discord bot that allows users to send **real-time Pushover notifications** through Discord commands.  
Perfect for urgent alerts, crypto/stock signals, or high-priority community announcements.

---

## ✨ Features

- `!push <message>` – Send high-priority push notifications to all subscribed users.
- `!subscribe <pushover_user_key>` – (via DM) Subscribe to alerts privately.
- `!unsubscribe` – (via DM) Remove your Pushover key from the subscription list.
- 🧠 Stores Discord User IDs alongside their Pushover keys.

---

## 📱 Example Use Case

> In any server channel:

```text
!push The market is volatile! 🚨 Take action now.
```

> ✅ All subscribed users instantly receive a high-priority Pushover alert with the message.

---

## 🔐 Privacy & Security

- Users **must DM** the bot to subscribe (ensures keys aren't exposed in public).
- Subscriptions are stored as `{ discord_id, pushover_key }` in a JSON file.
- All data is kept local and private – no third-party tracking.

---

## 🧰 Tech Stack

| Component     | Tech                     |
|---------------|--------------------------|
| Language      | Python 3.x               |
| Bot Framework | `discord.py`             |
| Notifications | [Pushover](https://pushover.net) |
| Storage       | Local `JSON` file        |
| Hosting       | [Heroku](https://heroku.com) or local/VPS |

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8+
- A Discord bot token (from [Discord Developer Portal](https://discord.com/developers/applications))
- A Pushover app token (from [Pushover dashboard](https://pushover.net/apps))

---

### 🛠️ Setup Steps

#### 1. Clone the repository

```bash
git clone https://github.com/yourusername/discord-pushover-bot.git
cd discord-pushover-bot
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Add your tokens using environment variables

In your `bot.py`, make sure your tokens are read like this:

```python
import os

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PUSHOVER_APP_TOKEN = os.getenv("PUSHOVER_APP_TOKEN")
```

Then in **Heroku** or locally, define these environment variables.

#### 4. Create required files

Make sure these files are in the project:

- `bot.py`
- `subscriber.py`
- `Procfile`
- `requirements.txt`

#### 5. Run the bot locally

```bash
python bot.py
```

---

## ☁️ Deploying to Heroku (Free Hosting)

#### 1. Login to Heroku

```bash
heroku login
```

#### 2. Create Heroku app

```bash
heroku create pushit-bot
```

#### 3. Add Heroku config variables

Go to **Heroku Dashboard → Settings → Reveal Config Vars** and add:

| Key                   | Value                      |
|------------------------|----------------------------|
| DISCORD_BOT_TOKEN      | your Discord bot token     |
| PUSHOVER_APP_TOKEN     | your Pushover app token    |

#### 4. Push to Heroku

```bash
git add .
git commit -m "Initial Heroku deployment"
git push heroku master
```

(If your branch is `main`, use `git push heroku main` instead.)

#### 5. Scale the bot

```bash
heroku ps:scale worker=1
```

---

## 🧪 How Users Subscribe

### Subscribe

> DM the bot:

```
!subscribe your_pushover_user_key
```

✅ The bot will confirm your subscription and delete the message.

### Unsubscribe

> DM the bot:

```
!unsubscribe
```

✅ You’ll be removed from the alert list.

---

## 📂 File Structure

```
📦 discord-pushover-bot/
├── bot.py                 # Main bot logic
├── subscriber.py          # Subscriber manager
├── requirements.txt       # Python dependencies
├── Procfile               # Heroku startup config
└── subscribers.json       # Auto-generated subscriber data
```

---

## 🙌 Credits

Built with 💻, ☕, and 💡 by **XyleExile**  
Inspired by the need for fast, private, mobile-first notifications.

---

## 🪪 License

MIT License – Use freely and modify as you wish.

```

---
