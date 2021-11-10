import logging
import os
import sys
from discord.ext import commands

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)
logger.info("Starting...")

bot = commands.Bot(command_prefix="!")

TOKEN = os.getenv("API_TOKEN")
if TOKEN is None:
    sys.exit("Environment variable API_TOKEN must be supplied")


@bot.command(help="Example")
async def suggest(ctx):
    await ctx.send(ctx.message)


# Need to generate token
bot.run(TOKEN)
