from raya.application_base import RayaApplicationBase
from itertools import product
import typing
if typing.TYPE_CHECKING:
    from controllers import LedsController

import random

class RayaApplication(RayaApplicationBase):
    async def setup(self,
            )-> None:
    
        self.leds:LedsController = await self.enable_controller('leds')
        self.groups = await self.leds.get_groups()
        self.colors = ['red', 'green', 'blue']


    async def main(self,
            )-> None:
        self.log.warning(f'Setting animations...')

        for color, group in product(
            self.colors, self.groups
        ):
            await self.leds.set_color(
                group=group, 
                color=color,
                wait=True,
            )

        for group in self.groups:
            self.log.info(f'Group: {group}')
            self.log.info(f'')
            self.log.info('Colors:')
            for color in self.colors: self.log.info(f' - {color}')
            self.animations = await self.leds.get_animations(group)
            self.log.info(f'')
            self.log.info('Animations:')
            for animation in self.animations: self.log.info(f' - {animation}')
            animation = random.choice(self.animations)
            speed = random.randint(1, 2)
            repetitions = random.randint(1, 3)
            color = random.choice(self.colors)

            self.log.info(f'')
            self.log.info(f'Running: group={group}, animation={animation}')
            self.log.info(f'         speed={speed}, repetitions={repetitions}')
            self.log.info(f'         color={color}')

            await self.leds.animation(
                    group = group, 
                    color = color, 
                    animation = animation, 
                    speed = speed, 
                    repetitions = repetitions, 
                    execution_control = 0,
                    wait=True
                )
        
            await self.sleep(2.0)

            

        self.finish_app()


    async def finish(self,
            )-> None:
        self.log.info(f'App finished!')
