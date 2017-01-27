# ====== Legal notices
#
# Copyright (C) 2017 GEATEC engineering
#
# This program is free software.
# You can use, redistribute and/or modify it, but only under the terms stated in the licence.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, without even the implied warranty of
# MERCHANTABILITY or FIT

import sys as ss

programName = ss.argv [0]
libraryName = 'pyxy'
libraryVersion = '0.0.1'
logName = '{} - {} {}'.format (programName, libraryName.capitalize (), libraryVersion)
               
colorsHex = {
    'white'     : 'ffffff',
    'silver'    : 'c0c0c0',
    'gray'      : '808080',
    'black'     : '000000',
    'red'       : 'ff0000',
    'maroon'    : '800000',
    'yellow'    : 'ffff00',
    'olive'     : '808000',
    'lime'      : '00ff00',
    'green'     : '008000',
    'aqua'      : '00ffff',
    'teal'      : '008080',
    'blue'      : '0000ff',
    'navy'      : '000080',
    'fuchsia'   : 'ff00ff',
    'purple'    : '800080'
}

colorsRgb = {}

for key, value in colorsHex.items ():
    colorsRgb [key] = (int (value [0:2], 16) / 255., int (value [2:4], 16) / 255., int (value [4:6], 16) / 255.)
    
backgroundColorFactor = 0.25

def backgroundFromRgb (rgb):
    return (backgroundColorFactor * rgb [0], backgroundColorFactor * rgb [1], backgroundColorFactor * rgb [2])
