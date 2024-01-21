from aiogram import types

from loader import dp
import wikipedia
wikipedia.set_lang("uz")

# Echo bot
@dp.message_handler()
async def send_Wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.reply(respond)
    except:
        await message.reply("Siz qidirgan matn haqida malumot topilmadi")
