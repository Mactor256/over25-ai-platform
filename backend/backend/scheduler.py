from apscheduler.schedulers.blocking import BlockingScheduler
import asyncio

from telegram_sender import send_picks



scheduler = BlockingScheduler()



def get_picks():

    return [

        {
        "match":
        "Team A vs Team B",

        "probability":
        75,

        "odds":
        1.80,

        "signal":
        "OVER 2.5"
        }

    ]



@scheduler.scheduled_job(
    "cron",
    hour=8,
    minute=0
)

def morning():

    picks = get_picks()

    asyncio.run(
        send_picks(picks)
    )



scheduler.start()
