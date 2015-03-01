#!/usr/bin/env python

# Copyright (C) 2015 Umberto De Giovannini 
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.

import RPi.GPIO as GPIO
import sys
import argparse


GPIO.setmode(GPIO.BCM)

# the pins
SNDPIN=17 # sound on/off
GNPIN=18  # sound gain


VERSION = '0.0.1'


desc="""
Simple tool to make the Pi control the audio amplifier () via GPIO pins.
"""

epilog="""
Examples:

To turn on and off hardware audio:
\'%(prog)s -a on\'
and 
\'%(prog)s -a off\'

\n\n
"""

parser = argparse.ArgumentParser(version='%s version %s' %(sys.argv[0],VERSION),
                                 description=desc,
                                 epilog=epilog,
                                 formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-a', '--audio', action='store',
                    help='Switch on and off audio.')

parser.add_argument('-g', '--gain', action='store',
                    help='Enable gain amplification.')    

args = parser.parse_args()

print args.audio




if args.audio:
    GPIO.setup(SNDPIN, GPIO.OUT)
    if (args.audio.lower() == "on"):
        GPIO.output(SNDPIN, GPIO.HIGH)
    if (args.audio.lower() == "off"):
        GPIO.output(SNDPIN, GPIO.LOW)

if args.gain:
    GPIO.setup(GNPIN, GPIO.OUT)
    if (args.gain.lower() == "on"):
        GPIO.output(GNPIN, GPIO.HIGH)
    if (args.gain.lower() == "off"):
        GPIO.output(GNPIN, GPIO.LOW)
        
    

