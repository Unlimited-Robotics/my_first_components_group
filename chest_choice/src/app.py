import json

from raya.application_base import RayaApplicationBase


class RayaApplication(RayaApplicationBase):

    async def setup(self,
            ) -> None:
        self.ui = await self.enable_controller('ui')


    async def main(self,
            ) -> None:
        await self.sleep(2.0)

        goal_data = {
            'title': 'Which elevator am I in?',
            'data': [
                    {'id': 1, 'name': '1'},
                    {'id': 2, 'name': '2'},
                    {'id': 3, 'name': '3'},
                    {'id': 4, 'name': '4'},
            ],
            'theme': 'WHITE',
        }

        res = await self.ui.component(
            component='Choice',
            priority=2,
            goal_data=json.dumps(goal_data),
            wait=True,
        )

        self.log.info(f'Error code:{res.error_code}')
        self.log.info(f'Error msg:{res.error_msg}')
        self.log.info(f'Result data:{res.result_data}')

        await self.sleep(3.0)
