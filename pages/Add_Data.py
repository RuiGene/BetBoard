import streamlit as st
import sqlite3
from helper_functions import calculate_profit

st.set_page_config(page_title="Add Data", page_icon = "➕")

connection = sqlite3.connect('bets.db')
cursor_obj = connection.cursor()

st.markdown("# Insert Data")
# st.sidebar.header("Add Data")

date_input = st.date_input("Date of Bet:", value = None)
units = st.number_input("Number of Units:", value = None, placeholder = "E.g 1 or 2")
description = st.text_input("Bet Description:", value = None, placeholder = "E.g. NBA: Kevin Durant Over 25 Pts")
multiplier = st.number_input("Multiplier:", value = None, placeholder = "E.g. 1.9 or 1.2")
outcome = st.selectbox("Outcome of Bet:", ("Won", "Lost"))

if st.button("Add Bet"):
    profit = calculate_profit(units, multiplier, outcome)
    st.text(profit)
    st.stop()
    outcome_boolean = True if outcome == "Won" else False
    try:
        cursor_obj.execute(
            """
                INSERT INTO BETS (Date, Units, Description, Multiplier, Outcome)
                VALUES (?, ?, ?, ?, ?)
            """,
            (date_input, units, description, multiplier, outcome_boolean)
        )
        connection.commit()
        st.success("Bet added successfully")
    except Exception as e:
        st.error(f"An error occurred: {e}")

connection.close()