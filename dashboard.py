import streamlit as st

from module import (
    TAX_COLLECTION_GRAPH,
    rating_data,
    sales_by_city,
    csi_calculation,
    sales_prediction_graph,
    revenue_prediction_graph,
    top_customers_by_revenue
)

st.set_page_config(page_title="Supermarket Dashboard", layout="wide")
st.title("Supermarket Sales Analysis Dashboard")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Tax by Product Line",
    "Rating vs Gross Income",
    "Sales by City",
    "Customer Satisfaction Index",
    "Sales Prediction",
    "Revenue Prediction",
    "ORIGNAL DATA"
])

with tab1:
    st.subheader("Monthly Tax Collection by Product Line")
    TAX_COLLECTION_GRAPH()

with tab2:
    st.subheader("Rating vs Gross Income by Branch")
    rating_data()

with tab3:
    st.subheader("Total Sales by City")
    sales_by_city()

with tab4:
    st.subheader("Customer Satisfaction Index by City")
    csi_calculation()

with tab5:
    st.subheader("Sales Forecast")
    sales_prediction_graph()

with tab6:
    st.subheader("Revenue Forecast")
    revenue_prediction_graph()

with tab7:
    st.subheader("ORIGNAL DATA")
    top_customers_by_revenue()

st.caption("Data Source: Supermarket Dataset")
