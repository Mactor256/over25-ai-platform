import os
from dotenv import load_dotenv
from telegram import Bot


load_dotenv()

TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)

CHANNEL_ID = os.getenv(
    "TELEGRAM_CHANNEL_ID"
)


bot = Bot(
    token=TOKEN
)


def format_picks(picks):

    message = """
⚽ DAILY OVER 2.5 AI PICKS

"""


    for pick in picks:

        message += f"""
🔥 {pick['match']}

Probability:
{pick['probability']}%

Odds:
{pick['odds']}

Signal:
{pick['signal']}

----------------
"""


    return message



async def send_picks(picks):

    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=format_picks(picks)
    )
