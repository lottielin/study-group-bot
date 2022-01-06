import discord
from discord.ext import commands

extensions = (
    "cogs.grouper",
    "cogs.help"
)

class StudyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        prefix = "!"
        super().__init__(command_prefix=prefix)

        self.remove_command("help")

        for ext in extensions:
            self.load_extension(ext)


    async def on_ready(self):
        print('Logged in as {0.user}'.format(self))

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)