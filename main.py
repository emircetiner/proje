import discord
import CommandNotFound
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'hello {bot.user}! Im a bot!')



@bot.command()
async def Küreselisinmaninetkilerinelerdir(ctx):
    await ctx.send(f'Kutuplarin erimesine yol açar.')                    


@bot.command()
async def komutlarneredeyaziyor(ctx):
    await ctx.send(f'Kanallar bolumunde komutlar kanali vardir.Oraya bakabilirsin')



from discord.ext.commands import CommandNotFound
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        boylebirkomutyokkomutlarabakabilirsin
    raise error



bot.run("enterbotcode")
