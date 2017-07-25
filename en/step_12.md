## Debugging your script

There are a few reasons you might encounter errors with your script:

- The `get_pulse_time` function can occasionally fail due to problems with the cycle of trigger and echo on the ultrasonic distance sensor. You might like to change it to handle these issues, by using a `try/except` to catch either of the variables not being stored:

	```python
	def get_pulse_time():
		trig.on()
		sleep(0.00001)
		trig.off()

		while echo.is_active == False:
			pulse_start = time()

		while echo.is_active == True:
			pulse_end = time()

		sleep(0.06)

		try:
			return pulse_end - pulse_start
		except:
			return 0.02
    ```

- The maximum range on the UDS might not reach 4m. The one used in writing this resource never went beyond 2m. You can alter the `calculate_vibration` function to use a different maximum if you like. For instance:

	```python
	def calculate_vibration(distance):
		vibration = (((distance - 0.02) * -1) / (2 - 0.02)) + 1
		print(vibration)
		return vibration
	```

- Occasionally, a number that the PWMOutputDevice can't handle might be returned by the `calculate_vibration` function. Another `try/except` in the final loop will handle this:

   ```python
   while True:
	   duration = get_pulse_time()
	   distance = calculate_distance(duration)
	   vibration = calculate_vibration(distance)
	   try:
		   motor.value = vibration
	   except:
		   pass

   ``` 

