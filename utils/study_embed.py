import discord

def study_embed(topic, location, time):

    description = '''
    ====================================
    React with  🙌  to join, ❔ for maybe    
    ====================================
    '''
    embed = discord.Embed(
        title='📚 Study Group: '+ topic,
        description = description,
        color=discord.Color.dark_orange()
    )

    embed.add_field(
        name='📍Location: ',
        value=location,
        inline=True
    )

    embed.add_field(
        name='⏰ Time : ',
        value=time,
        inline=True
    )

    return embed
