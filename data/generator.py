import random
import time

def start_sensing():
    print("Aura-Grid: Monitoring Live Data...")
    while True:
        # Create a random voltage number
        voltage = round(random.uniform(220, 260), 2)
        print(f"Current Reading: {voltage}V")
        time.sleep(1) # Wait 1 second

if __name__ == "__main__":
    start_sensing()