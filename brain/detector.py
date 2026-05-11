import sys
import os
import numpy as np
from sklearn.ensemble import IsolationForest

# Ensure Python can see the main folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your safety laws
from core.config import VOLTAGE_MAX, VOLTAGE_MIN

class AuraBrain:
    def __init__(self):
        print("🧠 Booting Aura-Grid AI Core...")
        
        # 1. Create the Machine Learning Model
        # contamination=0.05 means we expect 5% of grid activity to be dangerous anomalies
        self.model = IsolationForest(contamination=0.05, random_state=42)
        
        # 2. Train the AI on "Normal" grid behavior (e.g., safe ranges between 210V and 245V)
        # In a real grid, this would be months of historical sensor data
        normal_data = np.random.uniform(210, 245, (500, 1))
        self.model.fit(normal_data)
        
        print("✅ AI Training Complete. Model is active.")

    def analyze_voltage(self, voltage):
        # Level 1: Hardware Safety Check (The old rules)
        if voltage >= VOLTAGE_MAX:
            return "🚨 HARDWARE ALERT: CRITICAL SURGE"
        elif voltage <= VOLTAGE_MIN:
            return "📉 HARDWARE ALERT: BROWNOUT"
            
        # Level 2: AI Anomaly Detection (The new brain)
        # We ask the AI to predict if this specific voltage looks "weird" compared to its training
        v_array = np.array([[voltage]])
        prediction = self.model.predict(v_array)
        
        # The AI returns -1 if it detects a dangerous anomaly, and 1 if it's safe
        if prediction[0] == -1:
            return "⚡ AI WARNING: UNSTABLE PATTERN DETECTED"
        else:
            return "✅ SYSTEM STABLE"

# Create the brain instance
ai_core = AuraBrain()

# This is the function your main.py calls
def check_grid(voltage):
    return ai_core.analyze_voltage(voltage)