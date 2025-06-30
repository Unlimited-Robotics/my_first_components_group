from raya.controllers.base_controller import BaseController
from raya.controllers import LedsController as CustomLedsController
from raya.handlers.command_handler import CommandHandler

class LedsController(CustomLedsController):

    async def animation():
        ...

    @property
    def animation() -> CommandHandler:
        ...

    async def set_color():
        ...

    @property
    def set_color() -> CommandHandler:
        ...