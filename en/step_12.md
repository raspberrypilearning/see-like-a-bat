## Making it more durable

- The first thing to do is to solder the pair of resistors together, and then add female jumper leads to each end of the pair. Add tape or heat-shrink to secure and insulate the joins:

	![joined resistors](images/joined_resistors.jpg)

- Next, add a third female header lead to the join between the two resistors. This can then be taped up as well:

    ![t join](images/t_join.jpg)

	1. The lead that joins to the smaller of the two resistors needs to go into the Echo pin on the UDS.
	1. The lead that branches out from between the resistors must go into GPIO 17
	1. The lead that comes out of the larger of the two resistors must go into a ground pin on the Raspberry Pi.
	1. All the other connections are the same as the previous setup.


- Header leads also need to be attached to the vibration motor:

    ![vibro with headers](images/vibration_motor_with_jumpers.jpg)

- Lastly, you can connect it all to either your Raspberry Pi or, even better, to a Pi Zero:

	![pizero setup](images/pizero_setup.jpg)

This wiring diagram may help you:

![pizero wiring](images/See_Like_A_Bat_Diagram_7.png)

Run your `bat.py` script to test that everything is working correctly. If it's not working as expected, have a look at the debugging section in the [previous worksheet](worksheet.md).

