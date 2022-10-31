from time import sleep
from machine import Pin
from random import randint
from neopixel import NeoPixel

import network

# shh! you should never publish your password online
SSID = 'iPhone'
PASSWORD = 'Hall0W33n'

# We are using 26 LEDs, each corresponding to an alphabet
LEDS = 30

# Data in Pin for WS2812
# LEDS_PIN = Pin(29, Pin.OUT)

# Button GPIO pin to trigger LEDs when pressed
# BUTTON = Pin(23, Pin.IN)

# Default Message
MESSAGE = 'You Shouldnt Have Upset Him'

# Do not edit these.
ASCII_START = 97
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
    print(message)
    numeric_message = convert_ascii_to_numeric(message)
    print(numeric_message)

    # run the message twice, configure this later, if you need to.
    for loc in numeric_message:
        # if there is space in the ascii list
        if loc == ASCII_SPACE:
            sleep(1)
            continue

        location = loc - ASCII_START
        # make any random color!
        print(chr(loc) + ' - ' + str(location))
        # led_color = (255,0,0)
        led_color = (randint(0, 244), randint(0, 244), randint(0, 244))
        print(led_color)
        npixel[location] = led_color
        npixel.write()
        sleep(0.9)
        npixel[location] = (0, 0 , 0)



# By default Wi-Fi is not available on start
def initalize_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    # Keep waiting for Wi-Fi, hopefully we have a connection in a few seconds
    while not wlan.isconnected() and wlan.status() >= 0:
        print("Waiting to connect:")
        sleep(1)


# Main Program
print('starting program...')

# MESSAGE = initalize_wifi()


# initalize LEDs
pixels = NeoPixel(Pin(0), LEDS)
# print(pixels)
# pixels.fill((0,0,255))
# pixels.write()
# sleep(2)
# pixels = 'hello'

print('done')

while True:
    # everytime the button is pressed, the blink lights sequence is triggered.
    # if BUTTON.value():
    for i in range(2):
        blink_lights(pixels, MESSAGE)
        # sleep 2 seconds before a re-run
        sleep(3)
