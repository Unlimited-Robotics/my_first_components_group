from raya.application_base import RayaApplicationBase
import json

game_config = {  # [ ] Remove start modal
    'component': 'FindDifference',
    'goal_data':  {
        'theme': 'WHITE',
        'difficulty': 'Beginner',  # ! overwritten in code
        'title': 'מצא את ההבדלים',
        'button_text': 'התחל',
        'pageTitle': 'מצא את ההבדלים',
        'show_start_modal': False,
        'start_button_timeout': 7,
        # 'loaderTime' : '15',
        # 'loaderText' : 'בהצלחה',
        # 'languages' : [],
        'chosen_language': 'en',
        'end_game_text': ' משחק הבא',
        'custom_style': {
            'pageTitle': {
                'color': 'black'
            }
        }
    }
}

wait = False


class RayaApplication(RayaApplicationBase):

    async def setup(self,
            ) -> None:
        self.log.info('Hello from setup()')
        self.ui = await self.enable_controller('ui')


    async def loop(self,
            ) -> None:
        result = await self.ui.component(
            component=game_config['component'],
            goal_data=json.dumps(game_config['goal_data']),
            wait=wait,
            priority=2,
            cb_feedback=self.async_callback_feedback,
            cb_finish=self.async_callback_finish_game
        )
        if wait:
            self.log.info(f'Game result: {result}')
        else:
            self.log.info('sent game component')
            while True:
                if not self.ui.component.is_running():
                    break
                await self.sleep(1)
        self.log.info('finish game component')
        self.finish_app()


    async def finish(self,
            ) -> None:
        self.log.info('Hello from finish()')


    async def async_callback_feedback(self,
                msg=None,
            ) -> None:
        self.log.warning(f'Received game feedback msg: {msg}')


    async def async_callback_finish_game(self,
                msg=None,
            ) -> None:
        self.log.warning(f'Received game finish msg: {msg}')
