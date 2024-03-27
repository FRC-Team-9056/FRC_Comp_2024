#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib
import wpilib.drive
import math
import rev

import constants


class DriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.left1 = rev.CANSparkMax(
            constants.kLeftMotor1Port, rev.CANSparkMax.MotorType.kBrushed
        )
        self.left2 = rev.CANSparkMax(
            constants.kLeftMotor2Port, rev.CANSparkMax.MotorType.kBrushed
        )
        self.right1 = rev.CANSparkMax(
            constants.kRightMotor1Port, rev.CANSparkMax.MotorType.kBrushed
        )
        self.right2 = rev.CANSparkMax(
            constants.kRightMotor2Port, rev.CANSparkMax.MotorType.kBrushed
        )

        # Set current limits for the drivetrain motors
        self.left1.setSmartCurrentLimit(constants.kDTCurrentLimit)
        self.left2.setSmartCurrentLimit(constants.kDTCurrentLimit)
        self.right1.setSmartCurrentLimit(constants.kDTCurrentLimit)
        self.right2.setSmartCurrentLimit(constants.kDTCurrentLimit)

        self.leftDrive = wpilib.MotorControllerGroup(self.left1, self.left2)
        self.rightDrive = wpilib.MotorControllerGroup(self.right1, self.right2)
        self.leftDrive.setInverted(True)

        # The robot's drive
        self.drive = wpilib.drive.DifferentialDrive(
            self.leftDrive,
            self.rightDrive,
        )
        self.drive.setSafetyEnabled(False)

    def tankDrive(self, left: float, right: float) -> None:
        """
        Drives the robot using tank controls.

        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """
        # the following squares the motor inputs for the controller
        left_2 = math.copysign(left * left, left)
        right_2 = math.copysign(right * right, right)

        self.drive.tankDrive(left_2,right_2)
