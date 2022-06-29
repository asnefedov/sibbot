from aiogram import types, Dispatcher


async def bot_echo(message: types.Message):
    await message.answer(f'Вы написали: {message.text}')


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
