import qrcode 

data = 'Vai Santos'

img = qrcode.make(data)

img.save('V:/Coding/Python/QRcode/myqrcode.png')
