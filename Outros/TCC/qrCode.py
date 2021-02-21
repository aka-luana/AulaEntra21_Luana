import qrcode
import image

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

data = 'Gerando QR Code pra turma :D'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
img.save('QRPython.png')