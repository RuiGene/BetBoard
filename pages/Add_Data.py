import streamlit as st
import numpy as np

st.set_page_config(page_title="Add Data", page_icon = "➕")

st.markdown("# Insert Data")
# st.sidebar.header("Add Data")

date_input = st.date_input("Date of Bet:", value = None)
units = st.number_input("Number of Units:", value = None, placeholder = "E.g 1 or 2")
description = st.text_input("Bet Description:", value = None, placeholder = "E.g. NBA: Kevin Durant Over 25 Pts")
multiplier = st.number_input("Multiplier:", value = None, placeholder = "E.g. 1.9 or 1.2")
outcome = st.selectbox("Outcome of Bet:", ("Won", "Lost"))

st.button("Insert")