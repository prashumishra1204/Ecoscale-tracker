# Ecoscale-tracker
# 🍃 EcoScale — Next-Gen AI Green DevOps Platform

<p align="center">
  <img src="https://shields.io" alt="Python">
  <img src="https://shields.io" alt="MySQL">
  <img src="https://shields.io" alt="Flask">
  <img src="https://shields.io" alt="Gemini AI">
  <img src="https://shields.io" alt="MIT License">
</p>

---

## 💻 About The Project

As global cloud infrastructure demands surge, tech enterprises face strict compliance mandates to reduce their digital carbon footprint. **EcoScale** is a real-time, future-proof **Sustainability Engineering & DevOps Dashboard** designed to solve this massive corporate hurdle. 

The platform spins up a multi-threaded background simulation engine to mimic active compute load logs across multi-region server clusters, persists transactional metrics into an optimized relational database, and orchestrates **Google Gemini AI reasoning models** to dynamically deliver automated cloud down-scaling optimization plans to systems administrators.

---

## 🚀 Key Features

*   **⚡ Real-Time Compute Simulation Engine:** Multi-threaded worker background task simulating live telemetry streams (CPU, RAM utilization) across distributed infrastructure layers.
*   **🍃 Environmental Mathematical Schemas:** Formulaic engines converting computing resource loads into active Carbon Intensity scores (grams of CO₂ / sec).
*   **📊 Dynamic Cyberpunk Telemetry UI:** High-fidelity dark mode terminal interface built with vanilla JavaScript, Tailwind CSS, and **Chart.js** to render real-time graphical performance timelines.
*   **🧠 AI Cloud Optimization Advisor:** Deep integration with the **Google Gemini API** (`gemini-2.5-flash`/`gemini-3.7-flash`) to audit transaction streams and output actionable server management strategies.
*   **🛡️ Production-Grade Error Mitigation:** Robust architecture equipped to catch relational access database failures, bypass API throttling, and handle high-traffic network bottlenecks safely.

---

## 🛠️ The Technology Architecture

| Layer | Technology | Primary Purpose |
| :--- | :--- | :--- |
| **Backend Core** | `Python 3` + `Flask Engine` | API routing logic, infrastructure management threads. |
| **Database Store** | `MySQL Relational Storage` | Transactional data persistence, high-performance tracking logs. |
| **Artificial Intelligence** | `Google Gemini API SDK` | Telemetry pattern analysis, carbon-reduction advisory compilation. |
| **Frontend Layout** | `Tailwind CSS` + `Vanilla JS` | Ultra-fast rendering framework, clean responsive layout views. |
| **Visual Charting** | `Chart.js Library` | Interactive canvas drawing, real-time metric plotting loops. |

---

## 📂 System File Hierarchy

```text
Ecoscale-tracker/
├── templates/
│   └── index.html      # Frontend Cyberpunk UI Dashboard & Client-Side Chart.js Logic
├── app.py              # Central Python API Server Engine & Background Logging Threads
├── schema.sql          # Core MySQL Relational Database Table Blueprints
├── .env                # Local Environment Properties Configuration (Hidden Security Variables)
└── README.md           # Professional Technical Repository Documentation
```

---

## 🛢️ Database Schema Model

The data collection pipelines feed runtime metrics cleanly inside an optimized database framework setup:

```sql
CREATE TABLE IF NOT EXISTS server_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    server_name VARCHAR(50) NOT NULL,
    cpu_usage FLOAT NOT NULL,
    ram_usage FLOAT NOT NULL,
    carbon_emitted FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📦 Local Installation & Cloud Environment Setup

### 1. Initialize System Infrastructure & Dependencies
Open your workspace terminal terminal environment and run the package management tools:
```bash
# Download, install, and turn on the internal relational database server
sudo apt-get update && sudo apt-get install -y mysql-server && sudo service mysql start

# Instantiate project database and link schema models
sudo mysql -e "CREATE DATABASE ecoscale;"
sudo mysql ecoscale < schema.sql

# Install Python backend dependencies
pip install flask mysql-connector-python google-genai python-dotenv
```

### 2. Configure Local Database Access Permissions
Open the MySQL administrative prompt console block:
```bash
sudo mysql
```
Execute these credential control properties variables line by line to authorize your Python backend:
```sql
CREATE USER 'ecouser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'EcoPassword123!';
GRANT ALL PRIVILEGES ON ecoscale.* TO 'ecouser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 3. Add Environment Security Variables
Create a local variable properties folder named `.env` in your root file tree and insert your Google API credentials:
```text
GEMINI_API_KEY=your_secret_google_ai_studio_api_key_here
```

### 4. Boot Up the Machine!
Relaunch the entire platform system framework using the primary script manager:
```bash
python app.py
```
Open up your local preview port `5000` inside your browser to view your dynamic data logging engine running instantly!

---

## 📜 Educational Project Disclaimer
This full-stack system is designed and engineered exclusively as an advanced, future-proof professional engineering portfolio project. It leverages mock-simulated resource data streams alongside real-time live third-party cloud API communication modules.
