## Wiring the UDS

The next stage is to set up and test the UDS. This is best done with the Raspberry Pi switched off, as you're about to use 5V, and if you accidentally short the Pi, you might have issues.

- Start by connecting the 5V pin on the Pi into the VCC pin on the UDS.
- The Trig pin on the UDS can go straight into GPIO 4.
- The Echo pin on the UDS needs to go to your first resistor of the potential divider.
- The output of the first resistor of the potential divider needs to go into GPIO 17.
- The Gnd from the UDS can go into any ground pin on the Raspberry Pi.

The diagram below shows you the complete setup:

![breadboard UDS](images/See_Like_A_Bat_Diagram_5.png)

