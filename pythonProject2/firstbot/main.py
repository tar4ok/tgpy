from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2, get_keyboard_3 , get_keyboard_4
from database.database import initialize_dp, add_user, get_user

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_dp()

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Запуск бота'),
        types.BotCommand(command='/help', description='Чем может помочь бот'),
        types.BotCommand(command='/stop', description='Остановить бота'),
        types.BotCommand(command='/link', description='Cсылка на видео'),
        types.BotCommand(command='/sigma', description='Сигма'),
        types.BotCommand(command='/motivation', description='Мотивация')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
                 message.from_user.last_name)
        await message.reply('Есть несколько вариантов картинок: ', reply_markup=get_keyboard_1())
    else:
        await message.reply('Есть несколько вариантов картинок: ', reply_markup=get_keyboard_1())


@dp.callback_query_handler(lambda c: c.data == 'go_to_0')
async def go_to_1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Есть несколько вариантов картинок: ', reply_markup=get_keyboard_1())


@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    # await callback_query.message.edit_text('бибизян', reply_markup= keyboard2)
    await bot.send_photo(callback_query.from_user.id,
                         photo='https://krots.top/uploads/posts/2022-03/1646237256_26-krot-info-p-obezyana-mem-smeshnie-foto-29.jpg',
                         caption='бибизян', reply_markup=get_keyboard_1())
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    # await callback_query.message.edit_text('капибара', reply_markup= keyboard3)
    await bot.send_photo(
        callback_query.from_user.id,
         photo='https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg',
         caption='капибара', reply_markup=get_keyboard_1())
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(lambda c: c.data == 'go_to_3')
async def go_to_3(callback_query: types.CallbackQuery):
    # await callback_query.message.edit_text('минимышь', reply_markup= keyboard4)
    await bot.send_photo(callback_query.from_user.id,
                         photo='https://ekd.me/wp-content/uploads/2015/07/7427ea21079d171fd0f903-494x338.jpeg',
                         caption='мини мышь', reply_markup=get_keyboard_1())
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе с ...')


@dp.message_handler(commands='stop')
async def stop(message: types.Message):
    await message.answer('Стопаюсь')


@dp.message_handler(commands='link')
async def link(message: types.Message):
    await message.reply('https://www.youtube.com/watch?v=Ptb9F2KHcWo&list=PL2RiRLApO2-baS2UZQcuqY4n-fEImCg3Q')


@dp.message_handler(commands='sigma')
async def photo(message: types.Message):
    await message.answer(
        'https://i.ytimg.com/vi/oTKCnr7-HDg/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgVyhIMA8=&rs=AOn4CLBfJs-qd8IkDUJFgWrasuqW-OkobQ')


@dp.message_handler(commands='motivation')
async def translator(message: types.Message):
    await message.answer('https://i.kym-cdn.com/entries/icons/original/000/043/251/cover6.jpg')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
