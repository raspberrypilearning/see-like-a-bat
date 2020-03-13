## Αντιμετώπιση σφαλμάτων του σεναρίου σου

Υπάρχουν μερικοί λόγοι για τους οποίους ενδέχεται να αντιμετωπίσεις σφάλματα με το σενάριό σου:

- Η συνάρτηση ` get_pulse_time ` μπορεί να αποτύχει περιστασιακά λόγω προβλημάτων με τον κύκλο σκανδαλισμού και ηχούς στον υπερηχητικό αισθητήρα απόστασης. Ίσως θελήσεις να το αλλάξεις για να χειριστείς αυτά τα ζητήματα, χρησιμοποιώντας ένα ` try / exception ` για να πιάσεις μία από τις μεταβλητές που δεν αποθηκεύονται:

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

- Η μέγιστη εμβέλεια στον UDS ενδέχεται να μην φθάνει τα 4 μέτρα. Αυτός που χρησιμοποιήθηκε για τη σύνταξη αυτού του πόρου δεν ξεπέρασε τα 2 μέτρα. Μπορείς να αλλάξεις την συνάρτηση ` calculate_vibration ` για να χρησιμοποιήσεις διαφορετικό μέγιστο αν θέλεις. Για παράδειγμα:

    ```python
    def calculate_vibration(distance):
        vibration = (((distance - 0.02) * -1) / (2 - 0.02)) + 1
        print(vibration)
        return vibration
    ```

- Περιστασιακά, ένας αριθμός ο οποίος δεν μπορεί να χειριστεί το PWMOutputDevice μπορεί να επιστραφεί από την συνάρτηση ` calculate_vibration `. Άλλο ένα `try/except` στον τελικό βρόχο θα χειριστεί αυτό:

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

