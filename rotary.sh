#!/bin/bash
evsieve --input /dev/input/event2 grab \
        --hook key:t exec-shell="curl 127.0.0.1:14711/commands/start-picture" \
        --hook key:c exec-shell="curl 127.0.0.1:14711/commands/start-collage" \
        --hook key:p exec-shell="curl 127.0.0.1:14711/commands/start-print" \
        --hook key:v exec-shell="curl 127.0.0.1:14711/commands/start-video" \
        --hook key:u exec-shell="curl 127.0.0.1:14711/commands/start-custom" \
        --hook key:s exec-shell="curl 127.0.0.1:14711/commands/shutdown-now" \
        --hook key:enter exec-shell="curl 127.0.0.1:14711/commands/rotary-btn-press" \
        --hook key:left exec-shell="curl 127.0.0.1:14711/commands/rotary-ccw" \
        --hook key:right exec-shell="curl 127.0.0.1:14711/commands/rotary-cw"
