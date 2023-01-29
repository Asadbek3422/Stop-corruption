import logging
from aiogram import Bot, Dispatcher, executor, types
from buttons import *

API_TOKEN = '6006613364:AAHhbx7biiacYRMBEB4W5zrN-bs10OZysX0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum, ushbu bot orqali siz ish topish uchun imtihon topshirishingiz mumkin",
                        reply_markup=main_menu)


@dp.callback_query_handler(text="3")
async def func(query: types.CallbackQuery):
    await query.message.answer("Bosh menu", reply_markup=main_menu)


@dp.message_handler()
async def func(message: types.Message):
    try:
        mes_text = message.text
        if mes_text == "Bosh menu":
            await message.answer("Bosh menu", reply_markup=main_menu)

        elif mes_text == "🪪 Vakansiyalar":
            await message.answer("Sohani tanlang", reply_markup=sohalar_menu)

        elif mes_text == "⏳ Imtihon topshirish":
            await message.answer("Imtihon topshirishdan avval ushbu maqolani to'liq o'qib chiqing:\n"
                                 "https://telegra.ph/Imtihon-haqida-01-29")
            await message.answer("Sohangizni tanlang:", reply_markup=sohalar_menu)

        elif mes_text == "Ta'lim":
            await message.answer("O'quv muassasini tanlang:", reply_markup=muassasa_menu)

        elif mes_text == "Maktablar":
            await message.answer("Hududni tanlang", reply_markup=hududlar_menu)

        elif mes_text == "Toshkent":
            await message.answer("Ushbu hududda 17 ta vakansiya mavjud. Batafsil: https://vacancy.argos.uz/")

        elif mes_text == "Tibbiyot":
            await message.answer("Tibbiyotdagi yo'nalishingizni tanlang:", reply_markup=tibbiyot_menu)

        elif mes_text == "Xirurgiya":
            await message.answer("Tayyor bo'lsangiz, Boshlash tugmasini bosing", reply_markup=boshlash_tugmasi)

        elif mes_text == "Boshlash":
            await message.answer(
                "1-savol: Boʻgʻimning bukilmaydigan va yozil-maydigan boʻlib, qimirlamay qotib qolishi nima deyiladi? (ankiloz)", reply_markup=remove_k)

        elif mes_text.lower() == "ankiloz":
            await message.answer("2-savol: Plevra boʻshligiga qon yigʻilishi nima deyiladi? (gemotoraks)")

        elif mes_text.lower() == "gemotoraks":
            await message.answer(
                "3-savol: Davolash va kasallikni aniqlash maqsadida tirik odamning toʻqima yoki biror aʼzosidan bir qismini kesib olib tekshirish nima deyiladi? (biopsiya)")

        elif mes_text.lower() == "biopsiya":
            await message.answer("Siz 100% to'g'ri javob berdingiz.")
            await message.answer("Siz quyidagi joylarga ishga kirishingiz mumkin!", reply_markup=ishxona_menu)

        elif mes_text == "📝 Taklif va shikoyatlar":
            await message.answer("Taklif va shikoyatingizni yozib qoldiring", reply_markup=main_menu)
        else:
            await message.answer("Uzr, xato buyruq kiritdingiz!")

    except:
        await message.answer("Uzr, xatolik yuz berdi, qaytadan /start ni bosing")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
