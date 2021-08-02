# neopixel-animate
neopixel-animate is a small flexible micropython framework for easily creating
animations to run on neopixel arrays.  neopixel-animate has been tested to run on
the ESP8266 port of micropython and should run on other boards that support micropython.

## Getting Started
This project includes an Animator Base class and multiple animation classes that
add individual animations.  The Animator Base and animation files can be found in
the src directory.  Each animation is a separate python file.  This allows you to
save space on your device by only loading the animations you use.

### Loading files
TO get started, you will need to load animator_base.py and any animation files
you plan to use onto your device.  They should reside in the same directory as
your main python script.  Pushing files to your device can be done with whatever
tool you normally to move files to your micropython board (ex. Ampy).

### Using Animations
Using animations in your main script is easy.  Check out the examples directory for
specific animation examples.
1. Import the specific animation(s) you want to use in your script.
1. Initialize a NeoPixel Object.
1. Initialize a animation and pass it the NeoPixel object you created as well as
any other arguments.  The required arguments will differ slightly from one animation
to another.  Check the examples or documentation specific to the animation you
are trying to use.
1. To start the anmation call `start()` on the animation object you created.
1. To stop the animation call `stop()`.  The default behavior of the stop function
turns off all the LEDs.  To disable this behavior, pass a False to the 'clear' argument.

## Known Issues (READ THIS!)
### Running animations can interfere with file uploads
Due to the behavior of the timers used to update the animations in the background,
leaving animations running can cause reliability issues with file uploads and cause
difficulty accessing the REPL.  It is recommended that that you catch exceptions
and stop all running animations.  This allows file uploads to stop running animations
and allows the user to use Ctrl-C to access the REPL.  See the examples directory
for how this can be done.

## Creating New Animations
Coming Soon...
