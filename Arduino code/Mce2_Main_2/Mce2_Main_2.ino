#include <math.h>
#include "MPU6050_tockn.h"
#include <Wire.h>

#define leftmotor_A 2
#define leftmotor_B 4

#define rightmotor_A 3
#define rightmotor_B 5

MPU6050 mpu6050(Wire);

int left_count = 0;
// int right_count = 0;

int movement= 0;
double movement_theta = 0.0;
double distance = 0.0;
double velocity = 0.0;

const int RESOLUTION = 470; //idk, pulses per rotation? and *2 because it's 2x the base pulses per revolution
const int DELTA_T = 10; //milliseconds
const double WHEEL_RADIUS = 7.5; //cm

unsigned long current_time = 0l;
unsigned long previous_time = 0l; 

void setup() {
  
  Serial.begin(115200);

  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);

  Serial.println();
  Serial.println();

  pinMode(leftmotor_A,  INPUT);
  pinMode(leftmotor_B,  INPUT);
  pinMode(rightmotor_A, INPUT);
  pinMode(rightmotor_B, INPUT);
  attachInterrupt(digitalPinToInterrupt(leftmotor_A), phase_A_left, RISING);
  // attachInterrupt(digitalPinToInterrupt(rightmotor_A), phase_A_right, CHANGE);

}

void loop() {

  current_time = millis();
  mpu6050.update();

  if(((current_time - previous_time) > DELTA_T)){ // && ((left_count >= 0 && right_count >= 0) || (left_count < 0 && right_count < 0))){

    // if (left_count >= 0 && right_count >= 0){
    //   movement = min(left_count, right_count); //pulses
    // }else{
    //   movement = max(left_count, right_count);
    // }
    movement = left_count;

    movement_theta = (2.0 * M_PI * movement) / RESOLUTION; //radians
    distance += movement_theta * WHEEL_RADIUS; 
    velocity = 1000.0*(movement_theta * WHEEL_RADIUS)/(current_time - previous_time); // i decided linear cm/s idk
    left_count = 0;
    // right_count = 0;

    // Serial.print(movement);
    // Serial.print(", ");
    Serial.print(String(distance) + ", " + String(velocity));
    Serial.print(", ");
    Serial.print(mpu6050.getGyroX());
    Serial.print(", ");
    Serial.println(mpu6050.getAngleX()+1);

    while(Serial.available() == 0){}
    Serial.read();

    previous_time = current_time;
  }
}

void phase_A_left(){

  if(digitalRead(leftmotor_A)){

    if(digitalRead(leftmotor_B)){ left_count--; }
    else{ left_count++;}

  }else{

    if(digitalRead(leftmotor_B)){ left_count++; }
    else{ left_count--; }

  }
}

// void phase_A_right(){

//   if(digitalRead(rightmotor_A)){

//     if(digitalRead(rightmotor_B)){ right_count--; }
//     else{ right_count++;}

//   }else{

//     if(digitalRead(rightmotor_B)){ right_count++; }
//     else{ right_count--; }

//   }
// }
