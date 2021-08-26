import pyqrcode 
import png
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "t.me/coderbuzz"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file 
url.png("mytelegram.png", scale = 8)
