from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State

@dp.message_handler(state=State.menu)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('lang')

    input = message.text

    if input == texts.text_ru_btn:
        with open('images/text_ru.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.texts_ru_kb)
    elif input == texts.support_ru_btn:
        with open('images/support_ru.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.support_link)
    elif input == texts.video_ru_btn:
        with open('images/video_ru.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.videos_ru_kb)
    elif input == texts.media_ru_btn:
        with open('images/media_ru.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.media_kb)

    elif input == texts.text_en_btn:
        with open('images/text_en.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.texts_en_kb)
    elif input == texts.support_en_btn:
        with open('images/support_en.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.support_link)
    elif input == texts.video_en_btn:
        with open('images/video_en.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.videos_en_kb)
    elif input == texts.media_en_btn:
        with open('images/media_en.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.media_kb)

    elif input == texts.text_ukr_btn:
        with open('images/text_ukr.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.texts_ukr_kb)
    elif input == texts.support_ukr_btn:
        with open('images/support_ukr.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.support_link)
    elif input == texts.video_ukr_btn:
        with open('images/video_ukr.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.videos_ukr_kb)
    elif input == texts.media_ukr_btn:
        with open('images/media_ukr.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.media_kb)

    elif input == texts.change_lan_btn:
        await message.answer(texts.finger_down, reply_markup=kb.choose_lan_kb)
        await State.choosing_lan.set()
