import qrcode


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
#Input text to generate QR Code for
qr.add_data('https://deadline.com/wp-content/uploads/2021/06/TedCropped.png?w=521&h=315&crop=1')

qr.make(fit=True)
img = qr.make_image()

#File name to save QR code image
img.save("Projects.Python.png")
