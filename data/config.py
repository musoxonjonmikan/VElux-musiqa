import os
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS", "").split(",")
IP = os.getenv("IP", "localhost")
