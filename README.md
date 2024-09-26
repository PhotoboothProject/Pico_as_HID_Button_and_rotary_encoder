# Raspberry Pi Pico / Pico W as HID device: Use of Hardware Buttons and Rotary Encoder

This a Raspberry Pi Pico / Pico W CiruitPython code for using the Pico / Pico W as a USB HID device in the [Photobooth Project](https://photoboothproject.github.io). You can connect several Buttons or a Rotary Encoder to trigger different actions.

## Requirements:

- Download and install  CircuitPython as described [here](https://learn.adafruit.com/pico-w-wifi-with-circuitpython/installing-circuitpython)

## Preparation

1. Download and run the automated downloader to get needed files and libraries for your device.

The downloader also asks for your WiFi credentials to create the 
`settings.toml` file for you, also the Remotebuzzer Server IP and Port must be entered if asked to update the `code.py` automatically for you.

```sh
wget -O download-files.sh https://raw.githubusercontent.com/PhotoboothProject/Pico_W_as_remote_button_and_rotary_encoder/main/download-files.sh
bash download-files.sh
```

After running the script, the directory will be structured like this:

```
Photobooth_Pi_Pico_W_HTTP_clPhotobooth_Pi_Pico_W_HTTP_client/
├── library_info.txt
├── lib/
│   ├── adafruit_hid/
│   │   ├── .mpy files from the HID library
│   ├── adafruit_connection_manager.mpy
│   ├── adafruit_debouncer.mpy
│   ├── adafruit_requests.mpy
│   └── adafruit_ticks.mpy
├── code.py
└── settings.toml
```

2. Copy the `settings.toml`, `code.py` and `lib` folder to the Pico´s CIRCUITPY folder.

3. Have fun!

## Expected behaviour 

Up to 5 buttons can be used to trigger up to 6 different keystrokes for
- start-picture
- start-collage
- start-custom
- start-print
- start-video
- shutdown-now

as descirbed in the [Photobooth documentation](https://photoboothproject.github.io/FAQ#can-i-use-hardware-button-to-take-a-picture).

There is also LED support for arcarde pushbuttons, meaning if you use a combined LED button, triggering the button will also light up the LED.

### Button wiring
| Button Number | GP Number | LED GP Number | Short Press Keycode | Long Press Keycode |
|---------------|-----------|---------------|---------------------|-------------------|
| 1             | GP10      | GP11          | 84                  | 67                |
| 2             | GP12      | GP13          | 80                  | 80                |
| 3             | GP14      | GP15          | 86                  | 86                |
| 4             | GP16      | GP17          | 85                  | 85                |
| 5             | GP18      | GP19          | 83                  | 83                |
### Rotary encoder wiring
| GP Number | Encoder Action      | Keycode |
|-----------|---------------------|---------|
| GP2       | Short Press         | 13      |
| GP2       | Long Press          | 27      |
| GP3       | CW (Right Turn)     | 39      |
| GP4       | CCW (Left Turn)     | 37      |
### Keycode mapping
| Key            | Keycode |
|----------------|---------|
| `t`            | 84      |
| `c`            | 67      |
| `p`            | 80      |
| `v`            | 86      |
| `u`            | 85      |
| `s`            | 83      |
| ENTER          | 13      |
| ESC            | 27      |
| RIGHT_ARROW    | 39      |
| LEFT_ARROW     | 37      |

### Photobooth setup

The keystrokes `T` for Take Pic and `C` for Collage are triggered by short and long press. That will only work if the keycodes are defined accordingly in the admin panel:

- Key code which triggers a picture: t = 84
- Key code which triggers a collage: c = 67
- Key code which triggers printing: p = 80
- Key code which triggers video: v = 86
- Key code which triggers custom URL: u = 85
- Key code which triggers shutdown: s = 83

Optional, if you want to use the rotary encoder to control the user interface:
The rotary encoder triggers the key codes ENTER with a short press of the encoder pushbutton and ESC with a long press. A left turn (counterclockwise) triggers LEFT_ARROW and a right turn (clockwise) triggers RIGHT_ARROW.

### Rotary encoder support

Unfortunately, Photobooth has not implemented a control option via keyboard commands. However, it allows control through the user interface via HTTP requests. With a little trick, the previous keyboard commands can be converted into HTTP requests. For this purpose install the software [Evsieve](https://github.com/KarsMulder/evsieve) from Kars Mulder. It converts the USB HID device into a virtual event device and allows to execute HTTP request commands when predefined keys are pressed.

After having installed the software, copy the `rotary.sh` bash script, make it executable with `sudo chmod +x rotary.sh` and change the ID mentioned in the third line with the specific ID of your Pico / Pico W keyboard device. You can find it in the folder /dev/input/by-ID. Also change the [Photobooth IP] and [Hardware Button Server Port] accoding to your requirements (`sudo nano rotary.sh`) as defined on the Photobooth´s admin page. 

Then add the line `username ALL=NOPASSWD: /usr/local/bin/evsieve` at the end of /etc/sudoers (`sudo nano /etc/sudoers`).

Start the script in terminal with `sh /PATH/TO/rotary.sh`. Chromium browser should start and the rotary encoder should be avaiable. If you want to use another browser, change the command in the second line.

Finally, if you want to start Chomium and the rotary.sh script autmatically, change or create the xga-autostart photobooth.desktop file:
```sh
sudo nano /etc/xdg/autostart/photobooth.desktop
```
with the following content:
```
[Desktop Entry]
Version=1.3
Terminal=true
Type=Application
Name=Photobooth
Exec=/path/to/rotary.sh
Icon=/var/www/html/resources/img/favicon-96x96.png
StartupNotify=false
```

If it does not work: Pleae make sure that the "Remote Buzzer Server" is activated in your Photobooth. Deactivate the "GPIO support for remotebuzzer" server and activate "hardware buttons", the "rotary encoder" and additional buttons.
