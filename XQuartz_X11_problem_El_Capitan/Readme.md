Author: Bhishan Poudel, Physics PhD student Ohio University
Date  : Mar 15, 2018

Topic: Installing XQuartz (or X11) in simplici El Capitan(MacOs 10.11)
==========================================================================
Description: XQuartz was formerly names X11.
XQuartz allows cross-platform applications using X11 for the GUI to run on macOS.

Need: fv viewer needs X11.

Command: `cd /Applications/fv.app/Contents/MacOS/; ./fv`

Error: Unable to find application named 'X11'

Direct Error: Type XQuartz in SpotLight and open 
              XQuartz cannot be opened because of a problem.
              
              
Website: https://www.xquartz.org/
```
2.7.7 only support Yosemite # failed
2.7.8 should support El Capitan # failed
2.7.9 should support El Capitan # failed
2.7.10 should support El Capitan # failed
2.7.11 should support El Capitan # failed
```
on March 2018, 2.7.11 is the latest. So I kept it even if not working.


Linking:
======================================================
a) link dylib file:
```
locate libSM.6.dylib  # /opt/X11/lib/libSM.6.dylib
ls /usr/X11           # nothing
sudo ln -s /usr/X11 /opt/X11 
```

b) Link libpng file:
```
ls /usr/local/lib/libpng15.15.dylib  # If file exist, backup it.
sudo ln -s /opt/X11/lib/libpng15.15.dylib /usr/local/lib/libpng15.15.dylib
```
