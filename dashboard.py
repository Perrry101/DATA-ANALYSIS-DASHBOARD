import streamlit as st

from module import (
    Sales_by_DAY,
    TAX_COLLECTION_GRAPH,
    rating_data,
    sales_by_city,
    csi_calculation,
    sales_prediction_graph,
    revenue_prediction_graph,
    orignal
)

st.set_page_config(page_title="Supermarket Dashboard", layout="wide")
st.title("Supermarket Sales Analysis Dashboard")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 ,tab8 = st.tabs([
    "Sales by DAY",
    "Tax by Product Line",
    "Rating Across City",
    "Sales by City",
    "Customer Satisfaction Index",
    "Sales Prediction",
    "Revenue Prediction",
    "ORIGNAL DATA",
    
])

with tab1:
    st.subheader("SALES by DAY")
    Sales_by_DAY()

with tab2:
    st.subheader("Monthly Tax Collection by Product Line")
    TAX_COLLECTION_GRAPH()

with tab3:
    st.subheader("Rating Across City")
    rating_data()

with tab4:
    st.subheader("Total Sales by City")
    sales_by_city()

with tab5:
    st.subheader("Customer Satisfaction Index by City")
    csi_calculation()

with tab6:
    st.subheader("Sales Forecast")
    sales_prediction_graph()

with tab7:
    st.subheader("Revenue Forecast")
    revenue_prediction_graph()

with tab8:
    st.subheader("ORIGNAL DATA")
    orignal()

# with tab8:
#     st.subheader("Sales by day")
#     Sales_by_DAY()

st.caption("Data Source: Supermarket Dataset")
