import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
STRIPE_LINK = "https://buy.stripe.com/6oU00kcjvbC03o00Z21B60g"
PAID_USERS = set()

WELCOME_TEXT = """🌌 Добро пожаловать в экосистему 4Dverse

Мы создаём новую реальность на стыке искусства, технологий, моды и сознания.

Вы — настоящий человек нового времени и строитель новой реальности.

Мы бесконечно рады вам и сердечно благодарим за ваш импульс соединиться и включиться в новые программы вместе с нами 🙏

Выберите, куда хотите направить своё внимание:"""

ACTIVATION_TEXT = """⚡️ АКТИВАЦИЯ ЭНЕРГОСИСТЕМЫ

Это ваша бесплатная практика — входная точка в мир 4Dverse.

Получайте ваш пак практики:"""

BREATHCODE_TEXT = """🌬 BREATHCODE — программный код вашего дыхания

Полный курс включает 4 вида дыхания. Каждый пак содержит:
📹 Видео практика
🎵 Аудио сопровождение
🖼 Визуальная схема дыхания
📝 Текст введение

💫 Одна инвестиция — доступ навсегда

Стоимость: 33€"""

ABOUT_TEXT = """🌐 О ЭКОСИСТЕМЕ 4DVERSE

4Dverse — экосистема на стыке искусства, технологий, моды и сознания.

BREATHCODE — система осознанного дыхания, которая активирует ваш внутренний код.

📱 Instagram: @4dverse.io"""

PAID_WELCOME = """✨ Добро пожаловать в BREATHCODE!

Ваш доступ активирован. Выберите практику:"""

NOT_PAID_TEXT = """🔒 Этот раздел доступен после оплаты."""

def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⚡️ Активация энергосистемы (бесплатно)", callback_data="activation")],
        [InlineKeyboardButton("🌬 BREATHCODE — купить", callback_data="breathcode")],
        [InlineKeyboardButton("🌐 О экосистеме 4Dverse", callback_data="about")],
    ])

def breathcode_keyboard(user_id):
    if user_id in PAID_USERS:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("🌬 Дыхание 1", callback_data="breath_1")],
            [InlineKeyboardButton("🌬 Дыхание 2", callback_data="breath_2")],
            [InlineKeyboardButton("🌬 Дыхание 3", callback_data="breath_3")],
            [InlineKeyboardButton("🌬 Дыхание 4", callback_data="breath_4")],
            [InlineKeyboardButton("◀️ Назад", callback_data="back")],
        ])
    else:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("💳 Оплатить 33€", url=STRIPE_LINK)],
            [InlineKeyboardButton("✅ Я оплатил(а)", callback_data="check_payment")],
            [InlineKeyboardButton("◀️ Назад", callback_data="back")],
        ])

def back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("◀️ В главное меню", callback_data="back")],
    ])

def breath_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("◀️ К практикам", callback_data="breathcode_paid")],
        [InlineKeyboardButton("🏠 Главное меню", callback_data="back")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, reply_markup=main_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "back":
        await query.edit_message_text(WELCOME_TEXT, reply_markup=main_keyboard())

    elif data == "activation":
        await query.edit_message_text(ACTIVATION_TEXT, reply_markup=back_keyboard())
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="📹 Видео — скоро здесь\n🎵 Аудио — скоро здесь\n🖼 Схема — скоро здесь\n📝 Введение — скоро здесь"
        )

    elif data == "breathcode":
        if user_id in PAID_
