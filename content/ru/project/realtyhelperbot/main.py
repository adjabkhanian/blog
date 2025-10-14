import asyncio
import logging
import json
from datetime import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    FSInputFile,
)
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.exceptions import TelegramBadRequest

from config import BOT_TOKEN, ADMIN_IDS
from utils.google_api import get_cities as get_cities_sync, add_request as add_request_sync

logging.basicConfig(level=logging.INFO)

# ----------------- Асинхронные обёртки -----------------
async def get_cities():
    return await asyncio.to_thread(get_cities_sync)

async def add_request(data):
    await asyncio.to_thread(add_request_sync, data)

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

WELCOME_FILE = "welcome.json"

# ----------------- FSM States -----------------
class Form(StatesGroup):
    city = State()
    other_city = State()
    property_type = State()
    budget = State()
    mortgage = State()
    contact = State()

class WelcomeEdit(StatesGroup):
    waiting_for_photo = State()
    waiting_for_text = State()

# ----------------- Загрузка приветствия -----------------
def load_welcome():
    try:
        with open(WELCOME_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"text": None, "photo": None}

def save_welcome(data):
    with open(WELCOME_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ----------------- /start -----------------
@dp.message(CommandStart())
async def start(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Начать работу")]],
        resize_keyboard=True
    )

    welcome = load_welcome()
    photo = welcome.get("photo")
    caption = welcome.get("text") or (
        "👋 Добро пожаловать!\n\n"
        "Здесь вы найдёте лучшие предложения от застройщиков — квартиры со скидками до **20%**, "
        "о которых знают только мы.\n\n"
        "🏠 Покупая квартиру с нами, вы получаете не только выгодную цену, "
        "но и **ценный подарок при покупке**!\n\n"
        "👇 Чтобы начать подбор, нажмите кнопку «Начать работу» ниже."
    )

    if photo:
        try:
            await message.answer_photo(photo, caption=caption, reply_markup=kb)
        except TelegramBadRequest:
            # если file_id устарел — просто текстом
            await message.answer(caption, reply_markup=kb)
    else:
        await message.answer(caption, reply_markup=kb)

# ----------------- Команда /set_welcome -----------------
@dp.message(Command("set_welcome"))
async def set_welcome_start(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_IDS:
        return await message.answer("⛔ У вас нет прав для этой команды.")
    await message.answer("Отправьте новое фото приветствия или напишите «Пропустить».")
    await state.set_state(WelcomeEdit.waiting_for_photo)

@dp.message(WelcomeEdit.waiting_for_photo)
async def set_welcome_photo(message: Message, state: FSMContext):
    if message.text and message.text.lower() == "пропустить":
        await state.update_data(photo=None)
    elif message.photo:
        await state.update_data(photo=message.photo[-1].file_id)
    else:
        return await message.answer("Пожалуйста, отправьте фото или напишите «Пропустить».")
    await message.answer("Теперь отправьте текст приветствия:")
    await state.set_state(WelcomeEdit.waiting_for_text)

@dp.message(WelcomeEdit.waiting_for_text)
async def set_welcome_text(message: Message, state: FSMContext):
    data = await state.get_data()
    photo = data.get("photo")
    text = message.text.strip()

    save_welcome({"text": text, "photo": photo})

    await message.answer("✅ Приветствие успешно обновлено!")
    await state.clear()

# ----------------- Начало работы -----------------
@dp.message(F.text == "Начать работу")
async def choose_city(message: Message, state: FSMContext):
    cities = await get_cities()
    buttons = [KeyboardButton(text=city) for city in cities]
    buttons.append(KeyboardButton(text="Другой город"))
    kb = ReplyKeyboardMarkup(
        keyboard=[buttons[i:i + 2] for i in range(0, len(buttons), 2)],
        resize_keyboard=True
    )
    await message.answer("🏙 Выберите город:", reply_markup=kb)
    await state.set_state(Form.city)

# ----------------- Выбор города -----------------
@dp.message(Form.city)
async def process_city(message: Message, state: FSMContext):
    if message.text == "Другой город":
        await message.answer("Введите ваш город вручную:", reply_markup=None)
        await state.set_state(Form.other_city)
        return

    await state.update_data(city=message.text)
    await ask_property_type(message, state)

@dp.message(Form.other_city)
async def process_other_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await ask_property_type(message, state)

async def ask_property_type(message: Message, state: FSMContext):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Студия"), KeyboardButton(text="1к")],
            [KeyboardButton(text="2к"), KeyboardButton(text="3к")],
            [KeyboardButton(text="4к и более"), KeyboardButton(text="Апартаменты")],
            [KeyboardButton(text="Коммерция")]
        ],
        resize_keyboard=True
    )
    await message.answer("🏠 Выберите тип недвижимости:", reply_markup=kb)
    await state.set_state(Form.property_type)

# ----------------- Тип недвижимости -----------------
@dp.message(Form.property_type)
async def process_type(message: Message, state: FSMContext):
    await state.update_data(property_type=message.text)
    await message.answer("💰 Введите ваш бюджет (в рублях):", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.budget)

# ----------------- Бюджет -----------------
@dp.message(Form.budget)
async def process_budget(message: Message, state: FSMContext):
    await state.update_data(budget=message.text)
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Да"), KeyboardButton(text="Да — льготная")],
            [KeyboardButton(text="Нет")]
        ],
        resize_keyboard=True
    )
    await message.answer("🏦 Будет ли использована ипотека?", reply_markup=kb)
    await state.set_state(Form.mortgage)

# ----------------- Ипотека -----------------
@dp.message(Form.mortgage)
async def process_mortgage(message: Message, state: FSMContext):
    await state.update_data(mortgage=message.text)
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📞 Начать подбор недвижимости", request_contact=True)]],
        resize_keyboard=True
    )
    await message.answer("Отлично! Нажмите кнопку ниже, чтобы поделиться контактом:", reply_markup=kb)
    await state.set_state(Form.contact)

# ----------------- Контакт -----------------
@dp.message(Form.contact)
async def process_contact(message: Message, state: FSMContext):
    if not message.contact:
        await message.answer("Пожалуйста, поделитесь контактом через кнопку.")
        return

    data = await state.get_data()
    contact = message.contact.phone_number
    name = message.contact.first_name or message.from_user.full_name
    username = message.from_user.username or "—"
    user_id = message.from_user.id
    now = datetime.now().strftime("%d.%m.%Y %H:%M")

    await add_request([
        now,
        name,
        data.get("city"),
        data.get("property_type"),
        data.get("budget"),
        data.get("mortgage"),
        contact,
        f"@{username}",
        user_id
    ])

    text = (
        f"📩 Новая заявка:\n\n"
        f"👤 {name}\n"
        f"🏙 Город: {data.get('city')}\n"
        f"🏠 Тип: {data.get('property_type')}\n"
        f"💰 Бюджет: {data.get('budget')}\n"
        f"🏦 Ипотека: {data.get('mortgage')}\n"
        f"📞 Телефон: {contact}\n"
        f"🕓 {now}"
    )

    for admin in ADMIN_IDS:
        try:
            await bot.send_message(admin, text)
        except TelegramBadRequest as e:
            logging.warning(f"Не удалось отправить сообщение админу {admin}: {e}")

    await message.answer("✅ Спасибо! Свяжемся с вами в ближайшее время.", reply_markup=None)
    await state.clear()

# ----------------- Запуск -----------------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())