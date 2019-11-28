## How an ultrasonic distance sensor (UDS) works

An ultrasonic distance sensor (UDS) works using ultrasound. This is sound with a frequency so high that humans are unable to hear it. Bats and dolphins would have no problems though, as they have evolved to be able to use sounds of this frequency.

The ultrasonic distance sensor works by sending out a burst of ultrasound. This sound will travel through air, but reflect back (echo) off hard surfaces. The sensor can detect the echo, when it returns.

![uds](images/Ultrasonic_Distance_Sensor.png)

By knowing the time between the outgoing burst and returning echo, and the speed of sound, you can calculate how far an object is away from the sensor.

A UDS has 4 pins:

1. Vcc is the pin that powers the device. It needs 5V to work.
2. Trig is the pin that sends out the burst. It can be triggered using 3.3V.
3. Echo is the pin that outputs when the reflected sound is received. It outputs at 5V.
4. Gnd is the ground pin, used to complete the circuit.


Here we have a problem. The echo pin is going to output 5V, but your Raspberry Pi can only receive a maximum of 3.3V through any of the GPIO pins. So in order not to fry the Pi, you're going to have to reduce that output voltage.

