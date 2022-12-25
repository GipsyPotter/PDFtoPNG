# PDF to PNG converter
This python program help you easily convert pdf file to png image

#This project is being rewriten for ease of use
## Installation

### Requirements
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required lib
```bash
pip install argparse
```
### Usage
1st step: use pyinstaller to pack the python file to exe file
```bash
pyinstaller -F mainpdf.py
```
2nd step: use the exe file to convert pdf file to png image
```bash
cd [path of exe file]
mainpdf.exe -path [path of pdf file] -name [name of pdf file]
```

## Note

This program will automaticlly create a folder on your Desktop and save all files there
## License

[MIT](https://choosealicense.com/licenses/mit/)
