import streamlit as st
import requests
import plotly.express as px

st.set_page_config(layout="wide")

st.title("💰 Financial Risk Intelligence Dashboard")

# -------------------- INPUTS --------------------
st.sidebar.header("🔍 Input Parameters")

quantity = st.sidebar.slider("Quantity", 1, 500, 50)
price = st.sidebar.slider("Unit Price", 1.0, 200.0, 20.0)
year = st.sidebar.selectbox("Year", [2010, 2011])
month = st.sidebar.slider("Month", 1, 12, 6)
quarter = st.sidebar.selectbox("Quarter", [1, 2, 3, 4])
country = st.sidebar.selectbox("Country UK?", [0, 1])

# 🔗 YOUR API URL
url = "http://56.228.42.177/api/predict"
# -------------------- BUTTON --------------------
if st.sidebar.button("Analyze Products"):

    data = {
        "Quantity": quantity,
        "UnitPrice": price,
        "Year": year,
        "MonthNumber": month,
        "Quarter": quarter,
        "Country_United Kingdom": country
    }

    try:
        response = requests.post(url, json=data)

        if response.status_code != 200:
            st.error(f"API Error: {response.text}")
        else:
            result = response.json()

            st.success("Analysis Complete 🚀")

            low = result.get("Low Risk", [])
            medium = result.get("Medium Risk", [])
            high = result.get("High Risk", [])

            all_data = low + medium + high

            # -------------------- ALERTS --------------------
            for item in high:
                if any(k in item["product"].upper() for k in ["AMAZON", "FEE", "CHARGE", "POSTAGE"]):
                    st.error(f"🚨 Critical Risk: {item['product']} ({item['score']})")

            # -------------------- KPI METRICS --------------------
            st.subheader("📌 Key Insights")

            col1, col2, col3 = st.columns(3)

            total_products = len(all_data)
            highest_score = max([p["score"] for p in all_data]) if all_data else 0
            avg_score = round(
                sum(p["score"] for p in all_data) / max(len(all_data), 1), 2
            )

            col1.metric("Total Products", total_products)
            col2.metric("Highest Risk Score", highest_score)
            col3.metric("Average Risk Score", avg_score)

            # -------------------- DISPLAY PRODUCTS --------------------
            def show_products(title, data):
                st.subheader(title)
                for p in data:
                    st.write(f"📦 {p['product']}")
                    st.progress(p["score"] / 100)
                    st.caption(f"Risk Score: {p['score']}")

            col1, col2, col3 = st.columns(3)

            with col1:
                show_products("🟢 Low Risk", low)

            with col2:
                show_products("🟡 Medium Risk", medium)

            with col3:
                show_products("🔴 High Risk", high)

            # -------------------- PIE CHART --------------------
            st.subheader("📊 Risk Distribution")

            fig1 = px.pie(
                names=["Low", "Medium", "High"],
                values=[len(low), len(medium), len(high)],
                hole=0.4
            )
            st.plotly_chart(fig1, use_container_width=True)

            # -------------------- TOP HIGH RISK BAR --------------------
            st.subheader("📈 Top High Risk Products")

            if high:
                fig2 = px.bar(
                    x=[p["product"] for p in high],
                    y=[p["score"] for p in high],
                    labels={"x": "Product", "y": "Risk Score"}
                )
                st.plotly_chart(fig2, use_container_width=True)

            # -------------------- HISTOGRAM --------------------
            st.subheader("📊 Risk Score Distribution")

            if all_data:
                fig3 = px.histogram(
                    x=[p["score"] for p in all_data],
                    nbins=15,
                    labels={"x": "Risk Score", "y": "Frequency"}
                )
                st.plotly_chart(fig3, use_container_width=True)

            # -------------------- SCATTER --------------------
            st.subheader("📉 Risk Clustering")

            if all_data:
                fig4 = px.scatter(
                    x=list(range(len(all_data))),
                    y=[p["score"] for p in all_data],
                    color=[
                        "Low" if p in low else "Medium" if p in medium else "High"
                        for p in all_data
                    ],
                    labels={"x": "Product Index", "y": "Risk Score"}
                )
                st.plotly_chart(fig4, use_container_width=True)

            # -------------------- TOP 10 OVERALL --------------------
            st.subheader("🏆 Top 10 Risky Products (Overall)")

            top_all = sorted(all_data, key=lambda x: x["score"], reverse=True)[:10]

            if top_all:
                fig5 = px.bar(
                    x=[p["product"] for p in top_all],
                    y=[p["score"] for p in top_all],
                    labels={"x": "Product", "y": "Risk Score"}
                )
                st.plotly_chart(fig5, use_container_width=True)

            # -------------------- COMPARISON --------------------
            st.subheader("📊 Risk Level Comparison")

            fig6 = px.bar(
                x=["Low", "Medium", "High"],
                y=[len(low), len(medium), len(high)],
                labels={"x": "Risk Category", "y": "Count"},
            )
            st.plotly_chart(fig6, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")