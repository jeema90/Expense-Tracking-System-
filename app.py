import streamlit as st
from datetime import datetime
import requests
from analytics_by_category import analytics_by_category
from add_update_ui import add_update_tab

from analytics_by_month import analytics_by_month

st.title("EXPENSE TRACKING SYSTEM")


tab1, tab2,tab3 = st.tabs(["Add/Update", "Analytics_by_Category","Analytics_by_Month"])

with tab1:
    add_update_tab()

with tab2:
    analytics_by_category()

with tab3:
    analytics_by_month()