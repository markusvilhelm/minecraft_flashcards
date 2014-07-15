#!/usr/bin/python
# Written tng@chegwin.org 3-Jul-2014
# Python runs slower than C, so 18.9 factor below becomes 16.9 (microseconds)
sample_length=15.6/1000000.0
# Setup Pin 18 as output (Pin 12 in Pi numbering)
sample_length=15.6/1000000.0
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

#Remote
#Pulse coding: Short pulse length 53 - Long pulse length 162
#Short distance: 43, long distance: 157, packet distance: 1672

#Simulated
Pulse coding: Short pulse length 54 - Long pulse length 160
Short distance: 48, long distance: 161, packet distance: 799



#Calculate our on/offs up front
thirty=30*sample_length #27
thirtyonepointfive=31.5*sample_length
six=6*sample_length
four=4*sample_length


def one():
    #On  = 1 = 31.5 samples high, 6 low
    GPIO.output(18,True)
    time.sleep(thirtyonepointfive)
    GPIO.output(18,False)
    time.sleep(four)

def zero():
    #Off = 0 = 6 samples high, 30 low
    GPIO.output(18,True)
    time.sleep(six)
    GPIO.output(18,False)
    time.sleep(thirty)

def sequence(incoming_string):
    # Splits an incoming set of ones and zeros, runs the appropriate function
    # Loops 8 times through
    count =0
    # Make sure we are all off to start with
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18,False)
    time.sleep(450*sample_length)
    while count < 8:
        # Split the 1's and 0 into component parts and then run associated 
        #function
        for b in list(incoming_string):
            b = int(b)
            if (b == 0):
                zero()
            elif (b == 1):
                one()
            else:
                print ("Something gone wrong")
        count += 1
        # Sleep 150 samples between repetitions
        time.sleep(150*sample_length)
        GPIO.output(18,False)
    # Sleep 2 seconds between sequences
    time.sleep(0.3) 

def switch_socket(on_or_off): 
     # 1,2,3,4 on
#     sequence('1011111100010000000011110')
#     sequence('1011111100010000000001110')
     if (on_or_off == "on"):
         sequence('1011111100010000000010110')
     elif (on_or_off == "off"):
         sequence('1011111100010000000010100')
#         sequence('1011111100010000000011000')
#     time.sleep(1)
#     sequence('1011111100010000000000110')
     # 1,2,3,4 off
#     sequence('1011111100010000000011100')
#     sequence('1011111100010000000001100')
#     sequence('1011111100010000000000100')
     # Master
#     sequence('1011111100010000000011010')
#     sequence('1011111100010000000011000')
     GPIO.cleanup()

if __name__ == "__main__":
    try: 
        time.sleep(4)
        switch_socket("on")
        time.sleep(4)
        switch_socket("off")
    except (KeyboardInterrupt, SystemExit):
        print ("Thanks. Goodbye")
        GPIO.cleanup()
        exit();
