# QR Code

import pyqrcode

import png

from pyqrcode import QRCode

QRstring = 'https://www.linkedin.com/in/sandeep-sharma-00389755/'

url = pyqrcode.create(QRstring)

url.png('Desktop\\qr.png', scale = 9)