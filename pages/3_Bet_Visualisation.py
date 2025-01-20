import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bet Visualisations", page_icon = "💸")
st.markdown("# Cumulative Profit")

connection = sqlite3.connect('bets.db')
query = "SELECT Date, Profit FROM BETS WHERE Profit IS NOT NULL ORDER BY Date ASC"
df = pd.read_sql_query(query, connection)
connection.close()

df['Date'] = pd.to_datetime(df['Date'])
df['Cumulative_Profit'] = df['Profit'].cumsum()

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Cumulative_Profit'], marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Cumulative Profit Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Profit')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(plt)

# Visualisations to add
# Monthly/weekly profit loss
# Win Rate Over Time: A moving average or line graph showing your success rate over time. You can calculate this as (wins / total bets) within a time window.
# outcome distribution: A pie chart or bar chart of the outcomes (win, lose, push). It gives a snapshot of your overall betting success.
# Multiplier Distribution: A histogram of multipliers used. It shows the spread of low-risk vs. high-risk bets.