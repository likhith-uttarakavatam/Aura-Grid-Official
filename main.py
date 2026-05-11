import sys
import os

# Add the current directory to Python's memory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Removed "app." from this line!
from brain.detector import check_grid
import random
import time

print("--- AURA-GRID SAFETY SYSTEM ACTIVE ---")
print("--- AURA-GRID SAFETY SYSTEM ACTIVE ---")
print("--- Designed & Engineered by: LIKHITH ---")

while True:
    voltage = round(random.uniform(180, 270), 2)
    result = check_grid(voltage)
    print(f"Reading: {voltage}V | {result}")
    time.sleep(0.8)