## Testing the vibration motor

You're now going to need to test your soldering (or twisting).

- Twist the free ends of the multi-core wire so they become fairly rigid.

- Insert these ends into female-to-female jumper leads.

- Place the red lead onto the 3V3 output on your Raspberry Pi.

- Place the black lead onto any ground pin.

	![testing vibro](images/See_Like_A_Bat_Diagram_1.png)

It's important to note that you can only do this with this particular motor, as it has such a small current draw. Larger motors 	should never be attached directly to the pins on your Raspberry Pi, and should instead be attached to a motor driver or a transistor.

The motor should start vibrating, at which point you can disconnect it from your Raspberry Pi.

