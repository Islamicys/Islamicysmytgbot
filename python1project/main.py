import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
import random
import sqlite3

API_TOKEN = '8775214623:AAHaDbT3OJQX40oGye4NztPnsdj3dl0eths'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usersInfo(user_id INTEGER PRIMARY KEY, name TEXT, username TEXT)""")


photo_path = r"C:\Users\user\Pictures\Roblox\RobloxScreenShot20250608_143605505.png"

"""
@dp.message(Command("photo"))
async def send_photo_command(message: Message):
    photo = FSInputFile(path=photo_path)
    await message.answer_photo(photo=photo)
"""
@dp.message(Command("start"))
async def start_addUserToDataBase(message: Message):
    await message.answer("Салам")
    cursor.execute("INSERT OR IGNORE INTO usersInfo VALUES(?,?,?)",(message.from_user.id, message.from_user.full_name,message.from_user.username))
    conn.commit()

@dp.message(Command("photo"))
async def send_photo_command(message: Message):
    photo = "https://media.istockphoto.com/id/173242750/photo/banana-bunch.jpg?s=612x612&w=0&k=20&c=MAc8AXVz5KxwWeEmh75WwH6j_HouRczBFAhulLAtRUU="
    await message.answer_photo(photo=photo)
    await message.answer_sticker(sticker="CAACAgIAAxkBAAFFOb1pvFMuaXDTGdP0j6pDAdopwLGPkAACrCQAAu-zKEr_01KC2vW5gDoE")

@dp.message(Command("randN"))
async def send_randomNumber_command(message: Message):
    rN = random.randint(0,100)
    await message.answer(f"{rN}")

@dp.message(Command("list"))
async def send_listOfCommands_command(message: Message):
    await message.answer("Вот лист команд этого бота:\n/photo\n/randN")

@dp.message(F.voice)
async def get_voice_id(message: Message):
    await message.answer(f"FILE ID: {message.voice.file_id}")

@dp.message(Command("usersInfo"))
async def send_usersInfo_command(message: Message):
    if message.from_user.username == "Icaomo":
        cursor.execute("SELECT name, username FROM usersInfo")
        users = cursor.fetchall()
        text = "users:\n"
        for name, username in users:
            text = text + f"{name}, @{username}\n"
        await message.answer(text)
    else:
        await message.answer("Недостаточно прав")

@dp.message(F.text)
async def send_voiceAnswer_command(message: Message):
    if message.text == "Привет":
        await message.answer_voice(voice="AwACAgIAAxkBAAPeabz-6iu7KZHqiwMIiNcQr45qAAEEAAKwlAACoVDpSUxo-o12lw6fOgQ")
    elif message.text == "Как дела?":
        await message.answer_voice(voice="AwACAgIAAxkBAAPpab0AAWqmZcwnoarf2ptsMC0Dtrh-AAK5pQACL8XpSU6a4TJGxpOZOgQ")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
