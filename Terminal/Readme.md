# Solarized Theme
Download the [solarized-theme](https://github.com/tomislav/osx-terminal.app-colors-solarized), right click to add the theme.
Then go the terminal settings and set it as the default terminal.

Download this [solarized terminal](https://raw.githubusercontent.com/tomislav/osx-terminal.app-colors-solarized/master/Solarized%20Dark.terminal).

# Prompt Settings (PS1)

```bash
## Terminal Prompt Settings
orange=$(tput setaf 166);
yellow=$(tput setaf 228);
green=$(tput setaf 71);
white=$(tput setaf 15);
bold=$(tput bold);
reset=$(tput sgr0);



PS1="\[${bold}\]\n";
PS1+="\[${orange}\]\u"; # username
PS1+="\[${white}\] at ";
PS1+="\[${yellow}\]\h"; # host
PS1+="\[${white}\] in ";
PS1+="\[${green}\]\w"; # Working directory
PS1+="\n";
PS1+="\[${white}\]\$ \[${reset}\]";
export PS1;
```

