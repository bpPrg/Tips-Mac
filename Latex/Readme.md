### Installing latex in MacOS OS X El Capitan
- By default there was no latex installation on my iMac.
- I tried installing Tex Live Utilities (it says no latexmk installation).
- I tried `brew install latexmk`  and `brew install latex-mk` both failed.

Finally I installed [mactex (2.9GB pkg file)](http://www.tug.org/mactex/mactex-download.html).
It gives latex command `latexmk`.

### Using Latex in Atom
- Install packages  `language-latex`, `latex`, `latexer` and `script`.

Clean Pattern for `latex` package.
```
**/*.aux, **/*.aux.bak, **/*.bbl, **/*.bcf, **/*.blg, **/*.dvi, **/*.fdb_latexmk, **/*.fls, **/*.idx, **/*.idx.bak, **/*.ilg, **/*.ind, **/*.lof, **/*.log, **/*.lol, **/*.lot, **/*.nav, **/*.out, **/*.snm, **/*.synctex.gz, **/*.toc, /**/_minted-{jobname}, /{output_dir}/sage-plots-for-{jobname}.tex, /missfont.log, /texput.log, /texput.aux, *.aux, *.acn, *.bbl, *.blg, *.fdb_latexmk, *.fls, *.glo, *.lof, *.log; *.lot, *.nav, *.out, *.snm, *.toc, *.xdy
```

Config.cson custom configuration for `atom-shell-commands` package.
```
  "atom-shell-commands":
    commands: [
      {
        name: "backup"
        command: "cp"
        arguments: [
          "{FileName}"
          "/Users/poudel/Dropbox/FileBackups/macpro_{FileNameNoExt}{FileExt}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-b"
      }
      {
        name: "2to3"
        command: "2to3"
        arguments: [
          "-w"
          "{FileName}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-t"
      }
      {
        name: "mpiexec"
        command: "mpiexec"
        arguments: [
          "-np"
          "4"
          "python"
          "{FileName}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "alt-i"
      }
      {
        name: "gcc"
        command: "gcc"
        arguments: [
          "-Wall"
          "{FileName}"
          "-o"
          "{FileNameNoExt}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-g"
      }
      {
        name: "gfortran"
        command: "gfortran"
        arguments: [
          "-Wall"
          "-L/System/Library/Frameworks/vecLib.framework"
          "-framework"
          "Accelerate"
          "{FileName}"
          "-o"
          "{FileNameNoExt}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-f"
      }
      {
        name: "execute"
        command: "{FileNameNoExt}"
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-e"
      }
      {
        name: "rm"
        command: "rm"
        arguments: [
          "-rf"
          "{FileNameNoExt}"
          ".DS_Store"
          "content.aux"
          "{FileNameNoExt}.aux"
          "{FileNameNoExt}.bbl"
          "{FileNameNoExt}.bcf"
          "{FileNameNoExt}.blg"
          "{FileNameNoExt}.dvi"
          "{FileNameNoExt}.fdb_latexmk"
          "{FileNameNoExt}.fls"
          "{FileNameNoExt}.lof"
          "{FileNameNoExt}.log"
          "{FileNameNoExt}.lol"
          "{FileNameNoExt}.lot"
          "{FileNameNoExt}.nav"
          "{FileNameNoExt}.out"
          "{FileNameNoExt}.run.xml"
          "{FileNameNoExt}.snm"
          "{FileNameNoExt}.toc"
          "{FileNameNoExt}.tex.backup"
          "{FileNameNoExt}.vrb"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-d"
      }
      {
        name: "latexmk"
        command: "latexmk"
        arguments: [
          "-pvc"
          "-f"
          "-pdf"
          "-quiet"
          "-latex=xelatex"
          "-quiet"
          "{FileName}"
        ]
        options:
          cwd: "{FileDir}"
          keymap: "ctrl-s ctrl-l"
      }
    ]
```
