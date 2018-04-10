# Using Alfred in Mac
- Alfred is a better alternative for Spotlight app. 
- We can search any files and websites easily using Alfred.

- Snippets, workflows, and syncing are not available in free version.

- We can install Alfred 3 from [official website](https://www.alfredapp.com/).

- For the usage we can take a look at [youtube video](https://www.youtube.com/watch?v=-UZ1mHknTiM).


## Convert aText snippets to alfredsnippets
To convert a simple aText snippets in a csv format without special fields we can use the python script
`convert-aText-to-Alfred.py`.

If we have multiple `.csv` files without `whitespace` in thier names we can run following command:
```bash
for f in *csv; do python convert-aText-to-Alfred.py $f; done;
mkdir csvfiles; mv *.csv csvfiles
mkdir alfredsnippets; mv *.alfredsnippets alfredsnippets
```
