# Financial Risk Intelligence Dashboard

## 📌 Project Overview

Financial Risk Intelligence Dashboard is a cloud-deployed machine learning system designed to analyze financial transaction data and predict product-level risk in real time.

The project combines:
- Machine Learning
- Flask Backend APIs
- Streamlit Interactive Dashboard
- AWS EC2 Cloud Deployment
- Nginx Reverse Proxy Architecture

The system categorizes products into:
- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

It also generates risk scores and provides interactive visual insights for financial analysis.

---

# 🚀 Key Features

- Real-time financial risk prediction
- Product-level risk classification
- Dynamic risk scoring system
- Interactive Streamlit dashboard
- Flask REST API integration
- AWS EC2 cloud deployment
- Nginx reverse proxy configuration
- Interactive charts and visual analytics
- Top risky product identification
- Alert generation for critical products

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning model |
| Flask | Backend API |
| Streamlit | Frontend dashboard |
| Plotly | Interactive charts |
| AWS EC2 | Cloud deployment |
| Nginx | Reverse proxy server |
| Pickle | Model serialization |

---

# 🧠 Machine Learning Workflow

## 1. Dataset Preprocessing
- Removed missing values
- Converted date columns
- Cleaned transaction data

## 2. Feature Engineering
Created features such as:
- Quantity
- Unit Price
- Year
- Month
- Quarter
- Revenue
- Total Amount

## 3. Model Training
Algorithm Used:
- Random Forest Classifier

Dataset Split:
- 80% Training
- 20% Testing

## 4. Risk Classification
Products are classified into:
- Low Risk
- Medium Risk
- High Risk

---

# 🌐 System Architecture

```text
User
 ↓
Streamlit Dashboard
 ↓
Flask API
 ↓
Machine Learning Logic
 ↓
Risk Prediction
 ↓
JSON Response
 ↓
Dashboard Visualizations
```

---

# 📂 Project Structure

```text
Financial_Risk_Analysis/
│
├── app/
│   └── app.py
│
├── dashboard/
│   └── dashboard.py
│
├── models/
│   ├── product_data.pkl
│   ├── risk_model.pkl
│   ├── imputer.pkl
│   └── columns.pkl
│
├── training/
│   └── BDA_Final_project.ipynb
│
├── test.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Backend API

## Flask API Endpoint

```text
POST /predict
```

### Example Input

```json
{
  "Quantity": 120,
  "UnitPrice": 150,
  "Year": 2011,
  "MonthNumber": 12,
  "Quarter": 4,
  "Country_United Kingdom": 1
}
```

### Example Output

```json
{
  "Low Risk": [],
  "Medium Risk": [],
  "High Risk": []
}
```

---

# 📊 Dashboard Features

The Streamlit dashboard provides:

- Risk distribution charts
- Product-wise risk scores
- Top risky product analysis
- Interactive bar charts
- Pie chart visualizations
- Histogram analysis
- Scatter plot clustering
- KPI metrics
- Critical risk alerts

---

# ☁️ AWS Deployment

The project is deployed on:
- AWS EC2
- Ubuntu Linux

Deployment Architecture:

| Service | Port |
|---|---|
| Flask Backend | 5000 |
| Streamlit Frontend | 8503 |
| Nginx | 80 |

Nginx acts as a reverse proxy server to connect frontend and backend through a single public endpoint.

---

# 🚀 How to Run the Project

## 1. Clone Repository

```bash
git clone <YOUR_GITHUB_LINK>
cd Financial_Risk_Analysis
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4. Run Flask Backend

```bash
cd app
python app.py
```

---

## 5. Run Streamlit Dashboard

```bash
cd dashboard
streamlit run dashboard.py --server.port 8503
```

---

# 📈 Sample Visualizations

- Risk Distribution Pie Chart
- Top High-Risk Products
- Risk Score Histogram
- Product Risk Scatter Plot
- Risk Comparison Charts

---

# 👨‍💻 Team Members

| Name | Role |
|---|---|
| Atharv Jambhule | ML, Backend, AWS Deployment, System Integration |
| Rushabh Kamdi | Dashboard UI & Visualizations |
| Ayush Joshi | Data Processing & Testing |
| Shrikant Karande | Deployment Support & Documentation |

---

# 🎯 Advantages

- Automated financial risk analysis
- Real-time prediction system
- Cloud-based deployment
- Scalable architecture
- Interactive business insights
- Production-style deployment workflow

---

# 🔮 Future Scope

- Fraud detection integration
- Deep learning models
- Docker container deployment
- Authentication system
- Real-time notification alerts
- Database integration

---

# 🎤 Viva Summary

> Financial Risk Intelligence Dashboard is a cloud-deployed machine learning system that predicts and visualizes product-level financial risk using Flask APIs, Streamlit dashboards, AWS EC2, and Nginx reverse proxy architecture.

---

# 📜 License

This project is developed for academic and educational purposes.

