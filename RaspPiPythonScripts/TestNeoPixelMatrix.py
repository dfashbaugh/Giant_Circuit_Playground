import time
import serial
from NeoPixelMatrix import NeoPixelMatrix
from CircuitPlayGround import CircuitPlayGround
from EtherNeoPixel import EtherNeoPixel
#from rgbmatrix import RGBMatrix
from SimulationMatrix import SimulationMatrix
from SimulationPlayGround import SimulationPlayGround
from PIL import Image
from PIL import ImageDraw
import random

def GetTestImage() :
	image = Image.new("RGB", (320, 32))
	#image = Image.open("digikeyx10.png")
	draw = ImageDraw.Draw(image)
	draw.line( (0,0,31,31), fill=(0,255,0) )
	draw.line( (0, 31, 31, 0), fill=(0,255,0) )
	draw.line( (32,0,63,31), fill=(255,0,0) )
	draw.line( (32, 31, 63, 0), fill=(255,0,0) )
	draw.rectangle((64, 0, 95, 31), fill=(0, 0, 255), outline=(255,0,0))
	draw.rectangle((96, 0, 127, 31), fill=(0, 255, 255), outline=(255,0,0))
	draw.rectangle((128, 0, 159, 31), fill=(255, 255, 0), outline=(255,0,0))
	draw.rectangle((160, 0, 191, 31), fill=(0, 255, 0), outline=(255,0,0))
	draw.rectangle((192, 0, 223, 31), fill=(0, 0, 0), outline=(255,0,0))
	draw.rectangle((224, 0, 255, 31), fill=(0, 0, 0), outline=(255,0,0))
	draw.rectangle((256, 0, 287, 31), fill=(0, 0, 0), outline=(0, 0,255))
	draw.rectangle((288, 0, 319, 31), fill=(0, 0, 0), outline=(255,255,255))
	return image

def GetSimonRedImage() :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((256, 0, 319, 31), fill=(255, 0, 0), outline=(255,0,0))
	return image

def GetSimonBlueImage() :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((96, 0, 159, 32), fill=(0, 0, 255), outline=(0,0,255))
	return image

def GetSimonGreenImage() :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((160, 0, 223, 32), fill=(0, 255, 0), outline=(0,255,0))
	return image

def GetSimonYellowImage() :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((0, 0, 63, 32), fill=(255, 255, 0), outline=(255,255,0))
	return image

def GetSimonBlackImage() :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((0, 0, 320, 32), fill=(0, 0, 0), outline=(0,0,0))
	return image

def GetSoundReactiveImage(sound, rainbowImage) :

	sound = 255-sound
	image = rainbowImage.copy()
	draw = ImageDraw.Draw(image)
	startPos = map(sound, 0, 255, 0, 320)
	draw.rectangle( (startPos, 0, 320, 31), fill=(0,0,0), outline =(0,0,0))
	return image

def GetAttractModeImage(frame, digiKeyLogo) :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)

	if frame > 612 :
		draw.rectangle( (0,0,320,32), fill=(0, 0, 2*((frame-612))%255), outline=(0,0,2*((frame-612))%255) )

	elif frame > 486 :
		draw.rectangle( (0,0,320,32), fill=(0, 2*((frame-486))%255, 0,), outline=(0,2*((frame-486))%255,0) )

	elif frame > 360 :
		draw.rectangle( (0,0,320,32), fill=(2*((frame-360))%255, 0, 0,), outline=(2*((frame-360))%255,0,0) )

	elif frame > 200 :
		draw.rectangle( (0, 0, 2*((frame-200))%320, 32), fill=(255, (frame-200)%255, 0), outline=(255,(frame-200)%255,0))
	
	elif frame > 100 :
		image = digiKeyLogo

	else :
		draw.rectangle( (0,0,320,32), fill=(0, (3*frame+100)%255, (10*frame+30)%255), outline=(0,(3*frame+100)%255,(10*frame+30)%255))

	return image

def GetVJModeImage(Light, X, Y, Z) :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	channel1Value = 128 + int(X*12)
	channel2Value = 128 + int(Y*12)
	draw.rectangle( (0,0, 320, 32), fill = (channel1Value, channel2Value, 120), outline=(channel1Value, channel2Value, 120))
	return image

def LightSingleSimonColor(color) : 
	image = Image.new("RGB", (320,32))

	if color == 0 :
		image = GetSimonRedImage()
	elif color == 1 :
		image = GetSimonYellowImage()
	elif color == 2 :
		image = GetSimonBlueImage()
	elif color == 3 :
		image = GetSimonGreenImage()

	return image

def LightSimonColors(colorList, frame, framesPerColor) :
	numColors = len(colorList)
	curColorAddr = frame/framesPerColor
	myColor = colorList[curColorAddr]

	if frame + 5 > framesPerColor + (frame/framesPerColor)*framesPerColor :
		return GetSimonBlackImage()
	return LightSingleSimonColor(myColor)

def ProcessSimonUserInput(cap10, cap9, cap6, cap12, cap3, cap2, cap0, cap1, capacitorThreshold) :

	if cap2 > capacitorThreshold or cap3 > capacitorThreshold :
		return 0
	elif cap9 > capacitorThreshold or cap10 > capacitorThreshold :
		return 1
	elif cap6 > capacitorThreshold or cap12 > capacitorThreshold :
		return 2
	elif cap0 > capacitorThreshold or cap1 > capacitorThreshold :
		return 3

	return 5

def CheckSimonColors(simonColors, playerColors) :
	for x in range(0, len(playerColors)) :
		if simonColors[x] != playerColors[x] :
			return 0

	if len(playerColors) == len(simonColors) :
		return 2

	return 1

def GetFilledGreenImage(frame) :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle( (0,0,16*frame,32), fill=(0, 255, 0,), outline=(0,255,0) )
	return image

def GetRGBFromWheel(WheelPos) :
  WheelPos = 255 - WheelPos;
  if WheelPos < 85 :
    return (255-WheelPos*3, 0, WheelPos*3) 
  
  if WheelPos < 170 :
    WheelPos -= 85;
    return (0, WheelPos * 3, 255 - WheelPos * 3)

  WheelPos -= 170;
  return (WheelPos * 3, 255 - WheelPos * 3, 0)

def map(x, fromLow, fromHigh, toLow, toHigh) :
	return (x - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow

#Overall Control Variables
frame = 0
lastDrawTime = 0
mode = 3 # Mode = 0 : VJ Mode, Mode = 1 : Simon, Mode = 2 : Attract, Mode = 3 : VU Meter, Mode = 4 : Secret Test Image
circuitPlayGroundType = 1 # circuitPlayGroundType = 0 : Simulation, circuitPlayGroundType = 1 : Real
matrixType = 0 # matrixType = 0 : Simulation, matrixType = 1 : 32X32 RGB, matrixType = 2 : NeoPixel 8X8, MatrixType = 3 : Neo Pixel Ethernet
#circuitPlaygroundPort = '/dev/cu.usbmodem1411'
#neoPixelMatrixPort = '/dev/cu.usbmodem2115241'
circuitPlaygroundPort = '/dev/ttyACM0'
neoPixelMatrixPort = '/dev/serial0'

#Game Variables
colorList = []
framesPerColor = 15
inputColors = []
capacitorThreshold = 100
simonState = 0 # 0 - Add new Color.. # 1 - Display Colors # 2 - Take User input # 3 - Lose
lastUserInputTime = 0

# Image Preprocessing
image = Image.new("RGB", (320, 32))
digiKeyLogoImage = Image.open("digikeyx10.png")
draw = ImageDraw.Draw(image)

rainbowImage = Image.new("RGB", (320, 32))
draw = ImageDraw.Draw(rainbowImage)
draw.rectangle( (0,0, 319, 31), fill=(0,0,0), outline=(0,0,0))
px = rainbowImage.load()
for x in range(0, 320) :
	for y in range(0, 32) :
		px[x,y] = GetRGBFromWheel(map(x, 0, 320, 0, 255))

image = GetTestImage()

# Initialize the Hardware!
if circuitPlayGroundType == 0 :
	circuitPlayground = SimulationPlayGround()
else :
	circuitPlayground = CircuitPlayGround(circuitPlaygroundPort)

if matrixType == 0 :
	matrix = SimulationMatrix()
elif matrixType == 1 :
	matrix = RGBMatrix(32, 10, 1)
elif matrixType == 2 :
	matrix = NeoPixelMatrix(neoPixelMatrixPort)
else  :
	matrix = EtherNeoPixel()


matrix.Clear()
matrix.SetImage(image, 0, 0)


#The main loop where all the magic happens
#
#
while 1:
	# Define the frame rate for the whole system.. Only for Neo Pixel
	if matrixType > 1 :
		if time.time() - lastDrawTime > 0.05 :
			matrix.DrawLEDMemory()
			lastDrawTime = time.time()
			
	circuitPlayground.Read()
	mode = circuitPlayground.Mode

	if mode != 1 :
		colorList = []
		inputColors = []
		simonState = 0

	if mode == 0 :
		image = GetVJModeImage(circuitPlayground.Light, circuitPlayground.X, circuitPlayground.Y, circuitPlayground.Z)
		matrix.SetImage(image, 0, 0)

	elif mode == 1 :
		#When ready for new color, set the ready for new color flag to 0 and the frame to 0
		if simonState == 0 : #New 
			colorList.append(random.randrange(0,4))
			frame = 0
			simonState = 5

		elif simonState == 5 :
			matrix.SetImage(GetFilledGreenImage(frame), 0 ,0)
			if frame > 20 :
				simonState = 1
				frame = 0
	
		elif simonState == 1 :
			if frame == framesPerColor*len(colorList) : 
				matrix.Clear()
				inputColors = []
				simonState = 2
			else :
				matrix.SetImage(LightSimonColors(colorList, frame, framesPerColor), 0, 0)
	
		elif simonState == 2 :
			newColor = ProcessSimonUserInput(circuitPlayground.Cap10, circuitPlayground.Cap9, circuitPlayground.Cap6, circuitPlayground.Cap12, circuitPlayground.Cap3, circuitPlayground.Cap2, circuitPlayground.Cap0, circuitPlayground.Cap1, capacitorThreshold)
			if newColor >= 0 and newColor<=3 and time.time() - lastUserInputTime > 1.0:
				matrix.SetImage(LightSingleSimonColor(newColor), 0, 0)
				inputColors.append(newColor)
				simonState = 3

		elif simonState == 3 :
			newColor = ProcessSimonUserInput(circuitPlayground.Cap10, circuitPlayground.Cap9, circuitPlayground.Cap6, circuitPlayground.Cap12, circuitPlayground.Cap3, circuitPlayground.Cap2, circuitPlayground.Cap0, circuitPlayground.Cap1, capacitorThreshold)
			if newColor > 3 :
				matrix.Clear() 
				simonResult = CheckSimonColors(colorList, inputColors)
				if simonResult == 0 :
					simonState = 4
					frame = 0
				elif simonResult == 2 :
					simonState = 0
				else :
					simonState = 2

		elif simonState == 4 :
			draw = ImageDraw.Draw(image)
			if frame%2 == 0 :
				draw.rectangle( (0,0, 320, 32), fill = (255,0,0), outline=(0,0,0))
			else :
				draw.rectangle( (0,0, 320, 32), fill = (0,0,0), outline=(0,0,0))
			matrix.SetImage(image, 0, 0)
			if frame > 50 :
				simonState = 6

		else :
			colorList = []
			inputColors = []
			simonState = 0
			frame = 0

	elif mode == 2 :
		matrix.SetImage( GetAttractModeImage(frame, digiKeyLogoImage), 0, 0)
		if frame > 739 :
			frame = 0

	elif mode == 3 :
		image = GetSoundReactiveImage(circuitPlayground.Sound, rainbowImage)
		matrix.SetImage(image, 0, 0)

	else :
		image = GetTestImage()
		matrix.SetImage(image, 0, 0)

	frame = frame + 1

	

