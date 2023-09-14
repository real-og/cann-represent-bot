from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State

@dp.message_handler(state=State.choosing_lan)
async def send_welcome(message: types.Message, state: FSMContext):
    lan = message.text
    if lan in [texts.en_btn, texts.ru_btn]:
        await state.update_data(lan=lan)
    await message.answer(texts.menu)
    await message.answer(texts.finger_down, reply_markup=kb.menu_kb)
    await State.menu.set()

    