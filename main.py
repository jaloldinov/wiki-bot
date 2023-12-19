
import logging
import  wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6834692423:AAE9X6UAxg_rMUXVITQFj6uy8qem8-ho4YA'

wikipedia.set_lang('uz')
# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply("Hi!\nI'm Wikipedia!\nPowered by Omadbek.")




@dp.message_handler()


async def sendWiki(message: types.Message):

    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
       await message.answer("Uzr, bu mavzu haqida ma'lumot topa olmadim (:")



if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=False)