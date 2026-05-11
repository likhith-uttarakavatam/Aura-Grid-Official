# ⚡ Aura-Grid: Predictive AI Grid Monitoring System

Aura-Grid is a world-first, AI-powered infrastructure monitoring system designed to detect power grid anomalies before catastrophic hardware failures occur. 

Unlike traditional circuit breakers that act reactively to static voltage limits, Aura-Grid utilizes Machine Learning (Isolation Forest) to learn the "heartbeat" of a stable power grid, identifying micro-fluctuations and dangerous patterns in real-time.

## 🚀 Key Features
* **Dual-Layer Safety Architecture:** * *Hardware Layer:* Strict rule-based triggers for absolute maximum (250V) and minimum (190V) thresholds.
  * *Predictive AI Layer:* Machine Learning pattern recognition to detect instability within "safe" bounds.
* **Real-Time Data Processing:** Continuous ingestion and evaluation of simulated sensor data.
* **Command Center Dashboard:** A live, interactive Streamlit frontend featuring real-time waveform graphing and dynamic alert states.

## 🧠 The AI Engine: Isolation Forest
At the core of `app/brain/detector.py` lies an Unsupervised Machine Learning model. 
* **Algorithm:** `sklearn.ensemble.IsolationForest`
* **Contamination Rate:** `0.05` (Tuned to expect 5% anomaly variance).
* **How it works:** The model is pre-trained on a matrix of stable grid data. Live sensor readings are then mapped against this normal distribution. If a reading requires too few "splits" to isolate, it is flagged as an anomaly (`-1`), triggering an immediate **AI WARNING** before physical limits are breached.

## 📂 System Architecture
The backend is highly modular, following professional separation of concerns:

AURA_GRID/
│
├── app/
│   ├── brain/
│   │   └── detector.py    # The Machine Learning Logic & AI Core
│   ├── core/
│   │   └── config.py      # Immutable safety laws and static hardware limits
│   └── data/
│       └── generator.py   # Sensor simulation bridging
│
├── main.py                # Command Line Interface (CLI) Engine
├── ui.py                  # Streamlit Web Dashboard Frontend
└── README.md              # Project Documentation

---

## 👨‍💻 Lead Architect & Creator
* **[LIKHITH]** - *Project Head & Full-Stack Developer*
* **Institution:** [Maharaj Vijayaram Gajapathi Raj College of Engineering]
* **Role:** Designed the hardware bridge, developed the Isolation Forest AI, and built the Streamlit command center.