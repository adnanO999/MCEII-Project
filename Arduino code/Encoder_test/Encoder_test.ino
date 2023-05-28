#include <math.h>

#define motor_1_A 2
#define motor_1_B 4

#define motor_2_A 3
#define motor_2_B 5

int count_1_A = 0;
int count_1_B = 0;
int count_2_A = 0;
int count_2_B = 0;

int x1_A = 0;
int x1_B = 0;
int x2_A = 0;
int x2_B = 0;

const int DELTA_T = 100; //milliseconds

unsigned long current_time = 0l;
unsigned long previous_time = 0l; 

void setup() {
  
  Serial.begin(115200);

  pinMode(motor_1_A, INPUT);
  pinMode(motor_1_B, INPUT);
  pinMode(motor_2_A, INPUT);
  pinMode(motor_2_B, INPUT);
}

void loop() {

  x1_A = digitalRead(motor_1_A);
  x1_B = digitalRead(motor_1_B);
  x2_A = digitalRead(motor_2_A);
  x2_B = digitalRead(motor_2_B);

  count_1_A += x1_A;
  count_1_B += x1_B;
  count_2_A += x2_A;
  count_2_B += x2_B;

  Serial.print("1_A:");
  Serial.print(x1_A);
  Serial.print(",\t");
  Serial.print("1_B:");
  Serial.print(x1_B);
  Serial.print(",\t");
  Serial.print("2_A:");
  Serial.print(x2_A);
  Serial.print(",\t");
  Serial.print("2_B:");
  Serial.print(x2_B);
  Serial.print(",\t");

  Serial.print("count_1_A:");
  Serial.print(count_1_A);
  Serial.print(",\t");
  Serial.print("count_1_B:");
  Serial.print(count_1_B);
  Serial.print(",\t");
  Serial.print("count_2_A:");
  Serial.print(count_2_A);
  Serial.print(",\t");
  Serial.print("count_2_B:");
  Serial.println(count_2_B);

  Serial.println();


  delayMicroseconds(100000);
}