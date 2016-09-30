#include <Adafruit_CircuitPlayground.h>

boolean playedSoundRed = false;
boolean playedSoundBlue = false;
boolean playedSoundYellow = false;
boolean playedSoundGreen = false;

float X, Y, Z, temp;
int light, sound;

int cap_3, cap_2; //Top left
int cap_1, cap_0; //Bot left
int cap_9, cap_10; //Top right
int cap_6, cap_12; //Bot right

int mode = 2;
int cyclesUntilPush = 2;
int curCycles = 0;

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

  curCycles++;
  if(L_button && curCycles > cyclesUntilPush)
  {
    mode--;
    if(mode == -1)
      mode = 3;
    mode = mode%4;
    curCycles = 0;
    if(mode == 0)
      CircuitPlayground.playTone(800, 100);
    else if(mode == 1)
      CircuitPlayground.playTone(1000, 100);
    else if(mode == 2)
      CircuitPlayground.playTone(1200, 100);
    else if(mode == 3)
      CircuitPlayground.playTone(1600, 100);
  }
  else if(R_button && curCycles > cyclesUntilPush)
  {
    mode++;
    mode = mode%4;
    curCycles = 0;
    if(mode == 0)
      CircuitPlayground.playTone(800, 100);
    else if(mode == 1)
      CircuitPlayground.playTone(1000, 100);
    else if(mode == 2)
      CircuitPlayground.playTone(1200, 100);
    else if(mode == 3)
      CircuitPlayground.playTone(1600, 100);
  }


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

  int redValue = (cap_2+cap_3);
  if(redValue > 255) 
    redValue = 255;
  if(redValue > 100 && !playedSoundRed)
  {
    CircuitPlayground.playTone(800, 100);
    playedSoundRed = true;
  }
  else if(redValue < 10)
    playedSoundRed = false;
  CircuitPlayground.setPixelColor(0, redValue,   0,   0);
  CircuitPlayground.setPixelColor(1, redValue,   0,   0);

  int greenValue = (cap_0+cap_1);
  if(greenValue > 255)
    greenValue = 255;
  if(greenValue > 100 && !playedSoundGreen)
  {
    CircuitPlayground.playTone(800, 100);
    playedSoundGreen = true;
  }
  else if(greenValue < 10)
    playedSoundGreen = false;
  CircuitPlayground.setPixelColor(3, 0,   greenValue,   0);
  CircuitPlayground.setPixelColor(4, 0,   greenValue,   0);

  int blueValue = (cap_6+cap_12);
  if(blueValue > 255)
    blueValue = 255;
  if(blueValue > 100 && !playedSoundBlue)
  {
    CircuitPlayground.playTone(800, 100);
    playedSoundBlue = true;
  }
  else if(blueValue < 10)
    playedSoundBlue = false;
  CircuitPlayground.setPixelColor(5, 0,   0,   blueValue);
  CircuitPlayground.setPixelColor(6, 0,   0,   blueValue);

  int yellowValue = (cap_9+cap_10);
  if(yellowValue > 255)
    yellowValue = 255;
  if(yellowValue > 100 && !playedSoundYellow)
  {
    CircuitPlayground.playTone(800, 100);
    playedSoundYellow = true;
  }
  else if(yellowValue < 10)
    playedSoundYellow = false;
  CircuitPlayground.setPixelColor(8, yellowValue,   yellowValue,   0);
  CircuitPlayground.setPixelColor(9, yellowValue,   yellowValue,   0);


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

  Serial.print(cap_12);
  Serial.print(delim);

  Serial.println(mode);

  delay(50);

}

