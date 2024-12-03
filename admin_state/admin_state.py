from aiogram.fsm.state import StatesGroup, State


class admin_panel(StatesGroup):
    sending_message = State()
