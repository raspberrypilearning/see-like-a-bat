from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from time import sleep, time

trig = OutputDevice(17)
echo = InputDevice(4)
vibro = PWMOutputDevice(14)

sleep(2)

def get_pulse_time():
    trig.on()
    sleep(0.00001)
    trig.off()

    while echo.is_active == False:
        pulse_start = time()

    while echo.is_active == True:
        pulse_end = time()

    sleep(0.06)
    return pulse_end - pulse_start

def calculate_distance(duration):
    speed = 343
    distance = speed * duration / 2
    return distance

def indicate(distance):
    vibration = (((distance - 0.02) * -1) / (4 - 0.02)) + 1
    try:
        vibro.value = vibration
        print(distance)
    except:
        pass

for i in range(1000):
    duration = get_pulse_time()
    distance = calculate_distance(duration)
    indicate(distance)

trig.close()
echo.close()
vibro.close()
