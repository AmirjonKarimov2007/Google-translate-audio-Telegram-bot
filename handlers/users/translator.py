import requests
from aiogram.types import InputFile
from aiogram.utils import executor
from aiogram import types
from loader import dp,bot,db
from io import BytesIO
async def get_translation(word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(api_url)
    data = response.json()
    return data

@dp.message_handler()
async def translate(message: types.Message):
    word = message.text.lower()
    translation_data = await get_translation(word)

    if not translation_data:
        await message.reply("Sorry, I couldn't find a translation for that word.")
        return

    # Check if '0' key and 'meanings' key exist in the response
    if not isinstance(translation_data, list) or not translation_data:
        await message.reply("Sorry, no meanings found for the word.")
        return

    word_info = translation_data[0]
    meanings = word_info.get("meanings", [])

    if not meanings:
        await message.reply("Sorry, no meanings found for the word.")
        return

    translation_text = f"<b>Translation for '{word}':</b>\n"

    for meaning in meanings:
        part_of_speech = meaning.get("partOfSpeech", "N/A")
        definitions = meaning.get("definitions", [])

        for definition in definitions:
            text = definition.get("definition", "N/A")
            translation_text += f"  👉<i>{part_of_speech.capitalize()}:</i> {text}\n"

    await message.reply(translation_text, parse_mode="HTML")

    phonetics = word_info.get("phonetics", [])

    for phonetic in phonetics:
        audio_url = phonetic.get("audio", "")
        if audio_url:
            # Download the audio file
            audio_response = requests.get(audio_url)
            if audio_response.status_code == 200:
                audio_content = BytesIO(audio_response.content)
                await message.reply_audio(InputFile(audio_content, filename="pronunciation.mp3"))