import cv2
import os
import numpy as np

zbar_library_path = "C:\\Users\\rahul\\AppData\\Roaming\\Python\\Python38\\site-packages\\pyzbar\\__init__.py"
os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "C:\\path\\to\\libiconv.dll;C:\\path\\to\\libzbar-64.dll"

from pyzbar.pyzbar import decode

img = cv2.imread("qrcode.jpg")
code = decode(img)
print(code)




