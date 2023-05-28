#!/usr/bin/env python3

import time
import serial


class ReadingFromArduino:

    def __init__(self, port='/dev/ttyUSB0', baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)

    def read_line(self):
        return self.ser.readline().decode('utf-8').strip()

    def write_line(self, message):
        self.ser.write((message + '\n').encode('utf-8'))

    def write(self, message):
        self.ser.write((message).encode('utf-8'))

    def close(self):
        self.ser.close()


if __name__ == "__main__":
    try:
        arduino = ReadingFromArduino()

        while True:
            time.sleep(0.01)
            # if arduino.in_waiting > 0:
            message = arduino.read_line()
            arduino.write("1")
            print(message)

    except KeyboardInterrupt:
        pass

    finally:
        arduino.close()
