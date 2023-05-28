# MCEII-Project
## Self-Balancing/Self-Parking Robot 

This project was developed as final project for the Mechatronics System Design II. We were asked to implement a project that uses either ANN or Fuzzy Logic as controller. As result we teamed up I (Adnan Abdallah), Firas Abou Karnib and Jennifer Metri. The work was devided into tasks and we collaborated all together to finalize the project and make it work. 

This is a brief description of the project, however each section was done in details along with all calculations, data collection, testing and implementation.
The project can be devided to the following sections:
* Obtaining system dynamics through Newtonian's equation or Lagrangian
* Implementing and simulating results using Matlab and simulink
* Assembling hardware
* Developing controller and testing theoretically the closed loop system after choosing the corresponding parameters based on our design
* Tesing the actual hardware
* Tuning our controller
* Finishing self balancing
* Repeating the process with self parking (we tried two models, reference control and reaction wheel)
* Collecting and visualizing data
* Summarizing our findgs in a report and presentaion
 

# Motivation
![selfbalancing](https://github.com/adnanO999/MCEII-Project/assets/88556508/9570f2c9-1389-4a82-8e89-6e6acecf86a0)
The two-wheel self-balancing and self-parking robot serves as yet another example of recent advancements in the field of robotics. A two-wheeled self-balancing robot is conceptualized using the inverted pendulum idea. This type of robot has attracted the attention of engineers and academics worldwide since it is based on a control system that is used to stabilize an unstable system by utilizing efficient microcontrollers and sensors. Smaller size and lower power requirements allow these robots to provide exceptional robustness and capabilities. Other applications for these kinds of solutions include transportation and monitoring. As a result, we decided to try and build a proof of concept for self-balancing and self-parking segways. Our methodology includes researching previous literature, modeling and simulating MATLAB, implementing the Fuzzy logic controllers and building the hardware, and then testing and evaluating our project performance.

# Project summary

This project details the development of a self-parking, self-balancing 2-wheel robot. The robot is intended to go around and park itself independently in a predetermined parking space while keeping its balance. The components compromising the robot are a chassis, two wheels, a microcontroller, a microprocessor, an IMU sensor, power supply, and a motor control system. A Raspberry Pi microprocessor is used to create the robot's control system, while the Arduino controller is used to act as the sensor interface, communicating its readings with the Raspberry Pi through serial communication. The Raspberry Pi takes readings from the Arduino and uses those measurements to operate the motors and balance the system to steer the robot to the appropriate parking location.


# Project Overview and First Testing Iterations
https://github.com/adnanO999/MCEII-Project/assets/88556508/9121b20d-c2b0-4872-b8e7-bf2f9ecbd9d4

The video demonstrates our working robot yet it was the beginig. We needed to tune more our controller along with getting more accurate readingns from the heart of our application which is the MPU6050. After several research we found that the accelerometer and gyroscope reading will accumulate error and eventually drift. Thus we needed a way to filter out noise and eliminate error. We found the Kalman filter will work for our application since we linearized our model and obtained the state space matrix. However with additional research we found the complementary filter to be a simpler approach and gave accurate results shown below.

# MPU6050 Readings 
To get the readings and plot them we collected the data using serial communication between arduino and python and accumulated them automatically in a CSV file. We could ploted them directly using matplotlib or seaborn however since we were using matlab for modeling the system dynamics we opted to keep all plots in matlab.

## Serial Communication
Since C++ is faster than python and Arduino we found additional resources relationg IMU and arduino we opted to read data using arduino and send the data serially to raspberrypi ensuring the correct delay for communication and keeping the a convininet buffer size to avoid overflow.

## Obtained Results

![image](https://github.com/adnanO999/MCEII-Project/assets/88556508/1a76a74f-060b-405e-929b-6d4012c55564)
we can clearly see how we have only one curve that is oscillating. This is the blue curve that corresponds to our angle of interest which is the angle along x axis. To be able to collect these data, we fixed the accelerometer on the chassis after we made sure that it is installed at zero angle and in the correct orientation, then we started to tilt chassis backward and forward while monitoring the actual angle change. We can tell that we have accurate measurements since we do not have angle drift and when the chassis is at rest (sample 200~325) the three angles are aligned with the horizontal axis.

# Modeling the Dynamics of the System
To control the robot more accurately, we rely on modeling to better grasp its dynamic nature. We defined several parameters prior to formulating mathematical equations
We started by defining our inputs to be the voltage of the motor and the outputs to be the tilt angle and tilt speed (in our case the actuator is included in the plant model). Adetailed calculation was carried out starting by Newton's Second Law and finishing by a state space representation. Matlab and simulink were used througout the process.
![image](https://github.com/adnanO999/MCEII-Project/assets/88556508/c282fabc-2b09-42a7-9a8c-6b0efdddf66a)

# Control Strategy
To be able to balance the system after modeling it, we must identify the best control approach. Strategies include Neural Network control, PID control, Fuzzy Logic control and many more. However, for this task we opted to use Fuzzy based control strategy.
Our Fuzzy Logic controller will be a classical Mamdani Max-Min fuzzy inference system. We have two input values provided by the IMU which is the tilt of the chassis “theta” (deg) and the chassis tilt speed “dtheta” (deg/s). The fuzzy logic controller must output the voltage needed to control both wheels and move the vehicle as needed
![image](https://github.com/adnanO999/MCEII-Project/assets/88556508/6bbbd398-09f4-4cce-9f75-60e17e7faa61)

# Simulink Model
![image](https://github.com/adnanO999/MCEII-Project/assets/88556508/c99be785-7c50-489b-a6d4-dbd13ad0fdf8)

# Self Balancing Results
![image](https://github.com/adnanO999/MCEII-Project/assets/88556508/5cfa5946-3d5f-4585-990b-2f2024612ae9)

# Self-Parking

Our aim for self-parking is to have the Segway move a specific distance in a straight line and then stop moving around that point. Since we have the self-balancing working already, we just needed a disturbance to be added by something in our system to cause the chassis to tilt in a desired direction and consequently move in that direction. 

However, since there is no research or previous literature on self-parking segways, we decided to explore two ways of achieving self-parking in our chassis: reaction wheels and reference control. Our choices were based on both logical observations we saw when working on self-balancing, as well as literature that suggests the use of reaction wheels for modifying the tilt of objects.


# Reaction Wheel
According to previous literature, we found that maximizing the kinetic energy expenditure of the flywheel is the easiest method of achieving effective control with the reaction wheel. Thus, we used a high rpm DC motor along with a 3D printed disk whose mass distribution is concentrated at the radius and weighted with added bolts.

![Annotation 2023-05-28 104814](https://github.com/adnanO999/MCEII-Project/assets/88556508/425f78ca-01ca-4a39-8256-bd27b1e86a58)

![image](https://github.com/adnanO999/MCEII-Project/assets/88556508/bb700b5f-d68b-431b-b2c7-3ccd45f44c80)

# Self-Parking Fuzzy Controller

Our control strategy for self-parking is as follows: rotating the wheel in one direction should cause a bias in the segway that will make move forwards, and the case is the same for the opposite direction. Our fuzzy logic controller is a Mamdani Max-Min fuzzy inference system, with the input “distance” which is the distance that the segway must travel. 

distance error = reference distance – position of chassis

![image](https://github.com/adnanO999/MCEII-Project/assets/88556508/21a24c7b-0627-43a5-b719-cbef33d9cb59)

# Self-Parking Reference Control
We chose reference control because we believed it would be effective since by adjusting the reference away from one, we can get constant movement in one direction which we desired

![image](https://github.com/adnanO999/MCEII-Project/assets/88556508/dc0522b1-5ac7-400a-8573-4363aee60aa7)

# Demo


https://github.com/adnanO999/MCEII-Project/assets/88556508/1426b765-1831-4dc0-810e-a5c639f75fe2




Thank you for reading. All project details are available in the repo.
