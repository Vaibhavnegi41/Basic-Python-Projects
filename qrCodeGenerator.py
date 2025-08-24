import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)  

qr.add_data("https://github.com/Vaibhavnegi41")

qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="blue") #used for changing the color of the QR

img.save("vaibhav_github.png")

# img=qr.make("https://github.com/Vaibhavnegi41") #converting the link into the qrcode

# img.save("vaibhav_github.png") #used to save the file with the .png extension ,always save in that extension