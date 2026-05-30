from aiogram import executor
from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import threading
from flask import Flask

# Tiny web server so it works as a Web Service
web = Flask(__name__)

@web.route('/')
def index():
    return "Bot is running!", 200

def run_web():
    web.run(host="0.0.0.0", port=8080)

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    try:
        db.create_table_channel()
        db.create_table_admins()
        db.create_table_files()
        db.create_table_users()
    except Exception as err:
        print(err)
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    # Start web server in background thread
    threading.Thread(target=run_web, daemon=True).start()
    # Start bot
    executor.start_polling(dp, on_startup=on_startup)
