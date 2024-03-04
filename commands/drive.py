#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import constants

from robotcontainer import RobotContainer
#from subsystems.pwm_launchersubsystem import LauncherSubsystem

class DriveRobot(commands2.Command):
    def __init__(self, drive: RobotContainer.drive) -> None:
        super().__init__()
        self.drive = drive
        self.addRequirements(drive)

    def initialize(self) -> None:
        self.launcher.setLaunchWheel(constants.kLauncherSpeed)
        self.launcher.setFeedWheel(constants.kLaunchFeederSpeed)

    def isFinished(self) -> bool:
        return False

    def end(self, interrupted: bool) -> None:
        self.launcher.stop()