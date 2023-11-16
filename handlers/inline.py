from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State

@dp.callback_query_handler(state='*')
async def send_channels(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('lang')
    if lang == texts.en_btn:
        await callback.message.answer(texts.developing_eng)
    else:
        await callback.message.answer(texts.developing_ru)
    await callback.answer()