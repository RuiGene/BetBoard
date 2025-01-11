import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="View Data", page_icon = "👁️")

st.markdown("# View Data")

connection = sqlite3.connect('bets.db')
cursor_obj = connection.cursor()

query = "SELECT * FROM bets"
df = pd.read_sql_query(query, connection)

st.dataframe(
    df,
    use_container_width=True,
    column_config={
        "_index": None  # Hides the index column
    }
)

st.markdown("# Edit Data")
edited_df = st.data_editor(
    df,
    use_container_width=True,
    column_config={
        "_index": None  # Hides the index column
    }
)

# # Button to save changes
# if st.button("Save Changes"):
#     # Find rows that were updated
#     updated_rows = edited_df.compare(df)
#     st.write(updated_rows)
    

#     # Process updates
#     for index, changes in updated_rows.iterrows():
#         st.write(index, changes)
#         st.stop()
#         updated_values = changes["self"]  # Values from the updated DataFrame
#         original_values = changes["other"]  # Original values

#         st.write(updated_values, original_values)
#         st.stop()

#         # Generate the SQL query to update this row
#         update_query = f"""
#         UPDATE bets
#         SET {', '.join([f"{col} = ?" for col in edited_df.columns])}
#         WHERE id = ?
#         """
#         connection.execute(update_query, (*updated_values, original_values["id"]))

#     # Commit the changes to the database
#     connection.commit()
#     st.success("Database updated successfully!")

# Close the connection
connection.close()