import discord
from discord.ext import commands
import utils.study_embed

class Grouper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="study")
    async def study(self, ctx):
        msg = ctx.message
        await ctx.message.delete()

        help_msg = '''
            Please make sure you are using the command correctly.
            Enter !help to learn how to send study group invite.
        '''
        if not msg.author.bot:
            if msg.content.startswith("!study"):
                # !study Math paper 1 % Moffit % 3:00 pm

                study_params = msg.content[6:]

                # validate
                if len(study_params) != 3:
                    await msg.channel.send(help_msg)

                # isolate params
                topic = study_params.split('% ')[0]
                location = study_params.split('% ')[1]
                time = study_params.split('% ')[2]

                embed = utils.study_embed.study_embed(topic, location, time)
                embed.set_author(
                    name=ctx.author.display_name,
                    icon_url=ctx.author.avatar_url
                )
                await ctx.send(embed=embed)
            
            else:
                help_msg = '''
                Please make sure you are using the command correctly.
                Enter !help to learn how to send study group invite.
                '''
                await msg.channel.send(help_msg)


def setup(bot):
    bot.add_cog(Grouper(bot))