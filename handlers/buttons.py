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
    if input == texts.text_btn:
        with open('images/text_uk.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.texts_kb)
    elif input == texts.support_btn:
        with open('images/Сапорт.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.support_link)
    elif input == texts.video_btn:
        with open('images/Видео.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.videos_kb)
    elif input == texts.media_btn:
        with open('images/соцсети.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.media_kb)
    elif input == texts.change_lan_btn:
        await message.answer(texts.finger_down, reply_markup=kb.choose_lan_kb)
        await State.choosing_lan.set()

    elif input == texts.text_en_btn:
        with open('images/text.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.texts_en_kb)
    elif input == texts.support_en_btn:
        with open('images/support.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.support_link)
    elif input == texts.video_en_btn:
        with open('images/video.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.videos_en_kb)
    elif input == texts.media_en_btn:
        with open('images/social.jpg', 'rb') as photo:
            await message.answer_photo(photo, reply_markup=kb.media_kb)
