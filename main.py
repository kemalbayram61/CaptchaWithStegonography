from imageParser import ParseProcess as pp
from stegonography import StegonographyProcess as sp
from homeScreen import HomeScreen as hm

pp=pp(9,0,"images/shoes.jpg")

frames=pp.getFrames(0)

hm=hm()
hm.createHomeScreen(frames)
