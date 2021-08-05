# Using Animations
### Jump to a Specific Animation
- [Bare Minimum](#Bare-Minimum)
- [Flash](#Flash)
- [Sine](#Sine)
- [Alternate](#Alternate)
- [Chase](#Chase)
- [Fill](#Fill)

### Common (The Base)
These functions are included in the Animator Base so they can be called on all animations.
These functions are used to control animations.

*start()* - This function starts playing the animation on the np object that was
passed to the animation when it was instantiated.

*stop()* - This function stops the animation.  By default, this function will turn
off all LEDs after stopping the animation.  If you want to leave the LEDs in
whatever state they were in when the stop function is called, pass
`clear=False` as an argument to this function.

## Animations
Below  is the documentation for all of the different animations.  Each entry includes
a the type of NeoPixel arrangement that the animation was designed for, a short
description of the animation, and the arguments that can be used to configure the
animation when you create it.
### Bare Minimum
**Type:** None  
**Desc:** This animation does nothing and should not be used.  It is meant as a
template to give a starting point for creating new animations.

### Flash
**Type:** Any  
**Desc:** All LEDs turn on one color and then turn off.  
**Arguments:**  
  *np* - The NeoPixel object the animation should be displayed on  
  *color* - The color as a tuple that should be used for the animation  
   *period (Optional, Default=1)* - The time (in seconds) the LEDs flash on for

### Sine
**Type:** Any  
**Desc:** All LEDs start a single color at half brightness and follow an approximated
sine wave to full brightness, then to off, and back to half brightness before repeating.  
**Arguments:**  
  *np* - The NeoPixel object the animation should be displayed on  
  *color* - The color as a tuple that should be used for the animation  
  *period (Optional, Default=5)* - The time (in seconds) for one full cycle
  (half->full->off->half) to complete

### Alternate
**Type:** Any  
**Desc:** Turns all even index LEDs a given color and all odd index LEDs off, then
alternates the LEDs every period.
**Arguments:**  
  *np* - The NeoPixel object the animation should be displayed on  
  *color* - The color as a tuple that should be used for the animation  
  *period (Optional, Default=1)* - The time (in seconds) each state is shown

### Chase
**Type:** Linear, Ring  
**Desc:** A group of LEDs the given color travel down the line in order and
loop back to the beginning when they reach the end.
**Arguments:**  
  *np* - The NeoPixel object the animation should be displayed on  
  *color* - The color as a tuple that should be used for the animation  
  *width (Optional, Default=1)* - Number of LEDs that are on at one time  
  *period (Optional, Default=0.1)* - The time (in seconds) between each movement
of the group

### Fill
**Type:** Linear, Ring  
**Desc:** The LEDs turn on one by one in order.  Once all LEDs are on, the LEDs
turn off one by one starting back at the beginning.
**Arguments:**  
  *np* - The NeoPixel object the animation should be displayed on  
  *color* - The color as a tuple that should be used for the animation  
  *period (Optional, Default=0.1)* - The time (in seconds) between each LED is changed
