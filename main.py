import logging
from aiogram import Bot, Dispatcher, executor, types
from pictotext import picture_to_text

API_TOKEN = '5133118252:AAG428qfRCaZYKqc0QlUcYqqfC1pMfZElIM'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Привет! Я бот, с помощью которого можно чекиниться в аудиториях Вышки! Чтобы зачекиниться, пришли мне фотографию номера аудитории")

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    """
    This handler will be called when user sends picture to the bot
    """
    path_to_pic = f'C:/Users/User/Desktop/.py/bot/pics/{message.from_user.id}.jpg'
    await message.photo[-1].download(destination_file = path_to_pic)
    text_from_pic = picture_to_text(path_to_pic) 
    if text_from_pic: 
        reply_message = 'Поздравляю! Ты зачекинился в аудитории '
    else: 
        reply_message = 'Фотография должна содержать номер аудитории, попробуй ещё раз'
    await message.reply(reply_message + text_from_pic)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
