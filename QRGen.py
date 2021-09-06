import qrcode

link = input("Enter an URL: ")

qr = qrcode.QRCode(version = 3, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=25, border = 2,)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color = "black", back_color = "white")

for c in ['\"', '/', ':', '.']:
    if c in link:
        link = link.replace(c, '')

link = "qrcodes\\" + link + '.png'
img.save(link)
