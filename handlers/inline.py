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
    
    if callback.data == 'text_ru_2':
        with open('files/text_presentation_ru.pdf', 'rb') as file:
            await callback.message.answer_document(file)
    elif callback.data == 'text_en_2':
        with open('files/text_presentation_en.pdf', 'rb') as file:
            await callback.message.answer_document(file)
    elif callback.data == 'text_ukr_2':
        with open('files/text_presentation_ukr.pdf', 'rb') as file:
            await callback.message.answer_document(file)
    else:
        if lang == texts.en_btn:
            await callback.message.answer(texts.developing_en)
        elif lang == texts.ru_btn:
            await callback.message.answer(texts.developing_ru)
        elif lang == texts.ukr_btn:
            await callback.message.answer(texts.developing_ukr)
    await callback.answer()