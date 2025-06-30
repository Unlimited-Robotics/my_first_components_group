from raya.application_base import RayaApplicationBase
import typing

if typing.TYPE_CHECKING:
    from src.controllers import *


class RayaApplication(RayaApplicationBase):
    async def setup(self,
                    ) -> None:
        self.log.info(f'Setup')
        self.nav: NavigationController = (
            await self.enable_controller('navigation'))


    async def main(self,
            ) -> None:
        self.log.info('Rotating 90 degrees left at 20 deg/secs')
        await self.nav.rotate(
            angle_offset=1.57,
            angular_speed=0.3,
            enable_obstacle=True,
            callback_finish=self.cb_motion_finished,
            wait=True
        )
        self.log.info('Motion command finished')
        self.log.info('')
        self.log.info(
            'Rotating 1.5708 radians left (90 degrees) at 0.349 rads/sec'
        )

        await self.nav.rotate(
            angle_offset=1.57,
            angular_speed=-0.3,
            wait=True,
            callback_finish=self.cb_motion_finished
        )

        self.log.info('Motion command finished')

        self.log.info('Moving forward 0.5 meters at 0.2 m/s')
        await self.nav.move_linear(
            distance=0.5,
            x_velocity=0.2,
            enable_obstacles=True,
            wait=True,
            callback_finish=self.cb_motion_finished

        )
        self.log.info('Motion command finished')
        self.log.info('')

        self.log.info('Moving backward 0.5 meters at 0.3 m/s')
        await self.nav.move_linear(
            distance=0.5,
            x_velocity=-0.2,
            enable_obstacles=True,
            wait=False,
            callback_finish=self.cb_motion_finished

        )

        while self.nav.move_linear.is_running():
            await self.sleep(0.1)

        self.log.info('Motion command finished')
        self.log.info('')

        self.log.info('Moving forward at 0.3 m/s for 2.0 seconds')
        await self.nav.set_velocity(
            x_velocity=0.3,
            y_velocity=0.0,
            angular_velocity=0.0,
            wait=True,
            duration=2.0,
            callback_finish=self.cb_motion_finished
        )

        self.log.info('Motion command finished')
        self.log.info('')

        self.log.info('Moving backward at 0.3 m/s and rotate at 10 deg/sec')
        await self.nav.set_velocity(
            x_velocity=0.3,
            y_velocity=0.0,
            angular_velocity=10.0,
            duration=10.0,
            wait=False,
            callback_finish=self.cb_motion_finished,
            callback_feedback=self.cb_motion_feedback
        )
        self.log.info('for 10 seconds')
        await self.sleep(5.0)
        self.log.info('Canceling motion after 5.0 seconds')
        await self.nav.set_velocity.cancel_all()
        self.log.info('Motion command finished')
        self.log.info('')

        self.finish_app()


    async def finish(self,
            ) -> None:
        try:
            if self.motion.is_moving():
                self.log.info('Stopping motion')
                await self.motion.cancel_motion()
        except AttributeError:
            pass
        self.log.info('Finish app called')


    def cb_motion_feedback(self,
                feedback_code,
                feedback_msg,
                time_left,
                nearby_obstacle,
            ) -> None:
        self.log.info(f'Motion feedback: {time_left}')


    def cb_motion_finished(self,
                error_code,
                error_msg,
            ) -> None:

        self.log.info('Motion finished callback called!')
        if error_code != 0:
            self.log.info(f'Motion command error {error_code}: {error_msg}')
        self.motion_flag = False
