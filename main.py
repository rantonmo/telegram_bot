# Telegram bot for regadero project
from machine import Pin
from json import loads as json_loads
from time import sleep as t_sleep


from wifi_manager import configure_wifi
from gpio_manager_small import blink
from logger import Logger
from telegram_bot import TelegramBot


from utils import datetime



logger = Logger()
logger.info("reading settings")
SETTINGS = json_loads(open('settings.json', 'r').read())

led = Pin(2, Pin.OUT, value=1)
blink(led)

wlan = configure_wifi(SETTINGS['wifi'])

bot = TelegramBot(
    SETTINGS['telegram']['token'],
    SETTINGS['telegram']['chat_id'])