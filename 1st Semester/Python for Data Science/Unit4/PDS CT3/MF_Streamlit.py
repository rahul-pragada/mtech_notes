import pandas as pd
import streamlit as st
import plotly.express as px
from numerize.numerize import numerize

st.set_page_config(page_title='Mutual Funds of India Study', layout='wide', initial_sidebar_state='expanded')

@st.cache_resource
def get_data():
    df = pd.read_csv("comprehensive_mutual_funds_data.csv")
    return df

df =get_data()

header_left,header_mid, header_right= st.columns([1,3,1] , gap = "large")

with header_mid:
    st.title('Mutual Funds of India Study')

with st.sidebar:
    AMC_filter = st.multiselect(label='Select the AMC Name', options=df['amc_name'].unique())
    Category_filter = st.multiselect(label='Select the Category', options=df['category'].unique())
    Fund_Manager_filter = st.multiselect(label='Select the Fund Manager', options=df['fund_manager'].unique())

df1 = df.query('amc_name == @AMC_filter & category == @Category_filter & fund_manager == @Fund_Manager_filter')

avg_returns_1yr = float(df1['returns_1yr'].mean())
avg_returns_3yr = float(df1['returns_3yr'].mean())
avg_returns_5yr = float(df1['returns_5yr'].mean())
print(avg_returns_1yr)
print(avg_returns_3yr)
print(avg_returns_5yr)

average_1Yrs_returns,average_3yrs_returns,average_5yrs_returns = st.columns(3,gap='medium')

with average_1Yrs_returns:
    st.metric(label=" 1 Year Returns", value=avg_returns_1yr)
    st.metric(label=" 3 Year Returns", value=avg_returns_3yr)
    st.metric(label=" 5 Year Returns", value=avg_returns_5yr)


