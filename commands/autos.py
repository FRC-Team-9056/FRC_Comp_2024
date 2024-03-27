#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import constants
from .launchnote import LaunchNote
from subsystems.can_drivesubsystem import DriveSubsystem
from subsystems.can_launchersubsystem import LauncherSubsystem


class Autos(commands2.Command):
    def __init__(self) -> None:
        raise Exception("This is a utility class!")

    @staticmethod
    def simpleAuto(driveSubsystem: DriveSubsystem):
        """A simple auto routine that drives forward a specified time, and then stops."""
        return commands2.cmd.sequence(
            commands2.StartEndCommand(
            # Drive forward while the command is executing,
            lambda: driveSubsystem.tankDrive(constants.kAutoDriveSpeed, constants.kAutoDriveSpeed),
            lambda: driveSubsystem.tankDrive(0.0,0.0),
            driveSubsystem
            ).withTimeout(constants.kAutoDriveTime),
        )
    
    @staticmethod
    def complexAuto(driveSubsystem: DriveSubsystem, launcherSubsystem: LauncherSubsystem):
        #A more complex auto routine that launch the note at certain speed, and then stops.
        return commands2.cmd.sequence(
            LaunchNote().withTimeout(constants.kAutoLaunchTime),
            commands2.StartEndCommand(
            # Drive forward while the command is executing,
            lambda: driveSubsystem.tankDrive(constants.kAutoDriveSpeed, constants.kAutoDriveSpeed),
            lambda: driveSubsystem.tankDrive(0.0,0.0),
            driveSubsystem
            ).withTimeout(constants.kAutoDriveTime),
        )

