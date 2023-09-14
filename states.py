from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    choosing_lan = State()
    menu = State()