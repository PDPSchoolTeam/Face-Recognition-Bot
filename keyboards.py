from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Asosiy menyu uchun tugmalar
def main_menu():
    buttons = [
        [KeyboardButton(text="Kelgan o'quvchilar")],
        [KeyboardButton(text="Kelmagan o'quvchilar")],
        [KeyboardButton(text="Yangi o'quvchi qo'shish")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
