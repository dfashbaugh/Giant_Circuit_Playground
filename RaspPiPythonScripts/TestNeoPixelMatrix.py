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

def GetAttractModeImage(frame) :
	if frame > 200 :
		print 'Do second thing'
	elif frame > 400 :
		print 'Do third thing'
	else :
		print 'Do first thing'

	image = Image.new("RGB", (320, 32))
	draw = ImageDraw.Draw(image)
	draw.rectangle((0, 0, 319, 31), fill=(sound, 0, 0), outline=(255,255,0))
	return image

def LightSimonColors(colorList, frame, framesPerColor) :
	numColors = len(colorList)
	curColorAddr = frame/framesPerColor
	myColor = colorList[curColorAddr]

	image = Image.new("RGB", 320,32))

	if myColor == 0 :
		image = GetSimonRedImage()
	elif myColor == 1 :
		image = GetSimonYellowImage()
	elif myColor == 2 :
		image = GetSimonBlueImage()
	elif myColor == 3 :
		image = GetSimonGreenImage()

	return image

def ProcessSimonUserInput(cap10, cap9, cap6, cap12, cap3, cap2, cap0, cap1) :
	return

def CheckSimonColors(simonColors, playerColors) :
	for x in range(0, len(playerColors)) :
		if simonColors[x] != playerColors[x] :
			return 0

	if len(playerColors) == len(simonColors) :
		return 2

	return 1

#Overall Control Variables
frame = 0

#Game Variables
colorList = []
framesPerColor = 300
inputColors = []
capacitorThreshold = 100
simonState = 0 # 0 - Add new Color.. # 1 - Display Colors # 2 - Take User input # 3 - Lose

image = Image.new("RGB", (320, 32))
#image = Image.open("digikeyx10.png")
draw = ImageDraw.Draw(image)

lastDrawTime = 0
 
#circuitPlayground = CircuitPlayGround('/dev/cu.usbmodem1411')
circuitPlayground = SimulationPlayGround()

#matrix = NeoPixelMatrix('/dev/cu.usbmodem2115241')
matrix = SimulationMatrix()
#matrix = RGBMatrix(32, 10, 1)

matrix.Clear()
matrix.SetImage(image, 0, 0)

while 1:
	# Define the frame rate for the whole system.. Only for Neo Pixel
	if time.time() - lastDrawTime > 0.03 :
		matrix.DrawLEDMemory()
		lastDrawTime = time.time()

	circuitPlayground.Read()

	#First Interactive Mode
	#brightness = float((circuitPlayground.Light))/1024
	#channel1Value = 128 + 12*int(circuitPlayground.X)
	#channel2Value = 128 + 12*int(circuitPlayground.Y)
	#channel3Value = 128 + 12*int(CircuitPlayGround.Z)
	#draw.rectangle( (0,0, 319, 31), fill = (int(brightness*channel1Value), int(brightness*channel2Value), int(brightness*channel3Value)), outline=(0,0,0))
	#matrix.SetImage(image, 0, 0)

	#When ready for new color, set the ready for new color flag to 0 and the frame to 0
	if simonState == 0 :
		colorList.append(random.randrange(0,4))
		readyForNewColor = 0
		frame = 0
		simonState = 1
	elif simonState == 1 :
		matrix.SetImage(LightSimonColors(colorList, frame, framesPerColor), 0, 0)
		if frame > framesPerColor*len(colorList) : 
			matrix.Clear()
			simonState = 2
	elif simonState == 2 :
		newColor = ProcessSimonUserInput(circuitPlayground.cap10, circuitPlayground.cap9, circuitPlayground.cap6, circuitPlayground.cap12, circuitPlayground.cap3, circuitPlayground.cap2, circuitPlayground.cap0, circuitPlayground.cap1)
		if newColor >= 0 and newColor<=3 :
			inputColors.append(newColor)
			if CheckSimonColors(colorList, inputColors) == 0 :
				simonState = 3
			elif CheckSimonColors(colorList, inputColors) == 2 :
				simonState = 0
	elif simonState == 3 :
		colorList = []
		inputColors = []
		simonState = 0
		frame = 0



	frame = frame + 1



