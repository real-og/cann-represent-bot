from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State

@dp.message_handler(state=State.choosing_lan)
async def send_welcome(message: types.Message, state: FSMContext):
    lang = message.text
    if lang in [texts.en_btn, texts.ru_btn, texts.ukr_btn]:
        await state.update_data(lang=lang)
        if lang == texts.en_btn:
            await message.answer(texts.menu_en)
            await message.answer(texts.finger_down, reply_markup=kb.menu_en_kb)
        elif lang == texts.ru_btn:
            await message.answer(texts.menu_ru)
            await message.answer(texts.finger_down, reply_markup=kb.menu_ru_kb)
        elif lang == texts.ukr_btn:
            await message.answer(texts.menu_ukr)
            await message.answer(texts.finger_down, reply_markup=kb.menu_ukr_kb)

        await State.menu.set()
    else:
        await message.answer(texts.welcome)
        await message.answer(texts.finger_down, reply_markup=kb.choose_lan_kb)