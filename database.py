import sqlite3

connection = sqlite3.connect('bets.db')
cursor_obj = connection.cursor()

# Dropping the table if it exists
cursor_obj.execute("DROP TABLE IF EXISTS BETS")

# Creating the table
table = """ CREATE TABLE BETS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Date DATE NOT NULL,
            Units INT NOT NULL,
            Description VARCHAR(255) DEFAULT 'None',
            Multiplier INT NOT NULL,
            Outcome BOOLEAN,
            Profit INT DEFAULT NULL
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