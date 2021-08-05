# Rename this file to whatever file is run on your board's boot.  Usually this
# is main.py

# Import any libraries you need for your specific porject.  For this project,
# we only need the neopixel and machine libraries to set up our NeoPixel strip.
import machine, neopixel
# You will also need to import any animations you are using.  Each animation will
# be it's own import statement.  Make sure you also copy the animator_base.py and
# any animation files over to your board.
from flash import Flash

# Set up your neopixel object.  This script uses a string of 32 NeoPixels on
# pin 2.
np = neopixel.NeoPixel(machine.Pin(2), 32)

# Create an animation object.  Only the animations you copied and imported are
# available.  The arguments differ for each animation.  In this case, Flash
# only takes the NeoPixel object and a color.  We will leave the period at the
# default.
anim = Flash(np, (125, 0, 255))

# Once your animation is created, you can control it with the start() and stop()
# functions.
anim.start()

# If an animation is left running, there seems to be issues uploading new code
# and accessing the REPL on some boards.  One work around is to wrap your main
# code in a try execpt and stop all animations in the except block.  This cleans
# up any running animations if new code is uploaded or a keyboard inturrupt is
# seen.
try:
    while(1):
        # Your main code will run while the animation updates in the background.
        # We aren't doing anything else so just loop forever.
        pass
except:
    anim.stop()
