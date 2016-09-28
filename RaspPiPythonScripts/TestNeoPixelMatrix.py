import time
import serial
from NeoPixelMatrix import NeoPixelMatrix
from CircuitPlayGround import CircuitPlayGround
#from rgbmatrix import RGBMatrix
from SimulationMatrix import SimulationMatrix
from SimulationPlayGround import SimulationPlayGround
from PIL import Image
from PIL import ImageDraw

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
	#capValue = circuitPlayground.Cap12/10
	#neoMatrix.SetAllRed(circuitPlayground.Cap12/10)

	#First Interactive Mode
	brightness = float((circuitPlayground.Light))/1024
	channel1Value = 128 + 12*int(circuitPlayground.X)
	channel2Value = 128 + 12*int(circuitPlayground.Y)
	channel3Value = 128 + 12*int(CircuitPlayGround.Z)
	draw.rectangle( (0,0, 319, 31), fill = (int(brightness*channel1Value), int(brightness*channel2Value), int(brightness*channel3Value)), outline=(0,0,0))
	matrix.SetImage(image, 0, 0)

	#Simon


	#draw.rectangle( (0,0, 319, 31), fill = (0,0,0), outline=(0,0,0))
	#draw.rectangle((capValue, 0, capValue+31, 31), fill=(255, 0, 0), outline=(255,0,0))
	#neoMatrix.SetImage(image, 0, 0)
