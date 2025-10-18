import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def add_update_tab():
    # Date picker OUTSIDE the form so it reruns automatically
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1).date())

    # Fetch expenses for that date
    response = requests.get(f"{API_URL}/expenses/{selected_date.isoformat()}")
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []
    st.write("Selected date:", selected_date)

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    # ---------------- FORM START ----------------
    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        col1.markdown("**Amount**")
        col2.markdown("**Category**")
        col3.markdown("**Notes**")
        expenses=[]
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount, category, notes = 0.0, "Shopping", ""

            row = st.columns(3)
            amount_input=row[0].number_input("Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}_{selected_date}",label_visibility="collapsed")
            category_input=row[1].selectbox("Category", categories,
                             index=categories.index(category) if category in categories else 0,
                             key=f"category_{selected_date}_{i}",label_visibility="collapsed")
            notes_input=row[2].text_input("Notes", value=notes, key=f"notes_{selected_date}_{i}",label_visibility="collapsed")
            expenses.append({
                "amount":amount_input,
                "category":category_input,
                "notes":notes_input
            })
        submit_button = st.form_submit_button("Save Expenses")

        if submit_button:
            filtered_expenses=[expense for expense in expenses if expense["amount"]>0]
            response = requests.post(f"{API_URL}/expenses/{selected_date.isoformat()}",json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses saved!")
            else:
                st.error("Failed to retrieve expenses")