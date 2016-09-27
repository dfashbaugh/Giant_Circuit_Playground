#include <Adafruit_CircuitPlayground.h>

float X, Y, Z, temp;
int light, sound;

int cap_3, cap_2; //Top left
int cap_1, cap_0; //Bot left
int cap_9, cap_10; //Top right
int cap_6, cap_12; //Bot right

bool slideSwitch, L_button, R_button;

String delim = "\t";

void setup() {
  Serial.begin(9600);
  CircuitPlayground.begin();
}

void loop() {
  X = CircuitPlayground.motionX();
  Y = CircuitPlayground.motionY();
  Z = CircuitPlayground.motionZ();
  
  temp = CircuitPlayground.temperature();

  slideSwitch = CircuitPlayground.slideSwitch(); //True if Left, False if Right

  L_button = CircuitPlayground.leftButton(); //0 Unless pressed
  R_button = CircuitPlayground.rightButton();

  light = CircuitPlayground.lightSensor();

  sound = CircuitPlayground.soundSensor();

  cap_2 = CircuitPlayground.readCap(2); 
  cap_3 = CircuitPlayground.readCap(3); 
  cap_0 = CircuitPlayground.readCap(0); 
  cap_1 = CircuitPlayground.readCap(1); 
  cap_9 = CircuitPlayground.readCap(9); 
  cap_10 = CircuitPlayground.readCap(10); 
  cap_6 = CircuitPlayground.readCap(6); 
  cap_12 = CircuitPlayground.readCap(12); 

  Serial.print(X);
  Serial.print(delim);

  Serial.print(Y);
  Serial.print(delim);

  Serial.print(Z);
  Serial.print(delim);

  Serial.print(temp);
  Serial.print(delim);

  Serial.print(slideSwitch);
  Serial.print(delim);

  Serial.print(L_button);
  Serial.print(delim);

  Serial.print(R_button);
  Serial.print(delim);

  Serial.print(light);
  Serial.print(delim);

  Serial.print(sound);
  Serial.print(delim);

  Serial.print(cap_2);
  Serial.print(delim);

  Serial.print(cap_3);
  Serial.print(delim);

  Serial.print(cap_0);
  Serial.print(delim);

  Serial.print(cap_1);
  Serial.print(delim);

  Serial.print(cap_9);
  Serial.print(delim);

  Serial.print(cap_10);
  Serial.print(delim);

  Serial.print(cap_6);
  Serial.print(delim);

  Serial.println(cap_12);


  delay(100);
}

