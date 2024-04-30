import pyqrcode as pyq

url = input("Enter url to generate qr code: ")

qr = pyq.create(url)

qr.svg('qrcode.svg',scale=7)
print('qrcode.svg')