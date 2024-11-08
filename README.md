# Telegram bot

The current implementation of this telegram bot greets any users that joins in the chat group.

For additional features from the telegram bot API, do visit the official telegram bot API on [Telegram Bot API](https://core.telegram.org/api) or Telegram's Bot API wrapper for Python from [python-telegram-bot](https://docs.python-telegram-bot.org/en/v21.7/index.html)

## Setting up the Bot

### Installation of required dependencies

First when you download this repository on your local machine, you would need to install the required packages that is needed for the telegram bot to run.

Run this command on your terminal:

```
pip3 -r /path/to/requirements.txt
```

### Setting environment variables

To set environment variables such as the API Token for the telegram bot, you would first need to create a `.env` file at the root directory of the project.

In the `.env` file, fill this up:

```
API_TOKEN=your bot token here
```

Fill in your Bot token you got from telegram's botfather.

## Running the script

To run the python script after setting all up, in your terminal run:

```
python3 testbot.py
```

You should see the logs from the terminal stating the application has started.
