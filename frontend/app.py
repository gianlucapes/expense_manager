import streamlit as st
from datetime import datetime as dt
from analytics_ui import analytics_by_category_tab,analytics_by_month_tab
from add_update_ui import add_update_tab

API_URL="http://localhost:8000"


st.title("Expense Tracking System")

tab1,tab2,tab3= st.tabs(["Add/Update","Analytics By Category","Analytics By Month"])

with tab1:
   add_update_tab(api_url=API_URL)

with tab2:
   analytics_by_category_tab(api_url=API_URL)

with tab3:
   analytics_by_month_tab(api_url=API_URL)

