import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# Loading the data
data = pd.read_csv('dataset.csv')



data['Date(dd-mm-yyyy)'] = pd.to_datetime(data['Date(dd-mm-yyyy)'], format='mixed', dayfirst=True)
data['Day'] = data['Date(dd-mm-yyyy)'].dt.day_name()
data['Month'] = data['Date(dd-mm-yyyy)'].dt.month_name()

# ---------------------------- FUNCTIONS ---------------------------- 

def Sales_by_DAY():
    data.groupby(['Month', 'Day' , 'Product line' ])['Quantity'].sum().reset_index(name='Count')
    graph=data.groupby(['Month' ,'Day','Product line'])['Quantity'].sum().reset_index(name='Count')
    g= px.bar(
        graph,
        x="Day",
        y="Count",
        color="Product line",
        facet_row="Month",  
        barmode="group",
        height=1400,
        
        color_discrete_sequence=px.colors.qualitative.Set2,
        title="Sales by Product Line and Day (Interactive)"
  
)
    g.update_xaxes(showticklabels=True)
    st.plotly_chart(g)

def TAX_COLLECTION_GRAPH():
    tax_group = data.groupby(['Month', 'Product line'])['Tax 5%'].sum().reset_index()
    fig = px.bar(tax_group, x='Product line', y='Tax 5%', color='Product line',
                 facet_row='Month', title='Monthly Tax Collection by Product Line',
                 width=1100, height=1200)
    fig.update_xaxes(showticklabels=True)
    st.plotly_chart(fig)

def rating_data():
    rating_avg = data.pivot_table(columns='Product line', index='City',
                                  values='Rating', aggfunc='mean').reset_index()
    melted = pd.melt(rating_avg, id_vars='City', var_name='Product line', value_name='Average rating')
    fig = px.bar(melted, x='City', y='Average rating', color='Product line', barmode='group',
                 title='Average Ratings of Product Line by City')
    st.plotly_chart(fig)

def sales_by_city():
    sales = data.groupby('City')['Total'].sum().reset_index()
    fig = px.pie(sales, names='City', values='Total', title='Total Sales by City')
    st.plotly_chart(fig)

def csi_calculation():
    rating = data.groupby(['City', 'Product line', 'Rating']).size().reset_index(name='Count')
    max_rating = 10
    csi_data = []

    for city in rating['City'].unique():
        for line in rating['Product line'].unique():
            subset = rating[(rating['City'] == city) & (rating['Product line'] == line)]
            total = subset['Count'].sum()
            weighted = (subset['Rating'] * subset['Count']).sum()
            if total > 0:
                csi = (weighted / total) / max_rating * 100
                csi_data.append({"City": city, "Product line": line, "CSI(%)": round(csi, 2)})

    df = pd.DataFrame(csi_data)
    fig = px.bar(df, y='CSI(%)', x='City', color='Product line', barmode='group',
                 title='Customer Satisfaction Index by City')
    st.plotly_chart(fig)

def sales_prediction_graph():
    monthly_sales = data.groupby(['City', 'Month', 'Product line'])['Total'].sum().reset_index()
    fig = px.bar(monthly_sales, x="Month", y="Total", color="Product line",
                 facet_row="City", barmode='group',
                 category_orders={"Month": ['January', 'February', 'March']},
                 title="Monthly Sales of Product Line", height=1200)
    fig.update_xaxes(showticklabels=True)
    st.plotly_chart(fig)

def revenue_prediction_graph():
    sales_df = data.groupby(['City', 'Month'])['Total'].sum().reset_index(name="Revenue")
    sales_df['Month'] = pd.Categorical(sales_df['Month'], categories=['January', 'February', 'March'], ordered=True)
    pivot = sales_df.pivot(index='City', columns='Month', values='Revenue')
    
    pivot = pivot.reset_index()  #  The FIXING OF  THE MELT ERROR

    # Step 1: Define training data (predict March from Jan & Feb)
    X_train = pivot[['January', 'February']]
    y_train = pivot['March']

    # Step 2: Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Step 3: Prepare data to predict April (using Feb & Mar)
    X_april = pivot[['February', 'March']].copy()

    # Step 4: Rename columns to match the training feature names
    X_april.columns = ['January', 'February']

    # Step 5: Predict April
    pivot['April_Prediction'] = model.predict(X_april)

    # Step 6: Melt and plot
    long_df = pd.melt(
        pivot,
        id_vars='City',
        value_vars=['January', 'February', 'March', 'April_Prediction'],
        var_name='Month',
        value_name='Revenue'
    )

    fig = px.line(long_df, x='Month', y='Revenue', color='City', markers=True,
                  title='Monthly Revenue Prediction (Including April)')
    st.plotly_chart(fig)


def orignal():
    st.dataframe(data.head(100))
