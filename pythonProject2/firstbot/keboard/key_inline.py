from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Про крипов',
                                      url='https://dota2.fandom.com/wiki/Creeps')
    keyboard_inline.add(but_inline)
    return keyboard_inline


def get_keyboard_inline2():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline2 = InlineKeyboardButton('Про героев', url='https://dota2.fandom.com/wiki/Heroes')
    keyboard_inline.add(but_inline2)
    return keyboard_inline


def get_keyboard_inline3():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline3 = InlineKeyboardButton('Про предметы',
                                       url='https://dota2.fandom.com/wiki/Items')
    but_inline4 = InlineKeyboardButton('Про нейтральные предметы',
                                       url='https://dota2.fandom.com/wiki/Neutral_Items')
    keyboard_inline.add(but_inline3, but_inline4)
    return keyboard_inline
