import streamlit as st
from datetime import datetime as dt
import requests
import pandas as pd


def analytics_by_category_tab(api_url:str):
    col1, col2 = st.columns(2)

    with col1:
        start_date=st.date_input("Start Date",dt(2024,8,1))
    
    with col2:
        end_date=st.date_input("Start Date",dt(2024,8,5))
    
    if st.button("Get Analytics"):
        payload={
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        response=requests.post(f"{api_url}/analytics/category/",json=payload)
        response=response.json()

        data={
            "Category":list(response.keys()),
            "Total":[response[category]["total"] for category in response],
            "Percentage":[response[category]["percentage"] for category in response]
        }

        df=pd.DataFrame(data).sort_values(by="Percentage",ascending=False)

        st.title("Expense Breakdown By Category")

        st.bar_chart(data=df.set_index("Category")['Percentage'])


        st.table(df)

def analytics_by_month_tab(api_url:str):
    
    response=requests.get(f"{api_url}/analytics/month/")
    response=response.json()

    month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"}

    data={
        "Month Name" : [month_dict[record['month_number']] for record in response],
        "Total": [record['total'] for record in response]
    }

    df=pd.DataFrame(data).sort_values(by="Total",ascending=False)
    df.set_index('Month Name', inplace = True)

    st.title("Expense Breakdown By Month")

    st.bar_chart(data=df)

    st.table(df)