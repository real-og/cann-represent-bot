from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts

choose_lan_kb = ReplyKeyboardMarkup([[texts.en_btn, texts.ru_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

menu_kb = ReplyKeyboardMarkup([[texts.text_btn, texts.video_btn],
                               [texts.support_btn, texts.media_btn],
                               [texts.change_lan_btn]],
                                     resize_keyboard=True,)

texts_kb = InlineKeyboardMarkup(row_width=1)
texts_kb.add(InlineKeyboardButton(texts.text1, callback_data='1'))
texts_kb.add(InlineKeyboardButton(texts.text2, callback_data='2'))
texts_kb.add(InlineKeyboardButton(texts.text3, callback_data='3'))
texts_kb.add(InlineKeyboardButton(texts.text4, callback_data='4'))
texts_kb.add(InlineKeyboardButton(texts.text5, callback_data='5'))

videos_kb = InlineKeyboardMarkup(row_width=1)
videos_kb.add(InlineKeyboardButton(texts.video1, callback_data='1'))
videos_kb.add(InlineKeyboardButton(texts.video2, callback_data='2'))
videos_kb.add(InlineKeyboardButton(texts.video3, callback_data='3'))
videos_kb.add(InlineKeyboardButton(texts.video4, callback_data='4'))

media_kb = InlineKeyboardMarkup(row_width=1)
media_kb.add(InlineKeyboardButton(texts.inst, url='https://direct.smartsender.com/contacts/m:315088998/redirect?context=ZmI6MTM2MDAxOTM5&referer=315015063&continue=https%3A%2F%2Fwww.instagram.com%2Flocaltrade.cc%2F&random=1689'))
media_kb.add(InlineKeyboardButton(texts.tg, url='https://direct.smartsender.com/contacts/m:315088998/redirect?context=ZmI6MTM2MDAxOTQy&referer=315015063&continue=https%3A%2F%2Ft.me%2Flocaltradecc&random=3423'))
media_kb.add(InlineKeyboardButton(texts.fb, url='https://direct.smartsender.com/contacts/m:315088998/redirect?context=ZmI6MTM2MDAxOTQ1&referer=315015063&continue=https%3A%2F%2Fwww.facebook.com%2Flocaltrade.cc&random=7153'))

