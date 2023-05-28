from SelfBalancingFuzzy import balance_controller
from Ref_SelfParkingFuzzy import reference_controller
from MotorControl import MotorController
from ReadingFromArduino import ReadingFromArduino
import time


if __name__ == "__main__":
    left_motor = MotorController(5, 6, 13)
    right_motor = MotorController(23, 24, 12)

    theta = 0
    dtheta = 0
    # velocity = 0
    distance_travelled = 0 

    reference_theta = 1  # reference theta desired
    reference_distance = 1000


    distance_error = reference_distance - distance_travelled
    theta_error = theta - reference_theta  # this error is flipped cuz our controller works hek

    try:
        arduino = ReadingFromArduino()
        time.sleep(10)
        arduino.ser.flush()
        while True:

            # start = time.time_ns()
            message = arduino.read_line()
            print(message,",", reference_theta)

            Arduino_values = message.split(', ')
            if len(Arduino_values) == 4:
                # print(Arduino_values)
                theta = float(Arduino_values[3])
                dtheta = float(Arduino_values[2])
                # velocity = float(Arduino_values[1])
                distance_travelled = float(Arduino_values[0])

            # print(reference_theta)

            distance_error = reference_distance - distance_travelled
            theta_error = theta - reference_theta  # this error is flipped cuz our controller works hek

            balance_controller.input["theta"] = theta_error
            balance_controller.input['dtheta'] = dtheta
            balance_controller.compute()

            reference_controller.input['distance'] = distance_error
            reference_controller.compute()

            balance_voltage = balance_controller.output['voltage']
            reference_theta = (reference_controller.output['reference'] * 0.6) + 1 


            if balance_voltage > 1:
                balance_voltage = 1
            elif balance_voltage < -1:
                balance_voltage = -1

            left_motor.set_speed(balance_voltage)
            right_motor.set_speed(balance_voltage)

            # duration = time.time_ns() - start
            # print("Time: ", duration)
            arduino.write("1")

    except KeyboardInterrupt:
        pass

    finally:
        arduino.close()
