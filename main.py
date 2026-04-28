import discord
from discord.ext import commands

# Bot setup
bot = commands.Bot(command_prefix='!')

# Music command framework
@bot.command()
async def play(ctx, url):
    await ctx.send(f'Playing music from {url}')

if __name__ == '__main__':
    bot.run('YOUR_BOT_TOKEN')