## Calculating the distance

There's a simple formula for calculating the distance the sensor is from an object. You can start off with the speed equation:

![speed](images/speed.png)

This can be rearranged to make:

![distance](images/distance.png)

But you need to remember that as the sound has to travel to the object and back again, we need to divide the calculated distance by 2. Therefore:

![distance final](images/distance2.png)

The speed of sound in air will vary depending on the temperature and air pressure, but it tends to hover around 343ms<sup>-1</sup>.

We can write a simple Python function to calculate this for us:

```python
def calculate_distance(duration):
    speed = 343
    distance = speed * duration / 2 # calculate distance in metres
    return distance
```
		
To test everything is working, we can add an infinite loop at the bottom of the script. Your full code listing should now look like this:

```python
from gpiozero import InputDevice, OutputDevice
from time import sleep, time

trig = OutputDevice(4)
echo = InputDevice(17)

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

while True:
	duration = get_pulse_time()
	distance = calculate_distance(duration)
	print(distance)
```
Run your code and you should see a stream of numbers, showing you the distance from the sensor in metres. Move your hand closer to and further from the distance sensor.

