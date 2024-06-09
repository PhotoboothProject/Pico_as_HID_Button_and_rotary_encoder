#!/bin/bash
chromium-browser --noerrdialogs --disable-infobars --disable-features=Translate --no-first-run --check-for-update-interval=31536000 --kiosk http://localhost --touch-events=enabled --use-gl=egl &
sudo evsieve --input /dev/input/by-id/usb-Raspberry_Pi_Pico_E6614C311B1C7C37-if03-event-kbd grab \
        --hook key:t exec-shell="curl 127.0.0.1:14711/commands/start-picture" \
        --hook key:c exec-shell="curl 127.0.0.1:14711/commands/start-collage" \
        --hook key:p exec-shell="curl 127.0.0.1:14711/commands/start-print" \
        --hook key:v exec-shell="curl 127.0.0.1:14711/commands/start-video" \
        --hook key:u exec-shell="curl 127.0.0.1:14711/commands/start-custom" \
        --hook key:s exec-shell="curl 127.0.0.1:14711/commands/shutdown-now" \
        --hook key:enter exec-shell="curl 127.0.0.1:14711/commands/rotary-btn-press" \
        --hook key:left exec-shell="curl 127.0.0.1:14711/commands/rotary-ccw" \
        --hook key:right exec-shell="curl 127.0.0.1:14711/commands/rotary-cw"
