from discord.ext import commands
import discord, asyncio
token = ""
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
@bot.event
async def on_ready():
    activity = discord.Game(name="McGroups! | .gg/groups", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")
    
bot.run(token)    
