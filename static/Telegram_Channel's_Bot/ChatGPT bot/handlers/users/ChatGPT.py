from aiogram import types
from aiogram.types import ParseMode
from loader import dp,bot
from utils.ChatGpt import get_answer
from aiogram import bot
from data.config import CHANNELS
@dp.message_handler()
@dp.message_handler()
async def on_message(message: types.Message):
    response = get_answer(message.text)

    # Send the response back to the user
    await message.answer(response,parse_mode=ParseMode.MARKDOWN)

# Rest of your code
