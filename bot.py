import logging
from aiogram import *
TOKEN = "6033481726:AAG3B4rVVqEnJd0f8Ri6yb3rVLv-_qf6rBU"

logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_message(message: types.message):
    await bot.send_message(message.from_user.id,message.text)

if __name__ == '__main__':
    executor.start_polling(dp)
