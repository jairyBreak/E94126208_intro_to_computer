import discord
from discord.ext import commands
import json
import datetime

# 定義名為 Main 的 Cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 前綴指令
    @commands.command()
    async def Hello(self, ctx: commands.Context):
        await ctx.send("Hello, world!")



    #傳送刪除或編輯過的訊息
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        today = datetime.datetime.today()
        author = message.author.global_name
        await message.channel.send(f"{author} delete a message at {message.channel}.")
        with open('c:\Discord Bot\cogs\json dict\delete content.json', 'r',encoding="utf-8") as f:
            text = f.read()
        dict = json.loads(text)
        print (f"{author}" in dict.keys())
        if (f"{author}" in dict.keys()) == False:
            dict[f"{author}"] = {}
        if ("delete_content" in dict[f"{author}"].keys()) == False:
            dict[f"{author}"]["delete_content"] = {}
        dict[f"{author}"]["delete_content"][f"{today.ctime()}"] = {"content":f"{message.content}","channel": f"{message.channel}" ,"server":f"{message.guild}"}
        print(dict)
        with open('c:\Discord Bot\cogs\json dict\delete content.json', 'w',encoding="utf-8") as f:
            f.write(json.dumps(dict, indent = 4))

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        author = message.author.global_name
        with open('c:\Discord Bot\cogs\json dict\delete content.json', 'r',encoding="utf-8") as f:
            text = f.read()
        dict = json.loads(text)
        #print (f"{author}" in dict.keys())
        if (f"{author}" in dict.keys()) == False:
            dict[f"{author}"] = {}
        #print ("speakTime" in dict[f"{author}"].keys())
        if ("speakTime" in dict[f"{author}"].keys()) == False:
            dict[f"{author}"]["speakTime"] = 0
        if ("ID" in dict[f"{author}"].keys()) == False:
            dict[f"{author}"]["ID"] = message.author.id
        dict[f"{author}"]["speakTime"] += 1
        dict[f"{author}"]["level"] = int((dict[f"{author}"]["speakTime"])/100) + 1
        print(dict)
        with open('c:\Discord Bot\cogs\json dict\delete content.json', 'w',encoding="utf-8") as f:
            f.write(json.dumps(dict, indent = 4))
        

    
    @commands.Cog.listener()
    async def on_message_edit(self, message1: discord.Message,message2: discord.Message):
        author = message1.author.global_name
        await message1.channel.send(f"{author} edit a message at {message1.channel}.\nThe content before edit is \"{message1.content}\"")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(1261657295847292988)
        await channel.send(f"Welcome! {member.global_name} just join the server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.bot.get_channel(1261657295847292988)
        await channel.send(f"Bye! {member.global_name} just leave the server.")

    
# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))