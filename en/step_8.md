## Testing the UDS

You now need to make sure the UDS is working correctly. You'll need a little bit of Python 3 code to do this, so open up IDLE and create a new file called `bat.py`.

- You're going to use GPIO Zero to code this, but the UDS isn't in the library yet. Not to worry though: you can use the default InputDevice and OutputDevice instead:

	```python
	from gpiozero import InputDevice, OutputDevice
	from time import sleep, time
	```

- Next, you can set up the trigger and echo pins of the distance sensor:

	```python
	trig = OutputDevice(4)
	echo = InputDevice(17)

    sleep(2)
	```

	The `sleep(2)` is there to let the sensor settle itself when the program starts.

- You can create a function to send and receive a pulse next. The first thing to do is set the trigger pin to send out a burst of ultrasound for 10μs:

	```python
	def get_pulse_time():
	   trig.on()
	   sleep(0.00001)
	   trig.off()
	```
	
- As soon as the ultrasonic sensor has sent out a burst of sound, the echo pin is set to `high`. You can use a `while` loop to detect when this happens and then record the current time:

	```python
		while echo.is_active == False:
			pulse_start = time()

	```

- When an echo is received, the echo pin is set to `low`. Another `while` loop will be able to record the time at which it happens:

	```python
		while echo.is_active == True:
			pulse_end = time()

	```

- Next, you need to let the ultrasonic sleep for a little bit, and then return the length of time it took for the pulse to be sent and received:

	```python
		sleep(0.06)

		return pulse_end - pulse_start
	```
	
- To finish off you can test the program by running it and then typing the following in the interpreter:

	```python
	print(get_pulse_time())

	```

Try typing it when your hand is close to and far from the distance sensor. You should get smaller values as your hand approaches the sensor.

