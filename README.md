# Study Group Bot

study-group-bot is an open source Discord server bot for ....

### Features

### Usage

- Use !study <topic> % <location> % <time> to create a study group invite embed in Discord
- Use !help to retrieve overview of commands and usage

### Installation

Follow the steps below to set up the project on your environment

1. Clone the repo or download manually

```
https://github.com/lottielin/study-group-bot.git
```

2. Move to cloned/downloaded directory

```
cd study_group_bot
```

3. Install required packages:

```
pip3 install -r requirements.txt
```

4. Make a bot from Discord Developer Portal (https://discordapp.com/developers/applications/me); Copy it's token and fill in config.py as TOKEN=<your bot's token>
5. Add the bot to your server using the OAuth2 link

### Deploy on heroku

- Create a new app in heroku and choose your relevant region.
- Fork this repo and make it private.
- Add your API keys or follow 4. and 5. of Installation.
- Add a Procfile with worker as study-bot.py
- Add deployment method as Github in the website.
- Go ahead and deploy on heroku.

### FAQ

- Have any suggestion for a feature? Feel free to raise an issue.
