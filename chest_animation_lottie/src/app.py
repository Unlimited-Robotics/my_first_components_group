import json
import asyncio

from raya.application_base import RayaApplicationBase
import raya.globals as globals


class RayaApplication(RayaApplicationBase):

    async def setup(self,
            ) -> None:
        self.ui = await self.enable_controller('ui')


    async def main(self,
            ) -> None:
        await self.sleep(0.5)

        with open(globals.APP_PATH/'lotties'/'loader.json', 'r',
                  encoding='utf-8') as file:
            lottie = json.load(file)

        goal_data = {
            'title': 'Hello everyone',
            'subtitle': 'This is a test',
            'type': 'LOTTIE',
            'theme': 'WHITE',
            'lottie': lottie,
        }

        res = await self.ui.component(
            component='Animation',
            priority=2,
            goal_data=json.dumps(goal_data),
            wait=True,
        )

        self.log.info(f'Error code:{res.error_code}')
        self.log.info(f'Error msg:{res.error_msg}')
        self.log.info(f'Result data:{res.result_data}')

        await asyncio.sleep(3.0)
