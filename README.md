# Giant Circuit Playground

This project contains all of the firmware and software necessary to make a giant circuit playground.

-----------------------------------------------------------

## Setup

### Actual Circuit Playground Firmware

The circuit playground firmware is in the "CircuitPlayGround2Ft" folder. 

Treat this as any other .ino file, and just flash it to the Actual Circuit Playground

### Teensy Firmware

The Teensy firmware is in the "TestEthern" folder. 

To flash the teensy, you will need to install Teensyduino into Arduino. The firmware should compile after Teensyduino has been setup.

After the firmware has been compiled, press the reset button on the Teensy to flash it.

### Raspberry Pi Python Script

The Raspberry Pi python scripts are in the "RaspPiPythonScripts" folder.

If this is a new setup, you will need to open the file TestNeoPixelMatrix.py and follow these steps:
* Scroll down to line 12 and set the SystemType variable as follows
 * SystemType = 0 for the 4 foot playground
 * SystemType = 1 for the 2 foot playground
* Test that running TestNeoPixelMatrix.py works.
* If it works, then we need to set this up to be called on reboot.
 * Find the path to the TestNeoPixelMatrix.py file
 * Edit /etc/rc.local as root
 * Write "sudo /usr/bin/python <path from first step> &" on the last line of the file
 * Save the file and reboot!
 
---------------------------------------
 
## Modes
 
### Attract Mode
 
Shows a series of animations, bright colors, and the DigiKey logo. Designed to grab attention from far away
 
### VJ Mode
 
Uses Accelerometers to spin a rainbow. Players can experiment with making the rainbow move faster, slower, reverse direction, and stop!
 
### Simon Mode
 
Play Simon! Hopefully we can call it "Simon" legally.

### Audio Reactive Mode
 
The circuit playground acts as a giant VU meter!

------------------------------------------------

## Troubleshooting

### My Circuit Playground won't respond to button presses!

Reset the circuit playground. 

There seems to be some issue with the capacitive touch sensing when the Circuit Playground sits for long periods of time.
Resetting the system will make it recalibrate.
