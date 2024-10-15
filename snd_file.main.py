import cv2
import os
from pyzbar.pyzbar import decode

# Set the path to the directory containing the DLL files
dll_directory = "C:\\Users\\rahul\\AppData\\Roaming\\Python\\Python38\\site-packages\\pyzbar\\__init__.py"

# Set the environment variable to include the directory containing the DLL files
os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = dll_directory

# Load the image
img = cv2.imread("qrcode.jpg")

# Decode the QR code
codes = decode(img)

# Print the decoded data
for code in codes:
    print("QR Code data:", code.data.decode("utf-8"))
