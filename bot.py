import hikari
from decouple import config

bot = hikari.GatewayBot(token=config('DISCORD_BOT_TOKEN'))


# Events goes here

bot.run()