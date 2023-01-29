from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🪪 Vakansiyalar"),
            KeyboardButton(text="⏳ Imtihon topshirish")
        ],
        [
            KeyboardButton(text="📝 Taklif va shikoyatlar")
        ],
    ],
    resize_keyboard=True
)

sohalar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tibbiyot"),
            KeyboardButton(text="Qurilish")
        ],
        [
            KeyboardButton(text="Ta'lim"),
            KeyboardButton(text="Huquq")
        ],
        [
            KeyboardButton(text="Moliya"),
            KeyboardButton(text="Iqtisodiyot")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)

muassasa_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oliy ta'lim"),
            KeyboardButton(text="O'rta maxsus ta'limi")
        ],
        [
            KeyboardButton(text="Maktablar"),
            KeyboardButton(text="Maktabgacha ta'lim")
        ]
    ],
    resize_keyboard=True
)

hududlar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Andijon"),
            KeyboardButton(text="Namangan")
        ],
        [
            KeyboardButton(text="Farg'ona"),
            KeyboardButton(text="Sirdaryo"),
            KeyboardButton(text="Jizzax")
        ],
        [
            KeyboardButton(text="Samarqand"),
            KeyboardButton(text="Qashqadaryo"),
            KeyboardButton(text="Surxondaryo")
        ],
        [
            KeyboardButton(text="Buxoro"),
            KeyboardButton(text="Xorazm"),
            KeyboardButton(text="Navoiy")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)
tibbiyot_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Xirurgiya"),
            KeyboardButton(text="Stomatologiya")
        ],
        [
            KeyboardButton(text="Pediatriya"),
            KeyboardButton(text="Nevrologiya")
        ],
        [
            KeyboardButton(text="Travmatalogiya"),
            KeyboardButton(text="Kardiologiya")
        ],
        [
            KeyboardButton(text="Dermatologiya"),
            KeyboardButton(text="Ginekologiya")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)

ishxona_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="7-shaxar shifoxonasi", callback_data="1"),
            InlineKeyboardButton(text="9-shaxar shifoxonasi", callback_data="2")
        ],
        [
            InlineKeyboardButton(text="Bosh menu", callback_data="3")
        ]
    ]
)

boshlash_tugmasi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Boshlash")
        ]
    ],
    resize_keyboard=True
)

remove_k = ReplyKeyboardRemove()