import json
from pathlib import Path

SUBSCRIBERS_FILE = Path("subscribers.json")

# Load full list of subscribers
def load_subscribers():
    if SUBSCRIBERS_FILE.exists():
        with open(SUBSCRIBERS_FILE, "r") as f:
            return json.load(f)
    return []

# Save subscribers back to file
def save_subscribers(subscribers):
    with open(SUBSCRIBERS_FILE, "w") as f:
        json.dump(subscribers, f, indent=2)

# Add a new subscriber
def add_subscriber(discord_id, pushover_key):
    subs = load_subscribers()
    for sub in subs:
        if sub["discord_id"] == discord_id or sub["pushover_key"] == pushover_key:
            return False  # already subscribed
    subs.append({"discord_id": discord_id, "pushover_key": pushover_key})
    save_subscribers(subs)
    return True

# Remove subscriber by discord_id
def remove_subscriber(discord_id):
    subs = load_subscribers()
    new_subs = [s for s in subs if s["discord_id"] != discord_id]
    if len(new_subs) < len(subs):
        save_subscribers(new_subs)
        return True
    return False

# Get just the pushover keys (used for sending)
def get_all_pushover_keys():
    return [s["pushover_key"] for s in load_subscribers()]
