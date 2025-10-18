import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_by_month():

 if st.button("Get Analytics By Month"):

   response = requests.get(f"{API_URL}/analytics_by_month/")
   data2=response.json()

   df = pd.DataFrame(data2)
   df['month'] = pd.to_datetime(df['month'], format="%m").dt.strftime('%B')
   df['month_number'] = pd.to_datetime(df['month'], format='%B').dt.month
   df_sorted = df.sort_values('month_number')
   st.title ("Expense Breakdown By Month")
   st.bar_chart(data=df_sorted.set_index("month"),width=0, height=0, use_container_width=True)

   st.table(df_sorted)