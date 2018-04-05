# Using MacOS dictionary from terminal

- Write a python script `dict.py` and rename it `dict`.
- Make it executable `chmod +x dict`.
- Copy it to path `sudo cp dict /usr/local/bin/`.

## Dictionary Pop up
To use dictionary from terminal we can use `open dict://` command. 
```bash
open dict://oxymoron
open dict://"en route"
```

## We can also define a function in  `~/.bash_profile`.  
```bash
function define() { open dict://"$@";}
```
