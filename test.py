import stepic
from PIL import Image

im=Image.open("frames/f1.png")

im1 = stepic.encode(im,b"kaobkaob")
im1.save("frames/f1.png", 'PNG')

im=Image.open("frames/f1.png")

message=stepic.decode(im)
print(message)