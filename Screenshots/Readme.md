# Using screenshots in Mac
```
Default:  cmd-shift-3   save whole screen to desktop
Default:  cmd-shift-4   interactive screen to desktop
```

# Using Grab
```
Open the Grab app (from searchlight, or alfred)
When Grab is open: cmd3 screen
                   cmd4 selection
                   cmd5 window
                   
# Terminal commands to change type of image
# png (default is png) jpg tiff gif pdf
defaults write com.apple.screencapture type jpg
killall SystemUIServer (or we can also restart mac)
```

# Using terminal command `screencapture`.
I also have alfred workflows for them with keybindings.
Note: First we have to disable keys at `System Preferences > Keyboard > Shortcuts > Screenshots`.
```
screencapture -h
screencapture -i -x ${HOME}/Dropbox/Screenshots/$(date +%Y-%m-%d-%H-%M-%S).png
screencapture -i -M -x ${HOME}/Dropbox/Screenshots/$(date +%Y-%m-%d-%H-%M-%S).png

screencapture -w -x ${HOME}/Dropbox/Screenshots/$(date +%Y-%m-%d-%H-%M-%S).png
screencapture -w -M -x ${HOME}/Dropbox/Screenshots/$(date +%Y-%m-%d-%H-%M-%S).png

```
