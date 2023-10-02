#!/bin/bash
evsieve --input /dev/input/event2 grab \
        --hook key:t exec-shell="curl [Photobooth IP]:14711/commands/start-picture" \
        --hook key:c exec-shell="curl [Photobooth IP]:14711/commands/start-collage" \
        --hook key:p exec-shell="curl [Photobooth IP]:14711/commands/start-print" \
        --hook key:v exec-shell="curl [Photobooth IP]:14711/commands/start-video" \
        --hook key:u exec-shell="curl [Photobooth IP]:14711/commands/start-custom" \
        --hook key:s exec-shell="curl [Photobooth IP]:14711/commands/shutdown-now" \
        --hook key:enter exec-shell="curl [Photobooth IP]:14711/commands/rotary-btn \
        --hook key:left exec-shell="curl [Photobooth IP]:14711/commands/rotary-ccw" \
        --hook key:right exec-shell="curl [Photobooth IP]:14711/commands/rotary-cw"


