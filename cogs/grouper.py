import discord
from discord.ext import commands

class Grouper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="study")
    async def study(self, ctx):
        msg = ctx.message
        if not msg.author.bot:
            if msg.content.startswith("!study"):
                await msg.channel.send(f"Study msg sent by {msg.author}")

def setup(bot):
    bot.add_cog(Grouper(bot))