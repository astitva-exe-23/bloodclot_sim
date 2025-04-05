# 🩸 Blood Clot Risk Monitor

A real-time health monitoring system that simulates and visualizes blood data to predict the risk of blood clots using machine learning, to simulate the hardware working for the same. The system includes a data generator, a Flask backend, and a live Chart.js dashboard on the frontend.
![image](https://github.com/user-attachments/assets/aee8d974-02b3-4dce-b8b0-b151c0c92dfc)
![Cool Borwo](https://github.com/user-attachments/assets/46178507-e067-4572-b499-29a870960522)


---

## 🚀 Features

- 🔬 Simulates realistic blood metrics: Platelet Count, Clotting Time, Fibrinogen, and D-Dimer
- 📈 Real-time chart with Chart.js
- 🧠 Risk prediction using a machine learning model (`llm_handler`)
- ⚠️ Anomaly detection in blood parameters
- 🌐 Clean frontend with live data updates every 5 seconds
- 🔘 Start scan button to trigger data generation

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Pandas
- **Frontend:** HTML, JavaScript, Chart.js
- **ML Module:** Custom `predict_risk` logic in `llm_handler.py` using Gemini LLM.
- **Utilities:** dotenv, CORS
- **Data:** Simulated CSV blood data

---


