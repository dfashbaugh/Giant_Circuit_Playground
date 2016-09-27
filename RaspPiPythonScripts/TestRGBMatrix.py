import time
import serial
from NeoPixelMatrix import NeoPixelMatrix
from CircuitPlayGround import CircuitPlayGround
from PIL import Image
from PIL import ImageDraw
from rgbmatrix import RGBMatrix

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
draw.rectangle((160, 0, 191, 31), fill=(255, 0, 0), outline=(255,0,0))
draw.rectangle((192, 0, 223, 31), fill=(0, 255, 0), outline=(255,0,0))
draw.rectangle((224, 0, 255, 31), fill=(255, 0, 255), outline=(255,0,0))
draw.rectangle((256, 0, 287, 31), fill=(255, 255, 255), outline=(255,0,0))
draw.rectangle((256, 0, 287, 31), fill=(0, 0, 0), outline=(255,255,0))
image.show()

lastDrawTime = 0
 
circuitPlayground = CircuitPlayGround('/dev/cu.usbmodem1411')
matrix = RGBMatrix(32, 10, 1)

matrix.Clear()
matrix.SetImage(image, 0, 0)

while 1:

	circuitPlayground.Read()
	capValue = circuitPlayground.Cap12/10
	#neoMatrix.SetAllRed(circuitPlayground.Cap12/10)

	#First Interactive Mode
	brightness = float((circuitPlayground.Light))/1024
	#print circuitPlayground.Light
	channel1Value = 128 + 12*int(circuitPlayground.X)
	channel2Value = 128 + 12*int(circuitPlayground.Y)
	channel3Value = 128 + 12*int(CircuitPlayGround.Z)
	draw.rectangle( (0,0, 319, 31), fill = (int(brightness*channel1Value), int(brightness*channel2Value), int(brightness*channel3Value)), outline=(0,0,0))
	matrix.SetImage(image, 0, 0)

	#draw.rectangle( (0,0, 319, 31), fill = (0,0,0), outline=(0,0,0))
	#draw.rectangle((capValue, 0, capValue+31, 31), fill=(255, 0, 0), outline=(255,0,0))
	#neoMatrix.SetImage(image, 0, 0)
