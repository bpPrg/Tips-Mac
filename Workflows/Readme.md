This [merge pdf](https://jacobsalmela.com/2016/08/12/merge-pdfs-natively-with-a-right-click-in-os-x/) did not work in Yosemite (10.10) on pisces, but it is a good idea how to write shell script workflows in mac.

**Steps**
```
Automator > Services > choose
files or folders   and Finder.app

Search for get finder, then drag Get Selected Finder Items from the left pane into the right.

Next, search for script, drag Run Shell Script over.  Using the pulldown menus, 
choose /usr/bin/python for the Shell: and as arguments for Pass input:
```
