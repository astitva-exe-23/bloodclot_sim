import pandas as pd
import numpy as np
import random
import time

# Function to generate realistic blood data
def generate_blood_data():
    # Normal distributions for healthy blood values
    platelet_count = int(np.random.normal(loc=250, scale=50))  # Mean=250, SD=50
    clotting_time = round(np.random.normal(loc=7, scale=1.5), 2)  # Mean=7 mins
    fibrinogen = int(np.random.normal(loc=300, scale=50))  # Mean=300 mg/dL
    d_dimer = round(np.random.normal(loc=0.5, scale=0.3), 2)  # Mean=0.5 µg/mL

    # Simulating anomalies (5% chance)
    anomaly = random.random() < 0.05  # 5% probability of an anomaly

    if anomaly:
        print("⚠️ Anomaly Detected! Generating abnormal values...")
        if random.choice(["platelet", "clotting", "fibrinogen", "d_dimer"]) == "platelet":
            platelet_count = random.randint(50, 100)  # Dangerously low
        elif random.choice(["clotting", "fibrinogen", "d_dimer"]) == "clotting":
            clotting_time = round(random.uniform(12, 20), 2)  # Too high
        elif random.choice(["fibrinogen", "d_dimer"]) == "fibrinogen":
            fibrinogen = random.randint(500, 700)  # Very high
        else:
            d_dimer = round(random.uniform(3.0, 6.0), 2)  # Severe clot risk

    return {
        "Timestamp": pd.Timestamp.now(),
        "Platelet Count (x10^3/µL)": max(50, min(platelet_count, 450)),  # Clip to valid range
        "Clotting Time (mins)": max(3, min(clotting_time, 20)),
        "Fibrinogen (mg/dL)": max(150, min(fibrinogen, 700)),
        "D-dimer (µg/mL)": max(0.1, min(d_dimer, 6.0)),
        "Anomaly": "Yes" if anomaly else "No"
    }

# Function to generate & append data periodically
def generate_csv(filename="blood_data.csv", interval=5, num_entries=10):
    for _ in range(num_entries):
        data = generate_blood_data()
        df = pd.DataFrame([data])
        df.to_csv(filename, mode="a", header=not pd.io.common.file_exists(filename), index=False)
        print(f"Generated Data: {data}")
        time.sleep(interval)

if __name__ == "__main__":
    generate_csv(interval=5, num_entries=10)
