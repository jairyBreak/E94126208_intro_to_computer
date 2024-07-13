import discord
from discord import app_commands
from discord.ext import commands
import requests
url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-4603AFC8-930D-4564-B803-510166A0CB06'

class Weather(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 前綴指令
    @commands.command()
    async def weather(self, ctx: commands.Context,arg):
        data = requests.get(url)   # 取得 JSON 檔案的內容為文字
        data_json = data.json()
        #print(type(data_json))    # 轉換成 JSON 格式
        location = data_json["records"]["location"]
        for i in location:
            name = i["locationName"]
            for j in range(3):
                goo1 = i["weatherElement"][0]["time"][j]["startTime"]
                goo2 = i["weatherElement"][0]["time"][j]["endTime"]
                good = i["weatherElement"][0]["time"][j]["parameter"]["parameterName"]
                rain = i["weatherElement"][1]["time"][j]["parameter"]["parameterName"]
                MinT = i["weatherElement"][2]["time"][j]["parameter"]["parameterName"]
                MaxT = i["weatherElement"][4]["time"][j]["parameter"]["parameterName"]
                if name == arg:
                    #print(f'臺南 {goo1}至{goo2} 天氣狀態:{good}  降雨機率:{rain}  溫度:{MaxT}-{MinT}')
                    await ctx.send(f'{arg}  {goo1}至{goo2} 天氣狀態:{good}  降雨機率:{rain}%  溫度:{MaxT}-{MinT}度')
                    #await ctx.send(f'{city}')
    
    @commands.command()
    async def hola(self, ctx,arg ):
        await ctx.send(arg)

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Weather(bot))