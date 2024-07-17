import os
from colorama import Fore, Back, Style
import fitz  # pip install PyMuPDF
import io
from PIL import Image

print("PDF to PNG converter")
pdffile = input("Enter PDF file path: ")
namefile = input("Enter saving name of the file: ")
zoom = int(input("Enter zoom level (1-10, Default is 2): "))
# Setting default zoom level
if not zoom:
    zoom = 2
elif zoom > 10:
    zoom = 10
elif zoom < 1:
    zoom = 1

# Setting default saving path
if ":" not in namefile:
    save = f"C:\Desktop\\{namefile}\\"  # change the path to your desktop
else:
    save = f"{namefile}\\"
os.makedirs(save)

doc = fitz.open(pdffile)
i = 0
mat = fitz.Matrix(zoom, zoom)

# Loop through all pages --- updated due to attribute error
for page in doc:
    pix = page.get_pixmap(matrix=mat)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    output = f"{save}{namefile}_{page.number}.png"
    img.save(output)
    print(f"Finish converting page {page.number}")
    i += 1
print(f"{Fore.GREEN}Finish converting{Fore.BLUE} {i} {Style.RESET_ALL}{Fore.GREEN}pages{Style.RESET_ALL}")
