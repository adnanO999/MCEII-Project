#include <math.h>

#define motor_A 2
#define motor_B 4

int count = 0;

const int DELTA_T = 100; //milliseconds

unsigned long current_time = 0l;
unsigned long previous_time = 0l; 

void setup() {
  
  Serial.begin(115200);

  pinMode(motor_A,  INPUT);
  pinMode(motor_B,  INPUT);
  attachInterrupt(digitalPinToInterrupt(motor_A), phase_A, RISING);

}

void loop() {

  current_time = millis();

  if((current_time - previous_time) > DELTA_T){
    Serial.println(count);
    previous_time = current_time;
  }
}

void phase_A(){

  if(digitalRead(motor_A)){

    if(digitalRead(motor_B)){ count--; }
    else{ count++; }

  }else{

    if(digitalRead(motor_B)){ count++; }
    else{ count--; }

  }
}

void phase_B(){

  if(digitalRead(motor_B)){

    if(digitalRead(motor_A)){ count++; }
    else{ count--; }

  }else{

    if(digitalRead(motor_A)){ count--; }
    else{ count++; }

  }
}