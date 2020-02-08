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
            triggeredLed.value = False
            db_start_time = time.monotonic()
            db_filter = True

    if db_filter:
        print ("In db_filter")
        now = time.monotonic()
        print ("now:", now)
        print ("db_start_time:", db_start_time)
        print (now - db_start_time)
        if (now - db_start_time) >= db_filter_time:
            db_filter = False

    # time.sleep(0.1)