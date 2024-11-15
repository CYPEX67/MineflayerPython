from javascript import require, On, Once, AsyncTask, once, off

# Import the javascript libraries
mineflayer = require("mineflayer")

# Create bot with basic parameters
bot = mineflayer.createBot(
    {"username": "Admin", "host": "192.168.178.146", "port": 25565, "version": "1.20.1", "hideErrors": False}
)

# Login event required for bot
@On(bot, "login")
def login(this):
    pass
