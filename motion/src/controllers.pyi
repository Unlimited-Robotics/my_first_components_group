from raya.handlers.command_handler import CommandHandler
from raya.controllers.base_controller import BaseController
from raya.handlers.subscription_handler import SubscriptionHandler
from raya.handlers.publisher_handler import PublisherHandler

class NavigationController(BaseController):

    async def set_velocity():
        ...

    @property
    def set_velocity() -> CommandHandler:
        ...

    async def rotate():
        ...

    @property
    def rotate() -> CommandHandler:
        ...

    async def move_linear():
        ...

    @property
    def move_linear() -> CommandHandler:
        ...

    @property
    def navigation_status() -> SubscriptionHandler:
        ...

    @property
    def localization_status() -> SubscriptionHandler:
        ...