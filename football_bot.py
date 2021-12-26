from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from main import TodayMatches, matches_list
from aiogram.utils.markdown import hbold, hlink
import time

bot = Bot(token="token", parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    button = 'Matches'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)

    await message.answer('Show matches?', reply_markup=keyboard)


@dp.message_handler(Text(equals="Matches"))
async def get_matches(message: types.Message):
    await message.answer('Loading...')
    TodayMatches()
    for index, item in enumerate(matches_list):
        card = f'{hlink(item.get("Match"), item.get("Url"))}\n' \
               f'{hbold("Date: ")}{item.get("Date")}\n' \
               f'{hbold("Time: ")}{item.get("Time")}\n' \
               f'{hbold("Score: ")}{item.get("Score")}\n'
        if index % 20 == 0:
            time.sleep(3)
        await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
