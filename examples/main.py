import machine, neopixel
from flash import Flash

np = neopixel.NeoPixel(machine.Pin(2), 24)

anim = Flash(np, (125, 0, 255))
anim.start()
try:
    while(1):
        pass
except:
    anim.stop()
