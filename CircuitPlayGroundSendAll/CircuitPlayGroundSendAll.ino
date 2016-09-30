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

int soundList [1000];
int soundCounter = 0;

int lastRead = 0;

int animationFrame = 0;

String delim = "\t";

#define MIC_PIN         A4  // Microphone is attached to this analog pin (A4 for circuit playground)
#define SAMPLE_WINDOW   10  // Sample window for average level
#define PEAK_HANG       24  // Time of pause before peak dot falls
#define PEAK_FALL        4  // Rate of falling peak dot
#define INPUT_FLOOR     10  // Lower range of analogRead input
#define INPUT_CEILING  500  // Max range of analogRead 


float fscale( float originalMin, float originalMax, float newBegin, float
newEnd, float inputValue, float curve){

  float OriginalRange = 0;
  float NewRange = 0;
  float zeroRefCurVal = 0;
  float normalizedCurVal = 0;
  float rangedValue = 0;
  boolean invFlag = 0;


  // condition curve parameter
  // limit range

  if (curve > 10) curve = 10;
  if (curve < -10) curve = -10;

  curve = (curve * -.1) ; // - invert and scale - this seems more intuitive - postive numbers give more weight to high end on output 
  curve = pow(10, curve); // convert linear scale into lograthimic exponent for other pow function

  /*
   Serial.println(curve * 100, DEC);   // multply by 100 to preserve resolution  
   Serial.println(); 
   */

  // Check for out of range inputValues
  if (inputValue < originalMin) {
    inputValue = originalMin;
  }
  if (inputValue > originalMax) {
    inputValue = originalMax;
  }

  // Zero Refference the values
  OriginalRange = originalMax - originalMin;

  if (newEnd > newBegin){ 
    NewRange = newEnd - newBegin;
  }
  else
  {
    NewRange = newBegin - newEnd; 
    invFlag = 1;
  }

  zeroRefCurVal = inputValue - originalMin;
  normalizedCurVal  =  zeroRefCurVal / OriginalRange;   // normalize to 0 - 1 float

  // Check for originalMin > originalMax  - the math for all other cases i.e. negative numbers seems to work out fine 
  if (originalMin > originalMax ) {
    return 0;
  }

  if (invFlag == 0){
    rangedValue =  (pow(normalizedCurVal, curve) * NewRange) + newBegin;

  }
  else     // invert the ranges
  {   
    rangedValue =  newBegin - (pow(normalizedCurVal, curve) * NewRange); 
  }

  return rangedValue;
}


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

  cap_2 = CircuitPlayground.readCap(2); 
  cap_3 = CircuitPlayground.readCap(3); 
  cap_0 = CircuitPlayground.readCap(0); 
  cap_1 = CircuitPlayground.readCap(1); 
  cap_9 = CircuitPlayground.readCap(9); 
  cap_10 = CircuitPlayground.readCap(10); 
  cap_6 = CircuitPlayground.readCap(6); 
  cap_12 = CircuitPlayground.readCap(12); 

  if(mode == 1)
  {
    for(int i = 0; i < 10; i++)
    {
      CircuitPlayground.setPixelColor(i, 0,   0,   0);
    }

    int redValue = (cap_2+cap_3);
    if(redValue > 255) 
      redValue = 255;
    if(redValue > 200 && !playedSoundRed)
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
    if(greenValue > 200 && !playedSoundGreen)
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
    if(blueValue > 200 && !playedSoundBlue)
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
    if(yellowValue > 200 && !playedSoundYellow)
    {
      CircuitPlayground.playTone(800, 100);
      playedSoundYellow = true;
    }
    else if(yellowValue < 10)
      playedSoundYellow = false;
    CircuitPlayground.setPixelColor(8, yellowValue,   yellowValue,   0);
    CircuitPlayground.setPixelColor(9, yellowValue,   yellowValue,   0);
  }
  else if(mode == 2 || mode == 0)
  {
    int colorValue = 0;
    if(animationFrame > 25)
      colorValue = 255 - (animationFrame*10)%255;
    else
      colorValue = (animationFrame*10)%255;

    for(int i = 0; i < 10; i++)
    {
      CircuitPlayground.setPixelColor(i, colorValue,   colorValue,   colorValue);
    }
  }
  else if(mode == 3)
  {
    for(int i = 0; i < 10; i++)
    {
      CircuitPlayground.setPixelColor(i, 255-sound,   0,   0);
    }
  }

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

  unsigned int signalMax = 0;
  unsigned int sample = 0;
  unsigned int peakToPeak = 0;
  unsigned int signalMin = 1023;
  unsigned int c, y;
  unsigned long startMillis = millis();

  // collect data for length of sample window (in mS)
  while (millis() - startMillis < 50)
  {
    sample = analogRead(MIC_PIN);
    if (sample < 1024)  // toss out spurious readings
    {
      if (sample > signalMax)
      {
        signalMax = sample;  // save just the max levels
      }
      else if (sample < signalMin)
      {
        signalMin = sample;  // save just the min levels
      }
    }
  }
  peakToPeak = signalMax - signalMin;  // max - min = peak-peak amplitude

  //Scale the input logarithmically instead of linearly
  sound = fscale(INPUT_FLOOR, INPUT_CEILING, 10, 0, peakToPeak, 2);
  sound = map(sound, 0,10, 0, 255);

  animationFrame++;
  if(animationFrame > 50)
    animationFrame = 0;

}


