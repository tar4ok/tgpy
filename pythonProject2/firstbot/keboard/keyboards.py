from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def get_keyboard_1():
    keyboard1 = InlineKeyboardMarkup(row_width= 1)
    button1 = InlineKeyboardButton('Показать бибизянку', callback_data= 'go_to_1')
    button2 = InlineKeyboardButton('Показать капибару', callback_data= 'go_to_2')
    button3 = InlineKeyboardButton('Показать мини мышь', callback_data= 'go_to_3')
    keyboard1.add(button1, button2, button3)
    return keyboard1

def get_keyboard_2():
    keyboard2 = InlineKeyboardMarkup(row_width= 1)
    button4 = InlineKeyboardButton('', callback_data= 'go_to_2')
    button5 = InlineKeyboardButton('', callback_data= 'go_to_3')
    button6 = InlineKeyboardButton('', callback_data= 'go_to_0')
    keyboard2.add( button4, button5, button6)
    return keyboard2
def get_keyboard_3():
    keyboard3 = InlineKeyboardMarkup(row_width= 1)
    button7 = InlineKeyboardButton('', callback_data= 'go_to_1')
    button8 = InlineKeyboardButton('', callback_data= 'go_to_3')
    button9 = InlineKeyboardButton('', callback_data= 'go_to_0')
    keyboard3.add(button7, button8, button9)
    return keyboard3
def get_keyboard_4():
    keyboard4 = InlineKeyboardMarkup(row_width= 1)
    button10 = InlineKeyboardButton('', callback_data= 'go_to_1')
    button11 = InlineKeyboardButton('', callback_data= 'go_to_2')
    button12 = InlineKeyboardButton('', callback_data= 'go_to_0')
    keyboard4.add(button10, button11, button12)
    return keyboard4