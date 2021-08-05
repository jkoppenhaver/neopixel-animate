import machine, neopixel, uos

from alternate import Alternate
from chase import Chase
from fill import Fill
from flash import Flash
from sine import Sine

def alternate_setup(np, color):
    return Alternate(np, color, period=0.5)

def chase_setup(np, color):
    return Chase(np, color, width=3)

def fill_setup(np, color):
    return Fill(np, color, period=0.07)

def flash_setup(np, color):
    return Flash(np, color, period=0.5)

def sine_setup(np, color):
    return Sine(np, color, period=6)

colors = [
    (127, 0, 0),
    (0, 127, 0),
    (0, 0, 127),
    (75, 75, 0),
    (0, 75, 75),
    (75, 0, 75)
    ]

animation_gen = [alternate_setup, chase_setup, fill_setup, flash_setup, sine_setup]

np = neopixel.NeoPixel(machine.Pin(2), 32)

rand_num = int.from_bytes(uos.urandom(1), 'big')

color = colors[(rand_num >> 4) % len(colors)]
animation = animation_gen[rand_num % len(animation_gen)](np, color)

animation.start()
try:
    while(1):
        pass
except:
    animation.stop()
