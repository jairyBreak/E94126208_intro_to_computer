import discord
from discord.ext import tasks, commands
import datetime


class TaskTime(commands.Cog):


    tz = datetime.timezone(datetime.timedelta(hours = 8))
    everyday_time = datetime.time(hour = 0, minute = 0, tzinfo = tz)

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.everyday.start()

    @tasks.loop(time = everyday_time)
    async def everyday(self):
        
        channel_id = 864501430613966850
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(
            title = "🛏 晚安！",
            description = f"🕛 現在時間 {datetime.date.today()} 00:00",
            color = discord.Color.orange()
        )
        await channel.send(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(TaskTime(bot))