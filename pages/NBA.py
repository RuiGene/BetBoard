import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="NBA Player Profile", page_icon = "🏀")

col1, col2, col3 = st.columns(3)

text_search = st.text_input("Search for an NBA player", value="")