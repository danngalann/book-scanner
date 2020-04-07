import cv2
from pyzbar.pyzbar import decode
import os


class BarcodeScanner:
    def __init__(self):
        self.ISBNs = []

    def getCodes():

        images = os.listdir('images')

        for image in images:
            image = cv2.imread("images/" + image)
            # vertical_third = round(len(image)/3) # Compute mid section for vertical images
            # roi = image[vertical_third:vertical_third*2] # Get ROI
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert ROI to grayscale

            # Find barcodes
            barcodes = decode(gray)

            for barcode in barcodes:
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type

                # Add code to ISBN list
                ISBNs.append(barcodeData)

                print(f"Found {barcodeType} containing: {barcodeData}")

        return ISBNs

# img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
# vertical_third = round(len(img)/3)
# roi = img[vertical_third:vertical_third*2] # Get ROI
# gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# _, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)

# Show the images
# cv2.imshow('origin', img)
# cv2.imshow('threshold', thresh)
# cv2.imshow('gray', gray)
# cv2.imshow('ROI', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()