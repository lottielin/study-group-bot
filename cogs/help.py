import discord
from discord.ext import commands
import utils.embed

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        msg = ctx.message
        await ctx.message.delete()

        if not msg.author.bot:
            if msg.content.startswith("!help"):
                embed = utils.embed.help_embed()
                embed.set_author(
                    name='Study Grouper Bot'
                )
                await ctx.send(embed=embed)


def setup(bot):
    # bot.remove_command("help")
    bot.add_cog(Help(bot))
    