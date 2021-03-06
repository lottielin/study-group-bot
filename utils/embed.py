import discord
from discord.colour import Color

def study_embed(topic, location, time):

    description = '''
    ====================================
    React with  ๐  to join, โ for maybe    
    ====================================
    '''
    embed = discord.Embed(
        title='๐ Study Group: '+ topic,
        description = description,
        color=discord.Color.dark_orange()
    )

    embed.add_field(
        name='๐Location: ',
        value=location,
        inline=True
    )

    embed.add_field(
        name='โฐ Time : ',
        value=time,
        inline=True
    )

    return embed

def help_embed():
    embed = discord.Embed(
        title='Guide to Study Grouper Bot',
        description='Help message',
        color=discord.Color.light_grey()
    )

    embed.add_field(
        name='Study invite command',
        value='!study <topic> % <location> % <time>',
        inline=False
    )
    embed.add_field(
        name='Example',
        value='!study Midterm 1 review % Moffit % 5:00 pm',
        inline=False
    )
    embed.add_field(
        name='Be careful',
        value='Space before and after %',
        inline=False
    )

    return embed

