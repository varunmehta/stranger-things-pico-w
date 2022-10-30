from time import sleep
# from machine import Pin
from random import randint
# from neopixel import NeoPixel

# import network

# shh! you should never publish your password online
SSID = 'iPhone'
PASSWORD = 'Hall0W33n'

# We are using 26 LEDs, each corresponding to an alphabet
LEDS = 26

# Data in Pin for WS2812
LEDS_PIN = 13

# Button GPIO pin to trigger LEDs when pressed
# BUTTON = Pin(23, Pin.IN)

# Default Message 
MESSAGE = 'You Shouldnt Have Upset Him'

## Do not edit these.
ASCII_START = 97
ASCII_END = 122
ASCII_SPACE = 32


def convert_ascii_to_numeric(message):
    # first convert to lower string
    message = message.lower()
    numeric_message = []

    for char in message:
        numeric_message.append(ord(char))

    return numeric_message


def contains_number(value):
    if True in [char.isdigit() for char in value]:
        return True
    return False


# We blink lights twice and stop
def blink_lights(npixel, message):
    print (message)
    numeric_message = convert_ascii_to_numeric(message)
    print(numeric_message)

    # run the message twice, configure this later, if you need to.
    for loc in numeric_message: 
        # if there is space in the ascii list
        if loc == ASCII_SPACE:
            sleep(1)

        location = loc - ASCII_START
        # make any random color!
        print(chr(loc) + ' - ' + str(location))
        led_color = (randint(0,244), randint(0,244), randint(0,244))
        print (led_color)
        # npixel[location] = led_color
        # npixel.write()
        sleep(0.5)

# Main Program 
print ('starting program...')

# initalize LEDs
# pixels = NeoPixel(LEDS_PIN, LEDS)
pixels = 'hello'

while True:
    # everytime the button is pressed, the blink lights sequence is triggered.
    # if BUTTON.value():
    for i in range(2):
        blink_lights(pixels, MESSAGE)
        # sleep 2 seconds before a re-run
        sleep(3)