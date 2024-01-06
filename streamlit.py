import pandas as pd
import streamlit as st

st.title('Dashboard')

security_data = pd.read_csv('E:\\Assignment\\Input\\securities.csv')

st.dataframe(security_data)


