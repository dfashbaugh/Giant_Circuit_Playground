import time
import serial
from NeoPixelMatrix import NeoPixelMatrix
from CircuitPlayGround import CircuitPlayGround
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

image = Image.new("RGB", (320, 32))
#image = Image.open("digikeyx10.png")
draw = ImageDraw.Draw(image)

lastDrawTime = 0
 
circuitPlayground = CircuitPlayGround('/dev/cu.usbmodem1411')
neoMatrix = NeoPixelMatrix('/dev/cu.usbmodem2115241')

neoMatrix.Clear()
neoMatrix.SetImage(image, 0, 0)

while 1:
	if time.time() - lastDrawTime > 0.03 :
		neoMatrix.DrawLEDMemory()
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
	neoMatrix.SetImage(image, 0, 0)

	#Simon


	#draw.rectangle( (0,0, 319, 31), fill = (0,0,0), outline=(0,0,0))
	#draw.rectangle((capValue, 0, capValue+31, 31), fill=(255, 0, 0), outline=(255,0,0))
	#neoMatrix.SetImage(image, 0, 0)
