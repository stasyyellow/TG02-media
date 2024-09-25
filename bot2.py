from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from googletrans import Translator
import os
from config import TOKEN

API_TOKEN = TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
translator = Translator()

# Команда /start
@dp.message(Command('start'))
async def send_welcome(message: Message):
    await message.answer("Привет! Я бот, который умеет:\n"
                         "1. Сохранять все фото, которые ты отправляешь.\n"
                         "2. Отправлять голосовые сообщения по команде /send_voice.\n"
                         "3. Переводить текст на английский язык.\n"
                         "Для помощи введи /help.")

# Команда /help
@dp.message(Command('help'))
async def send_help(message: Message):
    await message.answer("Вот что я могу делать:\n"
                         "1. Сохранять все отправленные фото в папку 'img'.\n"
                         "2. Отправить голосовое сообщение по команде /send_voice.\n"
                         "3. Переводить любой текст, который ты мне отправляешь, на английский язык.\n"
                         "Для запуска команд введи:\n"
                         "/send_voice - отправить голосовое сообщение.\n"
                         "/start - начать работу с ботом.\n"
                         "/help - получить эту справку.")

# Хэндлер для сохранения всех фото, отправленных пользователем
@dp.message(F.photo)
async def handle_photos(message: Message):
    if not os.path.exists('img'):
        os.makedirs('img')

    photo_id = message.photo[-1].file_id  # Получение ID наибольшего изображения
    photo = await bot.get_file(photo_id)
    photo_path = photo.file_path

    file_name = f"img/{photo_id}.jpg"

    await bot.download_file(photo_path, file_name)
    await message.answer("Фото сохранено!")


# Хэндлер для отправки голосового сообщения
@dp.message(Command('send_voice'))
async def send_voice(message: Message):
    ogg_path = 'voice.ogg'  # Путь к существующему OGG файлу

    # Проверяем, существует ли файл перед отправкой
    if os.path.exists(ogg_path):
        voice = FSInputFile(ogg_path)  # Используем FSInputFile для отправки
        await message.answer_voice(voice)  # Отправляем голосовое сообщение
        await message.answer("Голосовое сообщение отправлено!")
    else:
        await message.answer("Файл голосового сообщения не найден.")

# Хэндлер для перевода текста на английский язык
@dp.message(F.text)
async def translate_text(message: Message):
    text = message.text
    translation = translator.translate(text, dest='en')
    await message.answer(f"Перевод: {translation.text}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())






# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message
# from aiogram.filters import Command
# from googletrans import Translator
# import os
# from config import TOKEN
#
# API_TOKEN = TOKEN
#
# # Инициализация бота и диспетчера
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
# translator = Translator()
#
# # Команда /start
# @dp.message(Command('start'))
# async def send_welcome(message: Message):
#     await message.answer("Привет! Я бот, который умеет:\n"
#                          "1. Сохранять все фото, которые ты отправляешь.\n"
#                          "2. Отправлять голосовые сообщения по команде /send_voice.\n"
#                          "3. Переводить текст на английский язык.\n"
#                          "Для помощи введи /help.")
#
# # Команда /help
# @dp.message(Command('help'))
# async def send_help(message: Message):
#     await message.answer("Вот что я могу делать:\n"
#                          "1. Сохранять все отправленные фото в папку 'img'.\n"
#                          "2. Отправить голосовое сообщение по команде /send_voice.\n"
#                          "3. Переводить любой текст, который ты мне отправляешь, на английский язык.\n"
#                          "Для запуска команд введи:\n"
#                          "/send_voice - отправить голосовое сообщение.\n"
#                          "/start - начать работу с ботом.\n"
#                          "/help - получить эту справку.")
#
# # Хэндлер для сохранения всех фото, отправленных пользователем
# @dp.message(F.photo)
# async def handle_photos(message: Message):
#     if not os.path.exists('img'):
#         os.makedirs('img')
#
#     photo_id = message.photo[-1].file_id  # Получение ID наибольшего изображения
#     photo = await bot.get_file(photo_id)
#     photo_path = photo.file_path
#
#     file_name = f"img/{photo_id}.jpg"
#
#     await bot.download_file(photo_path, file_name)
#     await message.answer("Фото сохранено!")
#
# # Хэндлер для отправки голосового сообщения
# @dp.message(Command('send_voice'))
# async def send_voice(message: Message):
#     ogg_path = 'audio/voice.ogg'  # Путь к существующему OGG файлу
#
#     # Отправка ogg файла
#     with open(ogg_path, 'rb') as voice:
#         await bot.send_voice(message.chat.id, voice)
#     await message.answer("Голосовое сообщение отправлено!")
#
# # Хэндлер для перевода текста на английский язык
# @dp.message(F.text)
# async def translate_text(message: Message):
#     text = message.text
#     translation = translator.translate(text, dest='en')
#     await message.answer(f"Перевод: {translation.text}")
#
# # Запуск бота
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())




# without start and help
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message, ContentType
# from aiogram.filters import Command
# from googletrans import Translator
# import os
# from config import TOKEN
# from pydub import AudioSegment
#
# API_TOKEN = TOKEN
#
# # Инициализация бота и диспетчера
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
# translator = Translator()
#
#
# # Хэндлер для сохранения всех фото, отправленных пользователем
# @dp.message(F.photo)
# async def handle_photos(message: Message):
#     if not os.path.exists('img'):
#         os.makedirs('img')
#
#     photo_id = message.photo[-1].file_id  # Получение ID наибольшего изображения
#     photo = await bot.get_file(photo_id)
#     photo_path = photo.file_path
#
#     file_name = f"img/{photo_id}.jpg"
#
#     await bot.download_file(photo_path, file_name)
#     await message.answer("Фото сохранено!")
#
#
# # Хэндлер для отправки голосового сообщения
# def convert_mp3_to_ogg(mp3_path, ogg_path):
#     audio = AudioSegment.from_mp3(mp3_path)
#     audio.export(ogg_path, format="ogg")
#
# @dp.message(Command('send_voice'))
# async def send_voice(message: Message):
#     mp3_path = 'audio.mp3'
#     ogg_path = 'audio.ogg'
#
#     # Конвертация mp3 в ogg
#     convert_mp3_to_ogg(mp3_path, ogg_path)
#
#     # Отправка ogg файла
#     with open(ogg_path, 'rb') as voice:
#         await bot.send_voice(message.chat.id, voice)
#     await message.answer("Голосовое сообщение отправлено!")
#
#
#
# # Хэндлер для перевода текста на английский язык
# @dp.message(F.text)
# async def translate_text(message: Message):
#     text = message.text
#     translation = translator.translate(text, dest='en')
#     await message.answer(f"Перевод: {translation.text}")
#
#
# # Запуск бота
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     import asyncio
#
#     asyncio.run(main())
