from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

from config import WEBAPP_URL
from database import add_user

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    user = message.from_user
    add_user(user.id, user.username or "", user.first_name or "")

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📚 IELTS mashqlarini boshlash",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )

    await message.answer(
        f"Salom, {user.first_name}! 👋\n\n"
        "Bu bot senga IELTS uchun ingliz tilini o'rganishda yordam beradi:\n"
        "• So'z boyligi (vocabulary)\n"
        "• Grammatika\n"
        "• Listening\n"
        "• Speaking va Writing baholash\n\n"
        "Boshlash uchun tugmani bos 👇",
        reply_markup=keyboard,
    )


@router.message()
async def fallback(message: types.Message):
    await message.answer(
        "Mashqlarni boshlash uchun /start buyrug'ini yuboring."
    )
