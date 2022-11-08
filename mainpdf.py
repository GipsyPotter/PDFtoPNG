import argparse
import os

import fitz  # pip install PyMuPDF

parser = argparse.ArgumentParser(description="PDF to PNG convertor")

parser.add_argument(
    "-path",
    type=str,
    help="Your pdf file path"
)

parser.add_argument(
    "-name",
    type=str,
    help="Your image name"
)

arg = parser.parse_args()

pdffile = arg.path
namefile = arg.name
os.makedirs(f"C:\Desktop\Output{namefile}")
save = f'''C:\Desktop\Output{namefile}{chr(92)}'''
doc = fitz.open(pdffile)
i = 0
for page in doc:  # Total number of pages
    pix = page.get_pixmap()
    output = f"{save}{namefile}{page.number}.png"  # Name and path of your saving folder
    pix.save(output)
    print(f"Finish converting page {page.number}")
    i += 1
print(f"Finished converting total {i}pages successfully")
