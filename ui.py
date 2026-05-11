import sys
import os
import time
import random
import streamlit as st

# Tell Python where to find your AI Brain
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from brain.detector import check_grid

# 1. Setup the Web Page
st.set_page_config(page_title="Aura-Grid Dashboard", page_icon="⚡", layout="wide")
# --- Author Identification ---
# --- Author Identification ---
st.sidebar.title("👨‍💻 Project Lead")
st.sidebar.info(
    "**Name:** Likhith\n\n"
    "**Role:** Chief Architect & Lead Developer\n\n"
    "**Project:** 3rd Year EEE project: Aura-Grid"
)
st.sidebar.divider()
# -----------------------------

# --- Quick Intro Section ---
st.sidebar.subheader("📖 How it Works")
st.sidebar.markdown(
    "**Welcome to the Future of Grid Safety.**\n\n"
    "Traditional circuit breakers are *reactive*—they only trip **after** a dangerous voltage limit is crossed. "
    "By then, hardware damage may have already begun.\n\n"
    "**Aura-Grid is predictive.**\n\n"
    "Powered by an **Isolation Forest Machine Learning Algorithm**, this system constantly monitors the 'heartbeat' of the power lines. "
    "By training on historical safe data, the AI detects invisible micro-fluctuations and warns the grid of an impending failure *before* physical limits are breached.\n\n"
    "⚡ **Hardware Layer:** Strict physical limits (190V - 250V).\n\n"
    "🧠 **AI Layer:** Real-time anomaly prediction."
)
# -----------------------------

st.title("⚡ Aura-Grid: AI Command Center")
st.markdown("Monitoring live grid stability using Isolation Forest Machine Learning.")

# 2. Create Layout Boxes
col1, col2 = st.columns(2)
voltage_display = col1.empty()
status_display = col2.empty()

st.subheader("Live Voltage Waveform")
graph_display = st.empty()

# 3. Memory for the graph
if 'history' not in st.session_state:
    st.session_state.history = []

st.divider()

# 4. The Live Feed Loop
if st.button("▶ Start Live AI Monitoring"):
    while True:
        # Generate the fake sensor data
        voltage = round(random.uniform(210, 260), 2)
        
        # Ask the AI Brain
        status = check_grid(voltage)
        
        # Save to history for the graph (keep last 50 readings)
        st.session_state.history.append(voltage)
        if len(st.session_state.history) > 50:
            st.session_state.history.pop(0)
            
        # Update the Web UI dynamically
        voltage_display.metric("Current Grid Load", f"{voltage} V")
        
        # This makes the dashboard react with professional colors
        if "🚨" in status:
            status_display.error(status)   # Turns RED for Hardware Danger
        elif "⚡" in status:
            status_display.warning(status) # Turns YELLOW for AI Predictions
        else:
            status_display.success(status) # Turns GREEN for Stable Grid
            
        graph_display.line_chart(st.session_state.history)
        
        # Wait half a second
        time.sleep(0.5)


