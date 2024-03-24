#using of the oficial lib qrcode from the python repository, that responsible for receiving a set of instructions and generating a cqrcode  
import qrcode

img = qrcode.make('Hello, world!')
print('=====',type(img))  # qrcode.image.pil.PilImage
img.save("some_file.png")