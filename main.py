import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("ログインしました！")
    await bot.change_presence(activity=discord.Game(name="1"))

bot.run("MTIzMjQ4MjU5NTI0NjMxMzUyNA.GsR1MR.1Y6Ij89xEIij2_hakkEhqCSe4G2JwzxeAtYvho")
