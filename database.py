import sqlite3

connection = sqlite3.connect('bets.db')
cursor_obj = connection.cursor()

# Creating table
table = """ CREATE TABLE IF NOT EXISTS BETS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Date DATE NOT NULL,
            Units INT NOT NULL,
            Description VARCHAR(255) DEFAULT 'None',
            Multiplier INT NOT NULL,
            Outcome BOOLEAN
        ); """

cursor_obj.execute(table)
connection.close()


import sqlite3

# Connect to the database
connection = sqlite3.connect('bets.db')
cursor_obj = connection.cursor()

# Insert values into the BETS table
cursor_obj.execute("""
    INSERT INTO BETS (Date, Units, Description, Multiplier, Outcome)
    VALUES ('2024-12-23', 5, 'Bet on Team A', 2, 1)
""")

# Commit the transaction
connection.commit()

# Close the connection
connection.close()