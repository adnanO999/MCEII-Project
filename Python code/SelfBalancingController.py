from SelfBalancingFuzzy import balance_controller
from MotorControl import MotorController
from ReadingFromArduino import ReadingFromArduino
import time


if __name__ == "__main__":
    left_motor = MotorController(5, 6, 13)
    right_motor = MotorController(23, 24, 12)

    theta = 0
    dtheta = 0
    reference_theta = 1

    try:
        arduino = ReadingFromArduino()
        time.sleep(10)
        arduino.ser.flush()
        while True:

            # time.sleep(0.01)
            # start = time.time_ns()
            message = arduino.read_line()
            print(message)

            IMUval = message.split(', ')
            if len(IMUval) == 4:
                # print(IMUval[3],IMUval[2])
                theta = float(IMUval[3])
                dtheta = float(IMUval[2])

            balance_controller.input["theta"] = theta - reference_theta
            balance_controller.input['dtheta'] = dtheta
            balance_controller.compute()

            voltage = balance_controller.output['voltage']
            if voltage>1:
                voltage = 1
            elif voltage<-1:
                voltage = -1
            left_motor.set_speed(voltage)
            right_motor.set_speed(voltage)
            #print(voltage)
            # duration = time.time_ns() - start
            # print("Time: ", duration)
            arduino.write("1")

    except KeyboardInterrupt:
        pass

    finally:
        arduino.close()
