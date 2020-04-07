from BarcodeScanner import BarcodeScanner
from ISBNTool import ISBNTool
import os

scanner = BarcodeScanner()
images = os.listdir("images")

# Loop through all the images in the images directory
for image in images:
  path = "images/" + image

  # Get the barcode (ISBN) of the image
  ISBN = scanner.getCode(path)
  print(ISBN)