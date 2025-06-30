from raya.handlers.command_handler import CommandHandler
from raya.controllers.base_controller import BaseController
from raya.handlers.subscription_handler import SubscriptionHandler
from raya.handlers.publisher_handler import PublisherHandler

class UiController(BaseController):

    async def component():
        ...

    @property
    def component() -> CommandHandler:
        ...

    async def finish():
        ...

    @property
    def finish() -> CommandHandler:
        ...

    @property
    def debug_text() -> PublisherHandler:
        ...