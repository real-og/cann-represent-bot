from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts

choose_lan_kb = ReplyKeyboardMarkup([[texts.en_btn, texts.ru_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

menu_ru_kb = ReplyKeyboardMarkup([[texts.text_btn, texts.video_btn],
                               [texts.support_btn, texts.media_btn],
                               [texts.change_lan_btn]],
                                     resize_keyboard=True,)

menu_en_kb = ReplyKeyboardMarkup([[texts.text_en_btn, texts.video_en_btn],
                               [texts.support_en_btn, texts.media_en_btn],
                               [texts.change_lan_btn]],
                                     resize_keyboard=True,)

texts_kb = InlineKeyboardMarkup(row_width=1)
texts_kb.add(InlineKeyboardButton(texts.text1, callback_data='1'))
texts_kb.add(InlineKeyboardButton(texts.text2, callback_data='2'))
texts_kb.add(InlineKeyboardButton(texts.text3, callback_data='3'))
texts_kb.add(InlineKeyboardButton(texts.text4, callback_data='4'))
texts_kb.add(InlineKeyboardButton(texts.text5, callback_data='5'))

texts_en_kb = InlineKeyboardMarkup(row_width=1)
texts_en_kb.add(InlineKeyboardButton(texts.text1_en, callback_data='11'))
texts_en_kb.add(InlineKeyboardButton(texts.text2_en, callback_data='22'))
texts_en_kb.add(InlineKeyboardButton(texts.text3_en, callback_data='33'))
texts_en_kb.add(InlineKeyboardButton(texts.text4_en, callback_data='44'))
texts_en_kb.add(InlineKeyboardButton(texts.text5_en, callback_data='55'))


videos_kb = InlineKeyboardMarkup(row_width=1)
videos_kb.add(InlineKeyboardButton(texts.video1, callback_data='1'))
videos_kb.add(InlineKeyboardButton(texts.video2, callback_data='2'))
videos_kb.add(InlineKeyboardButton(texts.video3, callback_data='3'))
videos_kb.add(InlineKeyboardButton(texts.video4, callback_data='4'))

videos_en_kb = InlineKeyboardMarkup(row_width=1)
videos_en_kb.add(InlineKeyboardButton(texts.video1_en, callback_data='11'))
videos_en_kb.add(InlineKeyboardButton(texts.video2_en, callback_data='22'))
videos_en_kb.add(InlineKeyboardButton(texts.video3_en, callback_data='33'))



media_kb = InlineKeyboardMarkup(row_width=1)
media_kb.add(InlineKeyboardButton(texts.inst, url='https://instagram.com/cannabetrust'))
media_kb.add(InlineKeyboardButton(texts.tg, url='https://t.me/CannabeChat'))
media_kb.add(InlineKeyboardButton(texts.web, url='https://cannabetrust.com'))

