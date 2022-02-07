import qrcode

link = input(r"insert a link, phone number, email or a value to make it itno a QrCode. Use (\n) for new line:  ")

out = link.replace(r'\n', '\n')

qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)

qr.add_data(out)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')

print(link)
print(out)
