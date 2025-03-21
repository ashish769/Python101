#pip install qrcode 
import qrcode
# qr=qrcode.make("https://www.facebook.com/sujan.thadarai")
# qr.save("sujan.png")

qr=qrcode.QRCode(version=1,box_size=120,border=3)
qr.add_data("https://www.facebook.com/sujan.thadarai")
qr.make(fit=True)
q=qr.make_image(fill_color="red",back_color="white")
q.save("ram.png")