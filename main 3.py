import guilded
from flask import Flask
import threading

# Create bot instance
bot = guilded.Client(command_prefix="/")

# Basic command
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Flask keep-alive server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Start Flask in a thread
threading.Thread(target=run).start()

# Run the bot
bot.run("YOUR_BOT_TOKEN")
