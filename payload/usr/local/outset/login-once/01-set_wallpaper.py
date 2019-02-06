#!/usr/bin/python

'''Uses Cocoa classes via PyObjC to set a desktop picture on all screens.
Tested on Mountain Lion and Mavericks. Inspired by Greg Neagle's work: https://gist.github.com/gregneagle/6957826

See:
https://developer.apple.com/library/mac/documentation/cocoa/reference/applicationkit/classes/NSWorkspace_Class/Reference/Reference.html

https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html

https://developer.apple.com/library/mac/documentation/cocoa/reference/applicationkit/classes/NSScreen_Class/Reference/Reference.html

for some fun with python - in terminal: while true; do python /path/to/script
'''

from AppKit import NSWorkspace, NSScreen
from Foundation import NSURL
from os import listdir
from os import path
import random
import sys

picture_path = "/opt/company/wallpaper/"
if not path.exists(picture_path):
    sys.exit(1)
wallpapers = []

for item in listdir(picture_path):
    wallpapers.append(item)

picture_file = picture_path + random.choice(wallpapers)

# generate a fileURL for the desktop picture
file_url = NSURL.fileURLWithPath_(picture_file)

# make image options dictionary
# we just make an empty one because the defaults are fine
options = {}

# get shared workspace
ws = NSWorkspace.sharedWorkspace()

# iterate over all screens
for screen in NSScreen.screens():
    # tell the workspace to set the desktop picture
    (result, error) = ws.setDesktopImageURL_forScreen_options_error_(
                file_url, screen, options, None)
    if error:
        print error
        exit(-1)
