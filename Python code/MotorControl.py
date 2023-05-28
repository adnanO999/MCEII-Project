#!/usr/bin/env python

import time
import RPi.GPIO as GPIO


class MotorController:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    def __init__(self, in1=17, in2=27, en=12):
        self.in1 = in1
        self.in2 = in2
        self.en = en  # not necessary

        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)

        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)

        self.pwm = GPIO.PWM(en, 100)
        self.pwm.start(0)

    def set_speed(self, speed):  # assuming input is (-1, 1)
        if speed < 0:
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)
        elif speed > 0:
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)
        else:
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.LOW)
        # print(speed)
        self.pwm.ChangeDutyCycle(abs(speed)*100)


if __name__ == "__main__":
    motor1 = MotorController(5, 6, 13)
    motor2 = MotorController(23, 24, 12)
    while True:
        motor1.set_speed(-1)
        motor2.set_speed(-1)
        time.sleep(2)
        motor1.set_speed(1)
        motor2.set_speed(1)
        time.sleep(2)
