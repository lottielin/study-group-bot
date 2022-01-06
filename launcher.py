import discord
from bot import StudyBot
from config.settings import DISCORD_TOKEN


bot = StudyBot()
bot.run(DISCORD_TOKEN)