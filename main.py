import random
import time

print("Smart Solar Inverter System Started...\n")

while True:
    # Simulated data
    battery = random.randint(20, 100)
    solar_power = random.randint(0, 1000)
    load = random.randint(100, 800)

    # Display data
    print(f" Battery Level: {battery}%")
    print(f" Solar Power: {solar_power} W")
    print(f" Load Usage: {load} W")

    # Alert condition
    if battery < 30:
        print(" Warning: Low Battery!")

    print("-" * 30)

    # Wait for 3 seconds
    time.sleep(3)
