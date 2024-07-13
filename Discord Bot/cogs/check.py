import discord
from discord.ext import commands
from discord import Color
import json
import datetime



class check(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command()
    async def speaktime(self, message: discord.Message):
        with open('c:\Discord Bot\cogs\json dict\delete content.json', 'r',encoding="utf-8") as f:
            text = f.read()
        dict = json.loads(text)
        speakTime = dict[f"{message.author.global_name}"]["speakTime"]
        await message.channel.send(f"<@{message.author.id}>，你傳送過了{speakTime}則訊息")

    @commands.command()
    async def level(self, message: discord.Message):
        with open('c:\Discord Bot\cogs\json dict\delete content.json', 'r',encoding="utf-8") as f:
            text = f.read()
        dict = json.loads(text)
        Level = dict[f"{message.author.global_name}"]["level"]
        await message.channel.send(f"<@{message.author.id}>，你目前為等級{Level}")
        
    @commands.command()
    async def checkInfo(self, message: discord.Message):
        await message.channel.send(f"使用者名稱 : {message.author.name}\n使用者ID : {message.author.id}\n顯示名稱 : {message.author.global_name}\n伺服器暱稱 : {message.author.nick}")

    @commands.command()
    async def role(self, ctx,arg1,arg2):
        guild = ctx.guild
        role = await guild.create_role(name=f"{arg1}", colour=discord.Color.from_str(arg2))
        authour = ctx.message.author
        await authour.add_roles(role)

async def setup(bot: commands.Bot):
    await bot.add_cog(check(bot))