import os
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart, Command
from bot.handlers.states import AddPhrase
from aiogram.fsm.context import FSMContext
from database_functions.sql_insert import add_phrases
from bot.utils.check_phrases import check_text
from database_functions.sql_edit import delete_phrase
from database_functions.sql_select import get_quantity_phrases_add_today

user1 = int(os.getenv('user1'))
users = {user1}


router = Router()


@router.message(CommandStart(), F.from_user.id.in_(users))
async def get_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}. Рад тебя видеть!')
    chat_id = message.chat.id
    await message.reply(f"Hello! Your chat_id is {chat_id}.")


@router.message(Command("add"), F.from_user.id.in_(users))
async def get_start(message: Message, state: FSMContext):
    await message.answer('ок. добавь вопрос')
    await state.set_state(AddPhrase.add_ask)


@router.message(AddPhrase.add_ask, F.from_user.id.in_(users))
async def get_cost(message: Message, state: FSMContext):
    if check_text(message.text.lower()):
        await state.update_data(ask=message.text.lower().replace("'", '"'))
        await message.answer(
            text='ок. теперь добавь ответ'

        )
        await state.set_state(AddPhrase.add_answer)
    else:
        await message.answer(
            text='нет такой буквы в этом слове!'

        )


@router.message(AddPhrase.add_answer, F.from_user.id.in_(users))
async def get_category_cost(message: Message, state: FSMContext):
    if check_text(message.text.lower()):
        await state.update_data(answer=message.text.lower())
        user_data = await state.get_data()
        await message.answer(
            text=f"добавляем вопрос/ответ {user_data['ask']} / {user_data['answer']}"
        )
        add_phrases(user_data['ask'], user_data['answer'])
        await state.clear()
    else:
        await message.answer(
            text="что за жалкое мычание?"
        )


@router.message(Command("delete"), F.from_user.id.in_(users))
async def get_start(message: Message, state: FSMContext):
    await message.answer('ок. добавь вопрос который надо удалить')
    await state.set_state(AddPhrase.delete)


@router.message(AddPhrase.delete, F.from_user.id.in_(users))
async def get_category_cost(message: Message, state: FSMContext):
    if check_text(message.text.lower()):
        await state.update_data(ask=message.text.lower().replace("'", '"'))
        user_data = await state.get_data()
        await message.answer(
            text=f"удалил фразу {user_data['ask']}"
        )
        delete_phrase(user_data['ask'])
        await state.clear()
    else:
        await message.answer(
            text="нет такой буквы в этом слове!"
        )


@router.message(Command("today"), F.from_user.id.in_(users))
async def get_start(message: Message):
    quantity = get_quantity_phrases_add_today()
    await message.answer(f'ок. сегодня в БД добавлено фраз: {quantity}')


if __name__ == "__main__":
    pass
