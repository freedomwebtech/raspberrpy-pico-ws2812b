import board
import neopixel
import time
 
 
np = neopixel.NeoPixel(board.GP0, 60)
np.brightness = 0.5
    


while True:
    for i in range (60):
      np[i]=(100,0,0)
      np.show()
      time.sleep(0.1)
      np[i]=(0,0,0)
      np.show()
    for i in range(59,0,-1): 
      np[i]=(0,0,255)
      np.show()
      time.sleep(0.1)
      np[i]=(0,0,0)
      np.show()
