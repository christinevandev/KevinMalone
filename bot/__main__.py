import logging
import sys
from common.commands import bot
import constants

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Starting...")


def main():
    TOKEN = constants.Bot.token
    if TOKEN is None:
        sys.exit("Environment variable API_TOKEN must be supplied")
    bot.run(TOKEN)


main()
