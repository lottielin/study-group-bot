import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def study(self, ctx):
        msg = ctx.message
        if not msg.author.bot:
            if msg.startswith("!help"):
                await msg.channel.send(f"Here's the help msg")

def setup(bot):
    bot.add_cog(Help(bot))