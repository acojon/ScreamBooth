from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import time
import board

soundVolume = AnalogIn(board.A0)
triggerLevel = AnalogIn(board.A4)

camera = DigitalInOut(board.A3)
camera.direction = Direction.OUTPUT
camera.value = False

triggeredLed = DigitalInOut(board.A2)
triggeredLed.direction = Direction.OUTPUT
triggeredLed.value = False

db_filter = False
db_start_time = 0
db_filter_time = 1.0

blink_led = False
blink_start_time = 0
blink_interval = .1

while True:
    print("soundVolume:", soundVolume.value, "triggerLevel:", triggerLevel.value, "db_filter:", db_filter)

    # If the sound is greater than the trigger level, it's time to take a
    # picture!  Unless the dead band filter is active... if it's active, don't
    # take a picture. :)
    if soundVolume.value >= triggerLevel.value:
        if not db_filter:
            # Take a picture!
            camera.value = True
            triggeredLed.value = True
            time.sleep(.25)
            camera.value = False

            # Turn on the dead band filtering.
            blink_led = True
            db_start_time = time.monotonic()
            db_filter = True

    # If the deadband filter is active, there needs to be a way to exit the
    # filter and start responding to sound again.  Check to see if enough time
    # has passed that we can turn off the deadband filter. 
    if db_filter:

        now = time.monotonic()

        # Blink the led to let us know the deadband filter is active.
        if blink_led:
            if now - blink_start_time >= blink_interval:
                blink_start_time = now
                triggeredLed.value = not triggeredLed.value

        if (now - db_start_time) >= db_filter_time:
            db_filter = False
            triggeredLed.value = False
            blink_led = False
