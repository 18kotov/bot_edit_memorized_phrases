from aiogram.fsm.state import StatesGroup, State


class AddPhrase(StatesGroup):
    add_ask = State()
    add_answer = State()
    delete = State()
