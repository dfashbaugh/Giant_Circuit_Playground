#define USE_OCTOWS2811

#include <OctoWS2811.h>
#include <FastLED.h>

#define NUM_LEDS 512
#define MEMORY_SIZE NUM_LEDS*3

byte drawingMemory[MEMORY_SIZE];

CRGB leds[NUM_LEDS];

long memoryCounter = 0;

int recvState = 0;
void CheckForDelimeter(byte recvInfo)
{
	if(recvInfo == 's' && recvState == 0)
		recvState = 1;
	else if(recvInfo == 't' && recvState == 1)
		recvState = 2;
	else if(recvInfo == 'a' && recvState == 2)
		recvState = 3;
	else if(recvInfo == 'r' && recvState == 3)
		recvState = 4;
	else if(recvInfo == 't' && recvState == 4)
	{
		recvState = 0;
		memoryCounter = 0;
	}
	else
		recvState = 0;
}

void setup()
{
	Serial.begin(9600);
	LEDS.addLeds <OCTOWS2811> (leds, NUM_LEDS/8).setCorrection( 0x9FFAF0 );
   	FastLED.show();
}

long lastMillis = 0;

void loop ()
{
	if(Serial.available())
	{
		byte recvInfo = Serial.read();

		if(memoryCounter < MEMORY_SIZE)
		{
			recvInfo = map(recvInfo, 0, 255, 0, 128);
			drawingMemory[memoryCounter] = recvInfo;
			memoryCounter++;
		}

		CheckForDelimeter(recvInfo);
	}

	if(memoryCounter == MEMORY_SIZE)
	{
         for(int i = 0; i < NUM_LEDS; i++ )
         {
         	CRGB myColor;
         	myColor.green = drawingMemory[i*3];
         	myColor.red = drawingMemory[i*3+1];
         	myColor.blue = drawingMemory[i*3+2];
          	leds[i] = myColor;
         }

         FastLED.show();
	}
}

