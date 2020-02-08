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
db_filter_time = .5

blink_led = False
blink_start_time = 0
blink_interval = .1

while True:
    print("soundVolume:", soundVolume.value, "triggerLevel:", triggerLevel.value, "db_filter:", db_filter)

    if soundVolume.value >= triggerLevel.value:
        if db_filter:
            db_start_time = time.monotonic()
        else:
            camera.value = True
            triggeredLed.value = True
            time.sleep(.5)
            camera.value = False
            blink_led = True
            db_start_time = time.monotonic()
            db_filter = True

    if db_filter:
        now = time.monotonic()
        if blink_led:
            if now - blink_start_time >= blink_interval:
                blink_start_time = now
                triggeredLed.value = not triggeredLed.value

        if (now - db_start_time) >= db_filter_time:
            db_filter = False
            triggeredLed.value = False
            blink_led = False
