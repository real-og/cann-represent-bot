from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('images/start_gif.mp4', 'rb') as video:
        await message.answer_video(video)
    await message.answer(texts.welcome)
    await message.answer(texts.finger_down, reply_markup=kb.choose_lan_kb)
    await State.choosing_lan.set()
    await aiotable.append_user(message.from_user.id, message.from_user.username)