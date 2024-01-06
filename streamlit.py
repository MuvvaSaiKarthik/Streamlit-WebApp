import pandas as pd
import streamlit as st

st.title('Dashboard')

# security_data = pd.read_csv('E:\\Assignment\\Input\\securities.csv')
security_data = pd.read_csv('E:\\Assignment\\Input\\new_values\\fo23FEB2023bhav.csv')


st.dataframe(security_data)


