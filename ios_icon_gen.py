#!/usr/bin/env python

import os
import sys

# See https://developer.apple.com/library/ios/documentation/userexperience/conceptual/mobilehig/IconMatrix.html
iphone_only = {
  'iTunesArtwork' : (512, 512), # 
  'iTunesArtwork@2x' : (1024, 1024), # app icon for the app store
  'Icon-60@2x.png' : (120, 120),
  'Icon-60@3x.png' : (180, 180),
  'Icon-76.png ' : (76, 76),
  'Icon-76@2x.png ' : (152, 152),
  'Icon-Small-40.png' : (40, 40),
  'Icon-Small-40@2x.png ' : (80, 80),
  'Icon-Small.png' : (29, 29),
  'Icon-Small@2x.png' : (58, 58),
  'Icon-Small@3x.png' : (87, 87),
}
if len(sys.argv) > 1:
  orignal = sys.argv[1]
else:
  print( 'ios_icon_gen.py <image to convert>' )
  quit(1)


command_fmt = 'convert {orignal} -resize {size[0]}x{size[1]} {name}'

for name, size in iphone_only.items():
  os.system( command_fmt.format( orignal=orignal, name=name, size=size ) )
  # print( command_fmt.format( name=name, size=size ) )

# vim:et:ts=2 sts=2 sw=2
