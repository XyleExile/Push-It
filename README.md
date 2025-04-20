# 🔔 Discord to Pushover Notification Bot

A Python-based Discord bot that allows users to send real-time Pushover notifications through Discord commands. Perfect for urgent alerts, signals, or community-wide announcements.

---

## ✨ Features

- `/push <message>`: Sends high-priority Pushover notifications to all subscribed users.
- `!subscribe <pushover_user_key>`: (via DM) Privately subscribe to notifications.
- `!unsubscribe`: (via DM) Unsubscribe from future alerts.
- Stores Discord User ID along with the Pushover key.

---

## 📱 Use Case

> In any server channel:
>
> !push The market is volatile! Take action now.
>
> All subscribed users will immediately receive a high-priority Pushover notification with the message.

---

## 🔐 Privacy and Security

- Users **must DM** the bot to subscribe using their Pushover key.
- Keys are stored along with Discord User IDs for future reference.
- No messages or keys are stored publicly or exposed in any channels.

---

## 🔧 Tech Stack

- **Language**: Python 3.x
- **Libraries**: `discord.py`, `requests`
- **Notifications**: [Pushover](https://pushover.net/)
- **Data Storage**: Simple `JSON`-based file for storing user keys

---

## 🚀 Getting Started

### 1. Clone the repository
- bash
- git clone https://github.com/yourusername/discord-pushover-bot.git
- cd discord-pushover-bot

### 2. Install dependencies
>pip install -r requirements.txt

## 3. Configure your credentials
Open the Python script and add your tokens:

```
DISCORD_BOT_TOKEN = 'your-discord-token-here'
PUSHOVER_APP_TOKEN = 'your-pushover-app-token-here'
```

## 4. Run the bot
>push_it.py

## 📬 How to Subscribe as a User
1. DM the bot with:
!subscribe your_pushover_user_key

2. Bot will confirm your subscription

To unsubscribe:
!unsubscribe

---

Requirements:
- Python 3.8+
- A Discord bot token
- A Pushover application token

🙌 Credits
Created with 💻 and ☕ by XyleExile. Inspired by the need for fast, private notifications during time-sensitive events.

