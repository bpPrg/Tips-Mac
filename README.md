- [Apps for mac](#apps-for-mac)
- [QuickLook Plugins](#quicklook-plugins)
- [Format markdown in Mail etc](#format-markdown-in-mail-etc)
- [Alfred](#alfred)
- [Show full path in Finder](#show-full-path-in-finder)
- [Mac Settings](#mac-settings)
- [Useful aliases and functions](#useful-aliases-and-functions)
- [Mac Malwares and Viruses](#mac-malwares-and-viruses)
- [Add spaces to dock](#add-spaces-to-dock)
- [Nofitications](#nofitications)
- [My customized finder](#my-customized-finder)

## Apps for mac
- NEVER download XQuartz (it harmed my dmstack), install xcode using atom, when installing atom, it installs xcode.
- CopyClip, Alfred, aText
- App Cleaner & Uninstaller
- Slack, Zotero, DS9, Latexit, [Time Out][time-out]
- BitBar # Put timer, spotify items etc plugins in Mac menubar.
- OneDrive, Google Drive, Dropbox
-  _Careful:_ [pCloud][pcloud] # It did not work well in macpro, but is working in linux.
- Dr. Cleaner, Battery Monitor, DjVu Reader
- Cheatsheet # Go to any app, press and hold to see keyboard shortcuts
- _Careful:_ hff5-view and fv-viewer (These gave problem with dmstack on pisces)

## QuickLook Plugins
- Collections of useful quick look plugins are given [here](https://github.com/sindresorhus/quick-look-plugins).
- Detail list of quick look plugins are given [here](http://www.quicklookplugins.com/).
- To look fitsfile we can use [QLfits](https://github.com/onekiloparsec/QLFits).
- [Rest Plugin](https://github.com/cluther/qlrest) does not work in MacOS High Sierra. It does not do anything.

## Format markdown in Mail etc
- Install this [Multimarkdown Installer](http://brettterpstra.com/2013/03/08/new-in-the-markdown-service-tools-in-place-markdown-to-rtf/).
- Copy these [Service Scripts](http://brettterpstra.com/projects/markdown-service-tools/) to `~/Library/Services`.
- Usage: Right click and select echo hello in new email. Right click, go to Services and convert markdown to rtf.


## Alfred
I have saved web search customization in a textfile.

## Show full path in Finder
- To see full path at bottom: `View > Show Path Bar`
- To see full path name at top: `defaults write com.apple.finder _FXShowPosixPathInTitle -bool true; killall Finder`

## Mac Settings
```
Terminal > Preferences # Red sands, courier new 24, vertical bar, disable VT100 and disable bells, window check most, text
System Preferences > Keyboard > Shortcuts > Services
System Preferences > Users and Groups > Login Items
Finder > Preferences 
Finder > View > Customize Toolbar
Dock settings
Time (from toolbar) > Open Date time preferences

```

## Useful aliases and functions
```bash
# File: ~/.bash_profile
alias sb='source ~/.bash_profile'
export PS1='\u@\[\e[0;34m\]\h:\[\e[0;31m\]\w\e[0m\n$ ' # Prompt Settings in terminal.
alias rm="echo Use 'del', or the full path i.e. '/bin/rm'"
function del () { mv  $@ ~/.Trash/; }
alias qlf='qlmanage -p "$1" > /dev/null 2>&1'
```

## Mac Malwares and Viruses
These are the viruses in Mac, If you see them, uninstall them.
1. Epolife
2. Jimbre
3. Friendlysocket

## Add spaces to dock
```
# One execution of first line gives one space, we can move this space in the dock.
defaults write com.apple.dock persistent-apps -array-add '{tile-data={}; tile-type="spacer-tile";}'
killall Dock
```

## Nofitications
```
# To display notifications in external monitor, enable it from system preferences
osascript -e 'display notification "Notification text" with title "Title"'
```


## My customized finder
![Finder Customized Toolbar](images/Finder_toolbar.png)

[pcloud]: https://www.pcloud.com/how-to-install-pcloud-drive-mac-os.html?download=mac
[time-out]: http://www.dejal.com/download/?prod=timeout&vers=2.4&rel=gen&lang=en&op=show&ref=timeout
