# Raspberry Pi Pico / Pico W as HID device: Use of Hardware Buttons and Rotary Encoder
This a Raspberry Pi Pico / pico W CiruitPython code for using the Pico / Pico W as a USB HID device in the Photobooth Project of Andreas Blaesius (https://photoboothproject.github.io). You can connect several Buttons or a Rotary Encoder to trigger different actions.

Preparation:

1. Download the latest adafruit_circuitpython_etc.uf2 file and copy it on the CIRCUITPY drive as described here: https://learn.adafruit.com/pico-w-wifi-with-circuitpython/installing-circuitpython
2. Download the latest Adafruit CircuitPython Library Bundle that contains the required CircuitPython libraries for this project. Download the latest 8x.zip file from here: https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/
3. Unzip the zip file and copy the following files and folders from the lib folder to the CIRCUITPY lib folder: adafruit_debouncer.mpy, adafruit_ticks.mpy, adafruit_hid (complete folder)
4. Download the code.py file and copy it to the Pico´s CIRCUITPY folder.
5. Have fun!

<b>Expected behaviour:</b>  
Up to 5 buttons can be used to trigger up to 6 different keystrokes for start-picture, start-collage, start-custom, start-print, start-video and shutdown-now as descirbed in the documentation: https://photoboothproject.github.io/FAQ#can-i-use-hardware-button-to-take-a-picture.
There is also LED support for arcarde pushbuttons, meaning if you use a combined LED button, triggering the button will also light up the LED.
The keystrokes "T" for Take Pic and "C" for Collage are triggered by short and long press. That will only work if the keycodes are defined accordingly in the admin panel:

- Key code which triggers a picture: t = 84
- Key code which triggers a collage: c = 67
- Key code which triggers printing: p = 80
- Key code which triggers video: v = 86
- Key code which triggers custom URL: u = 85
- Key code which triggers shutdown: s = 83

Optional, if you want to use the rotary encoder for control on the user interface:
The rotary encoder triggers the key codes ENTER with a short press of the encoder pushbutton and ESC with a long press. A left turn (counterclockwise) triggers LEFT_ARROW and a right turn (clockwise) triggers RIGHT_ARROW. 
Unfortunately, the photobooth software does not implement a control option via keyboard commands. However, it allows control through the user interface via HTTP requests. With a little trick, the previous keyboard commands can be converted into HTTP requests. 
For this purpose you can install the software Evsieve from Kars Muder (https://github.com/KarsMulder/evsieve). It converts the USB HID device into a virtual event device and allows to execute a script when a predefined key is pressed.

After having installed the software you can find out the input ID of your "Raspberry Pico W Keyboard" with the follwoing command: 

sudo evsieve --input /dev/input/event* --print

Just press a push button to find out. Important is the number (=*) in "domain = /dev/input/event*".

Copy the bash script rotary.sh, make it executable with sudo chmod +x rotary.sh and change the * in the second line with your event number of the Pico. Also change the [Photobooth IP] and [Hardware Button Server Port] accoding to your requirements (sudo nano rotary.sh). Finally use systemd unit to run the script on bootup: Change the path of the rotary.sh in the file script.service and copy it to /etc/systemd/system/. After copying enable it via the systemctl command: sudo systemctl enable script.service

Any problems? Make sure that the Pico CIRCUITPY drive is mounted automatically...

