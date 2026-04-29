import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title(" Finance Risk Intelligence Dashboard")

# INPUT PANEL

st.sidebar.header("🔍 Input Parameters")

quantity = st.sidebar.slider("Quantity", 1, 500, 10)
price = st.sidebar.slider("Unit Price", 1.0, 200.0, 2.5)
year = st.sidebar.selectbox("Year", [2010, 2011])
month = st.sidebar.slider("Month", 1, 12, 5)
quarter = st.sidebar.selectbox("Quarter", [1,2,3,4])
country = st.sidebar.selectbox("Country UK?", [0,1])

# API CALL
if st.sidebar.button("Predict Risk"):

    data = {
        "Quantity": quantity,
        "UnitPrice": price,
        "Year": year,
        "MonthNumber": month,
        "Quarter": quarter,
        "Country_United Kingdom": country
    }

    try:
        url = "http://13.51.204.143:5000/predict"   
        response = requests.post(url, json=data, timeout=5)
        result = response.json()

        col1, col2, col3 = st.columns(3)

        col1.metric("Risk Level", result["risk"])
        col2.metric("Confidence", result["confidence"])
        col3.metric("Prediction", result["prediction"])

    except:
        st.error("!! API not reachable. Make sure AWS server is running.")

# REAL DATA VISUALIZATION
st.header("📊 Business Insights")

# Load dataset
df = pd.read_csv("../data/BDA_SEM-4.csv")

# Feature Engineering
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["MonthNumber"] = df["InvoiceDate"].dt.month
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Revenue Trend
st.subheader("📈 Revenue Trend")

rev = df.groupby("MonthNumber")["Revenue"].sum()

fig1, ax1 = plt.subplots()
ax1.plot(rev.index, rev.values)
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue")
ax1.set_title("Monthly Revenue Trend")

st.pyplot(fig1)

# Country Analysis
st.subheader("🌍 Revenue by Country")

country_data = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots()
country_data.plot(kind='bar', ax=ax2)
ax2.set_title("Top Countries by Revenue")

st.pyplot(fig2)

# Risk Distribution
st.subheader("⚠️ Risk Distribution")

df["LossFlag"] = (df["Revenue"] < 0).astype(int)

risk = df["LossFlag"].value_counts()

fig3, ax3 = plt.subplots()
risk.plot(kind='pie', autopct='%1.1f%%', ax=ax3)
ax3.set_ylabel("")

st.pyplot(fig3)

# Correlation Heatmap
st.subheader("🔥 Feature Correlation")

corr = df.select_dtypes(include='number').corr()

fig4, ax4 = plt.subplots()
cax = ax4.imshow(corr)
fig4.colorbar(cax)

ax4.set_title("Correlation Heatmap")

st.pyplot(fig4)