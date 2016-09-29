import time
import serial
from NeoPixelMatrix import NeoPixelMatrix
from CircuitPlayGround import CircuitPlayGround
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
	draw.rectangle((0, 0, 63, 31), fill=(255, 0, 0), outline=(255,0,0))
	return image

def GetSimonBlueImage() :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((64, 0, 127, 31), fill=(0, 0, 255), outline=(0,0,255))
	return image

def GetSimonGreenImage() :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((160, 0, 223, 31), fill=(0, 255, 0), outline=(0,255,0))
	return image

def GetSimonYellowImage() :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((224, 0, 287, 31), fill=(255, 255, 0), outline=(255,255,0))
	return image

def GetSoundReactiveImage(sound) :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((0, 0, 319, 31), fill=(sound, 0, 0), outline=(255,255,0))
	return image

def GetAttractModeImage(frame, digiKeyLogo) :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)

	if frame > 200 :
		draw.rectangle( (4*frame%319, 0, (4*frame+31)%319, 31), fill=(255, 0, 0), outline=(0,0,0))
	elif frame > 100 :
		image = digiKeyLogo
	else :
		draw.rectangle( (0,0,319,31), fill=(0, (3*frame+100)%255, (10*frame+30)%255), outline=(0,0,0))

	return image

def GetVJModeImage(Light, X, Y, Z) :
	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	brightness = float(Light)/1024
	channel1Value = 128 + 12*int(X)
	channel2Value = 128 + 12*int(Y)
	channel3Value = 128 + 12*int(Z)
	draw.rectangle( (0,0, 319, 31), fill = (int(brightness*channel1Value), int(brightness*channel2Value), int(brightness*channel3Value)), outline=(0,0,0))
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

	return LightSingleSimonColor(myColor)

def ProcessSimonUserInput(cap10, cap9, cap6, cap12, cap3, cap2, cap0, cap1, capacitorThreshold) :

	if cap10 > capacitorThreshold or cap9 > capacitorThreshold :
		return 0
	elif cap6 > capacitorThreshold or cap12 > capacitorThreshold :
		return 1
	elif cap3 > capacitorThreshold or cap2 > capacitorThreshold :
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

#Overall Control Variables
frame = 0
mode = 3 # Mode = 0 : VJ Mode, Mode = 1 : Simon, Mode = 2 : Attract, Mode = 3 : VU Meter
circuitPlayGroundType = 0 # circuitPlayGroundType = 0 : Simulation, circuitPlayGroundType = 1 : Real
matrixType = 0 # matrixType = 0 : Simulation, matrixType = 1 : 32X32 RGB, matrixType = 2 : NeoPixel 8X8
circuitPlaygroundPort = '/dev/cu.usbmodem1411'
neoPixelMatrixPort = '/dev/cu.usbmodem2115241'

#Game Variables
colorList = []
framesPerColor = 300
inputColors = []
capacitorThreshold = 100
simonState = 0 # 0 - Add new Color.. # 1 - Display Colors # 2 - Take User input # 3 - Lose
lastUserInputTime = 0

image = Image.new("RGB", (320, 32))
digiKeyLogoImage = Image.open("digikeyx10.png")
draw = ImageDraw.Draw(image)
image = GetTestImage()

lastDrawTime = 0
 
if circuitPlayGroundType == 0 :
	circuitPlayground = SimulationPlayGround()
else :
	circuitPlayground = CircuitPlayGround(circuitPlaygroundPort)

if matrixType == 0 :
	matrix = SimulationMatrix()
elif matrixType == 1 :
	matrix = RGBMatrix(32, 10, 1)
else :
	matrix = NeoPixelMatrix(neoPixelMatrixPort)

matrix.Clear()
matrix.SetImage(image, 0, 0)


#The main loop where all the magic happens
#
#
while 1:
	# Define the frame rate for the whole system.. Only for Neo Pixel
	if matrixType > 1 :
		if time.time() - lastDrawTime > 0.03 :
			matrix.DrawLEDMemory()
			lastDrawTime = time.time()
			
	circuitPlayground.Read()

	if mode == 0 :
		image = GetVJModeImage(circuitPlayground.Light, circuitPlayground.X, circuitPlayground.Y, circuitPlayground.Z)
		matrix.SetImage(image, 0, 0)

	elif mode == 1 :
		#When ready for new color, set the ready for new color flag to 0 and the frame to 0
		if simonState == 0 :
			colorList.append(random.randrange(0,4))
			frame = 0
			simonState = 1
	
		elif simonState == 1 :
			if frame == framesPerColor*len(colorList) : 
				matrix.Clear()
				simonState = 2
			else :
				matrix.SetImage(LightSimonColors(colorList, frame, framesPerColor), 0, 0)
	
		elif simonState == 2 :
			newColor = ProcessSimonUserInput(circuitPlayground.Cap10, circuitPlayground.Cap9, circuitPlayground.Cap6, circuitPlayground.Cap12, circuitPlayground.Cap3, circuitPlayground.Cap2, circuitPlayground.Cap0, circuitPlayground.Cap1, capacitorThreshold)
			if newColor >= 0 and newColor<=3 and time.time() - lastUserInputTime > 1.0:
				lastUserInputTime = time.time()
				matrix.SetImage(LightSingleSimonColor(newColor), 0, 0)
				inputColors.append(newColor)
				if CheckSimonColors(colorList, inputColors) == 0 :
					simonState = 3
				elif CheckSimonColors(colorList, inputColors) == 2 :
					simonState = 0
	
		else :
			colorList = []
			inputColors = []
			simonState = 0
			frame = 0

	elif mode == 2 :
		matrix.SetImage( GetAttractModeImage(frame, digiKeyLogoImage), 0, 0)
		if frame > 600 :
			frame = 0

	else :
		image = GetSoundReactiveImage(circuitPlayground.Sound)
		matrix.SetImage(image, 0, 0)

	frame = frame + 1

	

