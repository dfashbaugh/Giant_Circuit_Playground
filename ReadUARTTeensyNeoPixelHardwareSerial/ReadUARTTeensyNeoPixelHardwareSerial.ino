#define USE_OCTOWS2811

#include <OctoWS2811.h>
#include <FastLED.h>

#define NUM_LEDS 1280
#define MEMORY_SIZE NUM_LEDS*3
#define REMOTE_MEMORY_SIZE 1920

byte drawingMemory[REMOTE_MEMORY_SIZE];
byte trueDrawingMemory[MEMORY_SIZE];

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

void correctDrawingMemory()
{
	for(int i = 0; i < REMOTE_MEMORY_SIZE; i++)
	{
		if(i < 64*3)
		{
			trueDrawingMemory[i] = drawingMemory[i];
		}
		else if(i < 64*2*3)
		{
			trueDrawingMemory[i+64*3] = drawingMemory[i];
		}
		else if(i < 64*3*3)
		{
			trueDrawingMemory[i + 2*64*3] = drawingMemory[i];
		}
		else if(i < 64*4*3)
		{
			trueDrawingMemory[i + 3*64*3] = drawingMemory[i];
		}
		else if(i < 64*5*3)
		{
			trueDrawingMemory[i + 4*64*3] = drawingMemory[i];
		}
		else if(i < 64*6*3)
		{
			trueDrawingMemory[i + 5*64*3] = drawingMemory[i];
		}
		else
		{
			trueDrawingMemory[i + 6*64*3] = drawingMemory[i];
		}
	}
}

void setup()
{
	Serial1.begin(500000);
	LEDS.addLeds <OCTOWS2811> (leds, NUM_LEDS/8).setCorrection( 0x9FFAF0 );
   	FastLED.show();
}

long lastMillis = 0;

void loop ()
{
	if(Serial1.available())
	{
		byte recvInfo = Serial1.read();

		if(memoryCounter < REMOTE_MEMORY_SIZE)
		{
			recvInfo = map(recvInfo, 0, 255, 0, 128);
			drawingMemory[memoryCounter] = recvInfo;
			memoryCounter++;
		}

		CheckForDelimeter(recvInfo);
	}

	if(memoryCounter == REMOTE_MEMORY_SIZE)
	{
         for(int i = 0; i < NUM_LEDS; i++ )
         {
         	CRGB myColor;
         	myColor.green = trueDrawingMemory[i*3];
         	myColor.red = trueDrawingMemory[i*3+1];
         	myColor.blue = trueDrawingMemory[i*3+2];
          	leds[i] = myColor;
         }

         FastLED.show();
	}
}

