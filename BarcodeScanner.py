import cv2
from pyzbar.pyzbar import decode
import os


class BarcodeScanner:

    def getCode(self, image):

        image = cv2.imread(image)
        # vertical_third = round(len(image)/3) # Compute mid section for vertical images
        # roi = image[vertical_third:vertical_third*2] # Get ROI
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert ROI to grayscale

        # Find barcodes
        barcodes = decode(gray)
        
        # Retrieve and return first barcode
        barcodeData = barcodes[0].data.decode("utf-8")       

        return barcodeData

cv2.waitKey(0)
cv2.destroyAllWindows()