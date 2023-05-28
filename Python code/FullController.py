from SelfBalancingFuzzy import balance_controller
from SelfParkingFuzzy import parking_controller
from MotorControl import MotorController
from ReadingFromArduino import ReadingFromArduino
import time


if __name__ == "__main__":
    left_motor = MotorController(5, 6, 13)
    right_motor = MotorController(23, 24, 12)
    reaction_motor = MotorController(10, 9, 11)

    theta = 0
    dtheta = 0
    velocity = 0
    distance_travelled = 0

    reference_theta = 1  # reference theta desired
    reference_distance = 100

    distance_error = reference_distance - distance_travelled
    theta_error = theta - reference_theta  # this error is flipped cuz our controller works hek

    reaction_motor.set_speed(0)

    try:
        arduino = ReadingFromArduino()
        time.sleep(10)
        arduino.ser.flush()
        # reaction_motor.set_speed(-1)
        while True:

            start = time.time_ns()
            message = arduino.read_line()
            print(message)

            Arduino_values = message.split(', ')
            if len(Arduino_values) == 4:
                # print(Arduino_values)
                theta = float(Arduino_values[3])
                dtheta = float(Arduino_values[2])
                velocity = float(Arduino_values[1])
                distance_travelled = float(Arduino_values[0])

            distance_error = reference_distance - distance_travelled
            theta_error = theta - reference_theta  # this error is flipped cuz our controller works hek

            balance_controller.input["theta"] = theta_error
            balance_controller.input['dtheta'] = dtheta
            balance_controller.compute()

            # parking_controller.input['distance'] = distance_error
            # parking_controller.compute()

            balance_voltage = balance_controller.output['voltage']
            # parking_voltage = parking_controller.output['voltage']

            if balance_voltage > 1:
                balance_voltage = 1
            elif balance_voltage < -1:
                balance_voltage = -1

            # if parking_voltage > 1:
            #     parking_voltage = 1
            # elif parking_voltage < -1:
            #     parking_voltage = -1

            left_motor.set_speed(balance_voltage)
            right_motor.set_speed(balance_voltage)
            # reaction_motor.set_speed(parking_voltage)

            # duration = time.time_ns() - start
            # print("Time: ", duration)
            arduino.write("1")

    except KeyboardInterrupt:
        pass

    finally:
        arduino.close()
