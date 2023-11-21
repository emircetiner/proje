import discord
#Her komutun başına "$" eklemeyi unutmayın.Daha fazla bilgi için "$komutlarnedir" yazabilirsiniz.Bazı bot cevapları geç gelebilir.(5-6 saniye)
from discord.ext.commands import CommandNotFound
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready(): 
    print(f'{bot.user} olarak giriş yaptik')



@bot.command()
async def nasilonlenir(ctx):
    with open(r'C:\Users\User\Desktop\ANAPROJE.py\images\chris-leboutillier-TUJud0AWAPI-unsplash.jpg', 'rb') as f:
        picture = discord.File(f)

    await ctx.send("İklim değişikliliğini önlemek için ağaçlandırma,fosil yakıt kullanmama,benzinli araç kullanmama,fabrikalara filtre takmak vb. yapılabilir.",file = picture)



               
@bot.command()
async def iklimdegisikliliginedir(ctx):
    with open(r'C:\Users\User\Desktop\ANAPROJE.py\images\linus-nylund-Q5QspluNZmM-unsplash.jpg', 'rb') as f:
        picture = discord.File(f)

    await ctx.send("İklim değişikliliği uzun dönemde dünyamıza zarar verebilecek değişiklikler yaratır.Bunlara örneğin:gıda ve su kıtlığı,bazı canlıların neslinin tükenmesi,fırtınalar vb. gibi zararları vardır.",file = picture)


@bot.command()
async def komutlarnedir(ctx):
    await ctx.send(f'Herkomudun basina $ eklemeyi unutma ve Turkçe harfler kullanma.İşte komutlar:$ulkemizezararlari,$kutuplarazararlari,$iklimdegisikliliginedir,$nasilonlenir,Quiz başlatmak için:$quiz')

@bot.command()
async def ulkemizezararlari(ctx):
    with open(r'C:\Users\User\Desktop\ANAPROJE.py\images\matt-palmer-kbTp7dBzHyY-unsplash (1).jpg', 'rb') as f:
        picture = discord.File(f)

    await ctx.send("İklim degisikliginin ulkemize zararlarilarindan biride orman yanginlaridir.Orman yanginlari sonucunda bazi canlilar evsiz kalir.Erozyon,sel vb.doğal afetler artar.",file = picture)

@bot.command()
async def kutuplarazararlari(ctx):
    with open(r'C:\Users\User\Desktop\ANAPROJE.py\images\jesse-orrico-NjpmEtVr6i4-unsplash.jpg', 'rb') as f:
        picture = discord.File(f)

    await ctx.send("Kuzey kutbu'nda donmuş olan buzulların erimesine ve buzulların geri çekilmesine neden olur.",file = picture)


@bot.command()
async def d(ctx):
    with open(r'C:\Users\User\Desktop\ANAPROJE.py\images\jesse-orrico-NjpmEtVr6i4-unsplash.jpg', 'rb') as f:
        picture = discord.File(f)

    await ctx.send("Kuzey kutbu'nda donmuş olan buzulların erimesine ve buzulların geri çekilmesine neden olur.",file = picture)

    
@bot.command()
async def quiz(ctx):
    puan = 0
    await ctx.send("Her soru 5 puandır.Cevapları küçük harfle yazınız.Soru 1 için '$s1' yazınız.Cevap için '$c1 cevabınız' şeklinde yapınız.Hangi sorudaysanız $c 'nin yanındaki sayıya soru numarasını yazınız.")
    @bot.command()
    async def s1(ctx):
        await ctx.send("""1.Soru iklim değişikliği zararlı mıdır? \n 
                       - evet \n
                       - hayır \n
                       (Cevap vermek için $c1 yazıp.Cevabınızı küçük harflerle yazınız.)
                       """)
    @bot.command()
    async def c1(ctx,cevap):
        if cevap == "evet":
            await ctx.send("Doğru cevap.Soru 2 için '$s2' yazınız.")
            puan += 5
        if cevap == "hayir":
            await ctx.send("Maalesef bilemedin doğru cevap evet zarar verir.Soru 2 için '$s2' yazınız.")

    @bot.command()  
    async def s2(ctx):
        await ctx.send("""2.soru kuraklığa yol açar mı? \n
                       - evet \n
                       - hayır \n
                       (Cevap vermek için $c2 yazıp.Cevabınızı küçük harflerle yazınız.)""")  

    @bot.command()
    async def c2(ctx,cevap):
        if cevap == "evet":
            await ctx.send("Doğru cevap.Soru 3 için '$s3' yazınız.")
            puan += 5
        if cevap == "hayir":
            await ctx.send("Maalesef bilemedin doğru cevap evet yol açar.Soru 3 için '$s3' yazınız.")
    @bot.command()
    async def s3(ctx):
        await ctx.send("""3.soru Filtresiz fabrikalar yararlı mıdır? \n
                       - evet \n
                       - hayır \n
                       (Cevap vermek için $c3 yazıp.Cevabınızı küçük harflerle yazınız.)""")
    @bot.command() 
    async def c3(ctx,cevap):   
        if cevap == "evet":
            await ctx.send("Maalesef bilemedin doğru cevap hayır yararlı değildir.Aksine zararlıdır.Soru 4 için '$s4' yazınız.")
            
        if cevap == "hayir":
            await ctx.send("Doğru cevap.Soru 4 için '$s4' yazınız.")
            puan += 5
    @bot.command()
    async def s4(ctx):
        await ctx.send("""4.soru İklim değişikliliği kuraklığa yol açar mı? \n
                       - evet \n
                       - hayır \n
                       (Cevap vermek için $c4 yazıp.Cevabınızı küçük harflerle yazınız.)""")
    @bot.command()
    async def c4(ctx,cevap):
        if cevap == "evet":
            await ctx.send("Doğru cevap.Soru 5 için '$s5' yazınız.")
        if cevap == "hayir":
            await ctx.send("Maalesef bilemedin.Doğru cevap evet kuraklığa yol açar.Soru 5 için '$s5' yazınız.")
    @bot.command()
    async def s5(ctx):
        await ctx.send("""5. soru İklim değişikliliğini biz değiştiremeyiz düşüncesi doğru mudur? \n
                       - evet \n
                       - hayır \n
                       (Cevap vermek için $c5 yazıp.Cevabınızı küçük harflerle yazınız.)""")
    @bot.command()
    async def c5(ctx,cevap):
        if cevap == "evet":
            await ctx.send("Maalesef bilemedin.Doğru cevap değiştirebiliriz.Quiz sonucunuzu öğrenmek için '$sonuc' yazınız")
        if cevap == "hayir":
            await ctx.send("Doğru cevap.Quiz sonucu için '$sonuc' yazınız.")

    @bot.command()
    async def sonuc(ctx):
        if puan == 0:
            await ctx.send("Puanın 0.İklim değişikliliği hakkında pek bir bilgin yok.Sanırım komutlarımdan ve internetten bilgi alıp tekrar deneyebilirsin.")
        if puan == 5:
            await ctx.send("Puanın 5.İklim değişikliliği hakkında ufak bilgilerin var.Komutlarımı okuyup internete bakabilirsin.Ardından tekrak quizi deneyebilirsin.")
        if puan == 10:
            await ctx.send("Puanın 10.İklim değişikliği hakkında az çok bilgilerin var.Kendini bu konuda geliştirip tekrak quizi çözebilirsin.")
        if puan == 15:
            await ctx.send("")

    






@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("boyle bir komut yok.Komutlari gormek icin'$komutlarnedir'yaziniz.Ya da varsa yukardaki bilgiyi okuyabilirsiniz.")
    raise error



bot.run("token")
    
