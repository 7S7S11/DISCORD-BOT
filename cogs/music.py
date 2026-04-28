from discord.ext import commands

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, track):
        pass

    @commands.command()
    async def stop(self, ctx):
        pass

def setup(bot):
    bot.add_cog(MusicCog(bot))
