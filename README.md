# ⚡ Aura-Grid: Autonomous Predictive Infrastructure Monitoring
> **Architecting the Next Generation of Smart Grid Stability through Unsupervised Machine Learning.**

---

## 🌐 The Problem & The Solution
Traditional grid protection is **reactive**—it only acts *after* a failure. **Aura-Grid** is **proactive**. By analyzing the "Digital Heartbeat" of power systems, it identifies microscopic precursors to failure, allowing for intervention *before* a blackout occurs.

### 🛡️ Dual-Layer Defense Architecture
1.  **The Deterministic Layer:** Hard-coded safety triggers (190V - 250V) for immediate hardware protection.
2.  **The Cognitive Layer:** An Unsupervised **Isolation Forest** ML model that detects anomalies even when voltage is within "safe" bounds.

---

## 🧠 Core Intelligence: The AI Engine
The "Brain" of Aura-Grid utilizes the **Isolation Forest** algorithm to map the normal distribution of grid behavior.

| Parameter | Specification | Purpose |
| :--- | :--- | :--- |
| **Algorithm** | `sklearn.ensemble.IsolationForest` | Anomaly isolation via recursive partitioning. |
| **Logic Type** | Unsupervised Learning | Learns "Normalcy" without requiring labeled fault data. |
| **Contamination** | `0.05` | Optimized to flag the top 5% of highest-risk variances. |
| **Alert Trigger** | Decision Path Analysis | If a point is "easily isolated," a **Predictive Warning** is issued. |

---

## 🏗️ System Architecture & Modular Design
Developed with strict **Separation of Concerns (SoC)** to ensure industrial-grade reliability.

```text
AURA_GRID/
├── 🧠 app/brain/         # AI CORE: ML Model training & Inference
├── ⚙️ app/core/          # FIRMWARE: Static safety laws & Hardware config
├── 📊 app/data/          # TELEMETRY: Real-time sensor simulation
├── 🖥️ ui.py              # COMMAND CENTER: Streamlit dashboard & live graphing
└── 🚀 main.py            # ENGINE: The system's central execution CLI
