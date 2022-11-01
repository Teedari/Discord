import hikari
from decouple import config

bot = hikari.GatewayBot(token=config('DISCORD_BOT_TOKEN'))


# Events goes here

@bot.listen()
async def bot_initiate(event: hikari.StartedEvent):
  print("BOT INITIATED.....")

@bot.listen()
async def greeting(event: hikari.GuildMessageCreateEvent) -> None:
  if event.is_bot or not event.content:
    return
  
  if event.content.startswith('@bot'):
    await event.message.respond("Hey i'm a bot")


bot.run()