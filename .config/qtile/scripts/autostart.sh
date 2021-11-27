#!/usr/bin/env bash

picom &
#conky -c $HOME/.config/conky/doomone-qtile.conkyrc
pasystray &
nm-applet &

nitrogen --restore &
