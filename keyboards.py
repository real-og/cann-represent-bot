from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts
from loader import INST_LINK, TG_LINK, WEB_LINK

choose_lan_kb = ReplyKeyboardMarkup([[texts.en_btn, texts.ru_btn, texts.ukr_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

menu_ru_kb = ReplyKeyboardMarkup([[texts.text_ru_btn, texts.video_ru_btn],
                               [texts.support_ru_btn, texts.media_ru_btn],
                               [texts.change_lan_btn]],
                                     resize_keyboard=True,)

menu_en_kb = ReplyKeyboardMarkup([[texts.text_en_btn, texts.video_en_btn],
                               [texts.support_en_btn, texts.media_en_btn],
                               [texts.change_lan_btn]],
                                     resize_keyboard=True,)

menu_ukr_kb = ReplyKeyboardMarkup([[texts.text_ukr_btn, texts.video_ukr_btn],
                               [texts.support_ukr_btn, texts.media_ukr_btn],
                               [texts.change_lan_btn]],
                                     resize_keyboard=True,)

#ru
texts_ru_kb = InlineKeyboardMarkup(row_width=1)
# texts_ru_kb.add(InlineKeyboardButton(texts.text1_ru, callback_data='text_ru_1'))
texts_ru_kb.add(InlineKeyboardButton(texts.text2_ru, callback_data='text_ru_2'))
texts_ru_kb.add(InlineKeyboardButton(texts.text3_ru, callback_data='text_ru_3'))
texts_ru_kb.add(InlineKeyboardButton(texts.text4_ru, callback_data='text_ru_4'))
texts_ru_kb.add(InlineKeyboardButton(texts.text5_ru, callback_data='text_ru_5'))

#en
texts_en_kb = InlineKeyboardMarkup(row_width=1)
# texts_en_kb.add(InlineKeyboardButton(texts.text1_en, callback_data='text_en_1'))
texts_en_kb.add(InlineKeyboardButton(texts.text2_en, callback_data='text_en_2'))
texts_en_kb.add(InlineKeyboardButton(texts.text3_en, callback_data='text_en_3'))
texts_en_kb.add(InlineKeyboardButton(texts.text4_en, callback_data='text_en_4'))
texts_en_kb.add(InlineKeyboardButton(texts.text5_en, callback_data='text_en_5'))

#ukr
texts_ukr_kb = InlineKeyboardMarkup(row_width=1)
# texts_ukr_kb.add(InlineKeyboardButton(texts.text1_ukr, callback_data='text_ukr_1'))
texts_ukr_kb.add(InlineKeyboardButton(texts.text2_ukr, callback_data='text_ukr_2'))
texts_ukr_kb.add(InlineKeyboardButton(texts.text3_ukr, callback_data='text_ukr_3'))
texts_ukr_kb.add(InlineKeyboardButton(texts.text4_ukr, callback_data='text_ukr_4'))
texts_ukr_kb.add(InlineKeyboardButton(texts.text5_ukr, callback_data='text_ukr_5'))


#ru
videos_ru_kb = InlineKeyboardMarkup(row_width=1)
videos_ru_kb.add(InlineKeyboardButton(texts.video1_ru, callback_data='video_ru_1'))
videos_ru_kb.add(InlineKeyboardButton(texts.video2_ru, callback_data='video_ru_2'))
videos_ru_kb.add(InlineKeyboardButton(texts.video3_ru, callback_data='video_ru_3'))
videos_ru_kb.add(InlineKeyboardButton(texts.video4_ru, callback_data='video_ru_4'))

#en
videos_en_kb = InlineKeyboardMarkup(row_width=1)
videos_en_kb.add(InlineKeyboardButton(texts.video1_en, callback_data='video_en_1'))
videos_en_kb.add(InlineKeyboardButton(texts.video2_en, callback_data='video_en_2'))
videos_en_kb.add(InlineKeyboardButton(texts.video3_en, callback_data='video_en_3'))

#ukr
videos_ukr_kb = InlineKeyboardMarkup(row_width=1)
videos_ukr_kb.add(InlineKeyboardButton(texts.video1_ukr, callback_data='video_ukr_1'))
videos_ukr_kb.add(InlineKeyboardButton(texts.video2_ukr, callback_data='video_ukr_2'))
videos_ukr_kb.add(InlineKeyboardButton(texts.video3_ukr, callback_data='video_ukr_3'))
videos_ukr_kb.add(InlineKeyboardButton(texts.video4_ukr, callback_data='video_ukr_4'))


media_kb = InlineKeyboardMarkup(row_width=1)
media_kb.add(InlineKeyboardButton(texts.inst_btn, url=INST_LINK))
media_kb.add(InlineKeyboardButton(texts.tg_btn, url=TG_LINK))
media_kb.add(InlineKeyboardButton(texts.web_btn, url=WEB_LINK))

