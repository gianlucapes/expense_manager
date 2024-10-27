import streamlit as st
from datetime import datetime as dt
import requests


def add_update_tab(api_url):
    selected_date=st.date_input("Enter Date",dt(2024,8,1), label_visibility="collapsed")
    response=requests.get(f"{api_url}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_response=response.json()
    else:
        st.error("Failed to retrieve expenses")
        existing_response = []
    categories=["Rent","Food","Shopping","Entertainment","Other"]
    with st.form(key="expense_form"):
        col1,col2,col3= st.columns(3)

        with col1:
            st.subheader("Amount")
        with col2:
            st.subheader("Category")
        with col3:
            st.subheader("Notes")
        
        expenses=[]

        for i in range(5):

            if i < len(existing_response):
                amount=existing_response[i]['amount']
                category=existing_response[i]['category']
                notes=existing_response[i]['notes']
            else:
                amount=0.0
                category="Shopping"
                notes=""

            col1,col2,col3= st.columns(3)
            with col1:
                amount_input=st.number_input(label="Amount",min_value=0.0,step=1.0,value=amount,key=f"amount_{i}",label_visibility="collapsed")
            
            with col2:
                category_input=st.selectbox(label="Category",options=categories,index=categories.index(category),key=f"category_{i}",label_visibility="collapsed")
            
            with col3:
                notes_input=st.text_input(label="Notes",key=f"notes_{i}",value=notes,label_visibility="collapsed")

            expenses.append(
                {
                    'amount':amount_input,
                    'category':category_input,
                    'notes':notes_input
                }
            )
        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses= [expense for expense in expenses if expense['amount']>0]
            response = requests.post(f"{api_url}/expenses/{selected_date}",json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses updated succesful")
            else:
                st.error("An error has occured during updating expenses")