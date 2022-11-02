import lightbulb
from hikari import StartedEvent
from decouple import config
import datetime

# instantiate bot app
bot = lightbulb.BotApp(token=config('DISCORD_BOT_TOKEN'))


# Events goes here
@bot.listen()
async def initiate_bot(event: StartedEvent):
  print('Bot has started')


@bot.command
@lightbulb.command('ping', 'check the bot is alive')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
  await ctx.respond('Pong!!')
  
@bot.command
@lightbulb.command('greeting', 'say greeting')
@lightbulb.implements(lightbulb.SlashCommand)
async def greeting(ctx: lightbulb.Context):
  await ctx.respond('Hey, I"m kwaku the bot')
  

# Grouping commands
@bot.command
@lightbulb.command('momo', 'This is a momo api command')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def momo(ctx: lightbulb.Context):
  pass


# 
@momo.child
@lightbulb.command('wallet', 'this checks for wallet information')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def wallet(ctx: lightbulb.Context):
  await ctx.respond(f'Account number is SA {1918000032}')


  
  
  
bot.run()