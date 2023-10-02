# SPDX-FileCopyrightText: 2023 Frank Grootens, Berlin
# SPDX-License-Identifier: MIT 

import os
import time
import microcontroller
import supervisor
import board
import rotaryio
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Button
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#  The keyboard object!
kbd = Keyboard(usb_hid.devices)

btn1_pin = DigitalInOut(board.GP10)             ### Connect to GND
btn1_pin.direction = Direction.INPUT
btn1_pin.pull = Pull.UP                         
btn1 = Button(btn1_pin, short_duration_ms=500, long_duration_ms=1000, value_when_pressed=False)

led1 = digitalio.DigitalInOut(board.GP11)       ### Connect to GND
led1.direction = digitalio.Direction.OUTPUT

btn2_pin = DigitalInOut(board.GP12)             ### Connect to GND
btn2_pin.direction = Direction.INPUT
btn2_pin.pull = Pull.UP                         
btn2 = Button(btn2_pin, short_duration_ms=500, long_duration_ms=1000, value_when_pressed=False)

led2 = digitalio.DigitalInOut(board.GP13)       ### Connect to GND 
led2.direction = digitalio.Direction.OUTPUT        

btn3_pin = DigitalInOut(board.GP14)             ### Connect to GND 
btn3_pin.direction = Direction.INPUT            
btn3_pin.pull = Pull.UP                         
btn3 = Button(btn3_pin, short_duration_ms=500, long_duration_ms=1000, value_when_pressed=False)

led3 = digitalio.DigitalInOut(board.GP15)       ### Connect to GND 
led3.direction = digitalio.Direction.OUTPUT    

btn4_pin = DigitalInOut(board.GP16)             ### Connect to GND
btn4_pin.direction = Direction.INPUT
btn4_pin.pull = Pull.UP                       
btn4 = Button(btn4_pin, short_duration_ms=500, long_duration_ms=1000, value_when_pressed=False)

led4 = digitalio.DigitalInOut(board.GP17)       ### Connect to GND
led4.direction = digitalio.Direction.OUTPUT    

btn5_pin = DigitalInOut(board.GP18)             ### Connect to GND
btn5_pin.direction = Direction.INPUT            
btn5_pin.pull = Pull.UP                    
btn5 = Button(btn5_pin, short_duration_ms=500, long_duration_ms=1000, value_when_pressed=False)

led5 = digitalio.DigitalInOut(board.GP19)       ### Connect to GND
led5.direction = digitalio.Direction.OUTPUT

sw_pin = DigitalInOut(board.GP2)                ### Connect to GND
sw_pin.direction = Direction.INPUT
sw_pin.pull = Pull.UP                           
sw = Button(sw_pin, short_duration_ms=500, long_duration_ms=1000, value_when_pressed=False) 

encoder = rotaryio.IncrementalEncoder(board.GP4, board.GP3)
last_position = encoder.position
   
        
try:
    while True:
        btn1.update()
        led1.value = not btn1.value
        btn2.update()
        led2.value = not btn2.value
        btn3.update()
        led3.value = not btn3.value
        btn4.update()
        led4.value = not btn4.value
        btn5.update()
        led5.value = not btn5.value
        sw.update()
        
        try:
            if btn1.short_count:              
                    print("-" * 40)
                    print("Button 1 short pressed - send keycode T")
                    print("-" * 40)
                    kbd.send(Keycode.T) 
                    time.sleep(0.2)

            if btn1.long_press: 
                    print("-" * 40)
                    print("Button 1 long pressed - send keycode C")
                    print("-" * 40)
                    kbd.send(Keycode.C)                    
                    time.sleep(0.2)
        
            if btn2.short_count:
                    print("-" * 40)
                    print("Button 2 short pressed - send keycode P")
                    print("-" * 40)
                    kbd.send(Keycode.P) 
                    time.sleep(0.2)

            if btn2.long_press:
                    print("-" * 40)
                    print("Button 2 long pressed - send keycode P")
                    print("-" * 40)
                    kbd.send(Keycode.P) 
                    time.sleep(0.2)

            if btn3.short_count:
                    print("-" * 40)
                    print("Button 3 short pressed - send keycode V")
                    print("-" * 40)
                    kbd.send(Keycode.V) 
                    time.sleep(0.2)
                    
            if btn3.long_press:
                    print("-" * 40)
                    print("Button 3 long pressed - send keycode V")
                    print("-" * 40)
                    kbd.send(Keycode.V) 
                    time.sleep(0.2)

            if btn4.short_count:
                    print("-" * 40)
                    print("Button 4 short pressed - send keycode U")
                    print("-" * 40)
                    kbd.send(Keycode.U) 
                    time.sleep(0.2)

            if btn4.long_press:
                    print("-" * 40)
                    print("Button 4 long pressed - send keycode U")
                    print("-" * 40)
                    kbd.send(Keycode.U) 
                    time.sleep(0.2)
                    
            if btn5.short_count:
                    print("-" * 40)
                    print("Button 5 short pressed - send keycode S")
                    print("-" * 40)
                    kbd.send(Keycode.S) 
                    time.sleep(0.2)

            if btn5.long_press:
                    print("-" * 40)
                    print("Button 5 short pressed - send keycode S")
                    print("-" * 40)
                    kbd.send(Keycode.S) 
                    time.sleep(0.2)

            if sw.short_count:
                    print("-" * 40)
                    print("Rotary encoder push button short pressed - send keycode ENTER")
                    print("-" * 40)
                    kbd.send(Keycode.ENTER) 
                    time.sleep(0.2)
                
            if sw.long_press:
                    print("-" * 40)
                    print("Rotary encoder push button long pressed - send keycode ESC")
                    print("-" * 40)
                    kbd.send(Keycode.ESCAPE) 
                    time.sleep(0.2)
          
            current_position = encoder.position
            position_change = current_position - last_position
        
            if position_change > 0:
                for _ in range(position_change):
                    print("-" * 40)
                    print("Rotary encoder rotation ccw - send keycode LEFT_ARROW")
                    print("-" * 40)
                    kbd.send(Keycode.LEFT_ARROW) 
                    time.sleep(0.2)

            elif position_change < 0:
                for _ in range(-position_change):
                    print("-" * 40)
                    print("Rotary encoder rotation cw - send keycode RIGHT_ARROW")
                    print("-" * 40)
                    kbd.send(Keycode.RIGHT_ARROW) 
                    time.sleep(0.2)
              
            last_position = current_position
        
        except Exception as e:
            print("An error occured" ,e)
            time.sleep(2)
            supervisor.reload()

except Exception as e:
    print("An error occured" ,e)
    print("Pico will hard reset in 10 seconds")
    time.sleep(10)
    micorcontroller.reset()
