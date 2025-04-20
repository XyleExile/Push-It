import discord
import requests
from subscriber import add_subscriber, remove_subscriber, load_subscribers, get_all_pushover_keys

# Your tokens here
DISCORD_BOT_TOKEN = ''
PUSHOVER_APP_TOKEN = ''

# Intents setup
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.dm_messages = True  # this is key for DM functionality

# Create the client
client = discord.Client(intents=intents)

def send_pushover(message, user_keys):
    success = True
    for user_key in user_keys:
        payload = {
            'token': PUSHOVER_APP_TOKEN,
            'user': user_key,
            'message': message,
            'priority': 1,
            'title': 'Road To Riches',
            'sound': 'Pushover Echo (long)'
        }
        response = requests.post('https://api.pushover.net/1/messages.json', data=payload)
        print(f"Pushover to {user_key}: {response.status_code}")
        if response.status_code != 200:
            success = False
    return success


@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.strip()

    # Check if this is a DM (Private Channel)
    is_private = isinstance(message.channel, discord.DMChannel)

    # SUBSCRIBE via DM
    if content.startswith('!subscribe') and is_private:
        try:
            user_key = content.split(' ', 1)[1].strip()
            discord_id = message.author.id
            if add_subscriber(discord_id, user_key):
                await message.channel.send("✅ Subscribed successfully!")
            else:
                await message.channel.send("⚠️ You're already subscribed.")
        except IndexError:
            await message.channel.send("❌ Usage: !subscribe <your_pushover_key>")
        finally:
            try:
                await message.delete()
            except discord.Forbidden:
                pass

                
    # UNSUBSCRIBE via DM
    elif content.startswith('!unsubscribe') and is_private:
        discord_id = message.author.id
        if remove_subscriber(discord_id):
            await message.channel.send("🗑️ Unsubscribed successfully.")
        else:
            await message.channel.send("⚠️ You're not currently subscribed.")
        try:
            await message.delete()
        except discord.Forbidden:
            pass


    # PUSH command in server only (not DMs)
    elif content.startswith('!push') and not is_private:
        message_body = content[len('!push'):].strip()
        keys = get_all_pushover_keys()
        if not keys:
            await message.channel.send("❌ No one is subscribed.")
        elif message_body:
            success = send_pushover(message_body, keys)
            if success:
                await message.channel.send("✅ Notification sent to all subscribers.")
            else:
                await message.channel.send("❌ Some notifications may have failed.")
        else:
            await message.channel.send("⚠️ Please provide a message after !push.")

# Run the bot
client.run(DISCORD_BOT_TOKEN)