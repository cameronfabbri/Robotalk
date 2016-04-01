#include <AFMotor.h>

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

String readString;

void setup() {
  Serial.begin(9600);
  motor1.setSpeed(75);
  motor2.setSpeed(75);
  motor3.setSpeed(75);
  motor4.setSpeed(75);
}

void backward(){
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);  
}

void forward(){
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}

void turn_left(){
  // left wheels
  motor4.run(FORWARD);
  motor1.run(FORWARD);
  
  // right wheels
  motor3.run(BACKWARD);
  motor2.run(FORWARD);
}

void turn_right(){
  // left wheels
  motor4.run(BACKWARD);
  motor1.run(BACKWARD);
  
  // right wheels
  motor3.run(FORWARD);
  motor2.run(BACKWARD);
}

void stop()
{
  motor1.setSpeed(75);
  motor2.setSpeed(75);
  motor3.setSpeed(75);
  motor4.setSpeed(75);

  // at some point make this a slow stop
    
}

void loop() {
  
  // listen for python
  while (!Serial.available()){}
      
  while (Serial.available())
  {
    char c = Serial.read();
    readString += c;   
  }
  
  Serial.print("read: ");
  Serial.print(readString);  
}
