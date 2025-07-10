# import requests


# def log_process(log, uid=5030730429):
#       req_url = f"https://api.telegram.org/bot5977798236:AAF_unH81iJf7S95SdgW9YOcoii8aX-CBwU/sendMessage?chat_id={uid}&text={log}"
#       resp = requests.get(req_url)
#       return

# log_process("started")


from pyrogram import Client, filters
import logging
import sys


logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

api_id = 14681826
api_hash = "add59ab14dbbccf3c92c65ca4477f2fa"
bot_token = "5977798236:AAF_unH81iJf7S95SdgW9YOcoii8aX-CBwU-----"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    print("heheehe")
    logger.info(f"Received /start from {message.from_user.id}")
    await message.reply("Hello!")

logger.info("Starting bot...")
app.run()
