import discord
#Her komutun başına "$" eklemeyi unutmayın.Daha fazla bilgi için "$komutlarnedir" yazabilirsiniz.
from discord.ext.commands import CommandNotFound
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready(): 
    print(f'{bot.user} olarak giriş yaptik')

@bot.command()
async def hello(ctx):
    await ctx.send(f'hello {bot.user}! Im a bot!')



@bot.command()
async def d(ctx):
    await ctx.send(f'd')                  


@bot.command()
async def komutlarnedir(ctx):
    await ctx.send(f'Herkomudun basina $ eklemeyi unutma ve Turkçe harfler kullanma.İşte komutlar:$Kureseliklimdegisikligininetkilerinelerdir')

@bot.command()
async def ulkemizezararlari(ctx):
    with open(r'C:\Users\User\Desktop\ANAPROJE.py\images\matt-palmer-kbTp7dBzHyY-unsplash (1).jpg', 'rb') as f:
        picture = discord.File(f)

    await ctx.send("İklim degisikliginin ulkemize zararlarilarindan biride orman yanginlaridir.Orman yanginlari sonucunda bazi canlilar evsiz kalir.Erozyon,sel vb.doğal afetler artar.",file = picture)


    


    

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("boyle bir komut yok.Komutlari gormek icin'$komutlarnedir'yaziniz.")
    raise error



bot.run("token")
