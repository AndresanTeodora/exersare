import random
import time

print("Aruncăm zarul...")
time.sleep(1) # Adaugă un pic de suspans

numar = random.randint(1, 6)

print(f"Ai dat un: {numar}!")

if numar == 6:
    print("Felicitări! Ai obținut punctajul maxim.")