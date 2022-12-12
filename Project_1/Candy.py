# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Candy Dispenser
--------------------------------------------------------------------------
License:   
Copyright 2022 - Anas Yousaf

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Candy Dispenser that will
    - Use an ir beam to detect when a hand is waved
    - Rotate a servo to dispense candy when the ir beam is broken
    - Calculate and display the number of candy using an ir beam 

--------------------------------------------------------------------------
"""

"""
Sets the path to find the python file ht16k33. May need to change depending on 
where ht16k33 is located.
"""
import sys
sys.path.append("/var/lib/cloud9/ENGI301/Project_1")

import time
import math
import random

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import ht16k33 as HT16K33

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------
servo_pin = "P2_1"
FSR_pin = "AIN5"
ir1_pin = "P2_2"
ir2_pin = "P2_4"

# ------------------------------------------------------------------------
# Main Tasks
# ------------------------------------------------------------------------

def setup():
    """Set up hardware components."""
    GPIO.setup(ir1_pin, GPIO.IN)
    GPIO.setup(ir2_pin, GPIO.IN)
    HT16K33.setup()
    HT16K33.clear()
    
# end def

def open_door():
    """Makes servo open the dispensing door and close it again."""
    PWM.start(servo_pin, (100), 20.0)
    PWM.set_duty_cycle(servo_pin, 1.5)
    
    time.sleep(2.0)
    
    PWM.start(servo_pin, (100), 20.0)
    PWM.set_duty_cycle(servo_pin, 3.5)
    
    time.sleep(1.0)
    
    PWM.stop(servo_pin)
    PWM.cleanup()
    
# end def

def amount_calc():
    """Calculates the amount of candy in the candy dispenser by assuming one 
    piece of candy falls every second and subtracting the amount of time the ir
    sensor is open with the time at the start of the function."""
    """ WORK IN PROGRESS DUE TO UNAVAILABLE HARDWARE."""
    initial_time = time.time()
    count = int()
    while GPIO.input("P2_3") == 0:
        count = count + (initial_time+10 - initial_time)
    return count
# end def

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    setup()
    amount = amount_calc()
    while True:
        HT16K33.update(amount)
        if GPIO.input("P2_2") == 0:
            open_door()
            time.sleep(5)
        else:
            pass
        time.sleep(1)