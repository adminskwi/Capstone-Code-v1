import sqlite3
from bs4 import BeautifulSoup

# Step 1: Read the file
with open('try1.html', 'r') as file:
    content = file.read()

# Step 2: Parse the HTML
soup = BeautifulSoup(content, 'html.parser')
pre_text = soup.find('pre').get_text()

# Step 3: Extract and structure data
lines = pre_text.splitlines()
data = []
for line in lines:
    if line.strip() == "#RD@75" or line.startswith("#RD@75"):  # Ignore "#RD@75" lines
        continue
    if line.startswith("#RD"):  # Process lines starting with "#RD"
        fields = line[12:].split()  # Skip the "#RD" prefix and split the rest
        while len(fields) < 11:  # Ensure there are 11 fields by adding None if necessary
            fields.append(None)
        data.append(fields[:11])  # Take only the first 11 fields

# Step 4: Create a database and table
conn = sqlite3.connect('data.db')  # This creates a file named 'data.db' in the current directory
cursor = conn.cursor()

# Drop the table if it exists to avoid column mismatches
cursor.execute("DROP TABLE IF EXISTS records")

# Recreate the table with the correct columns
cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col1 TEXT,
    col2 TEXT,
    col3 TEXT,
    col4 TEXT,
    col5 TEXT,
    col6 TEXT,
    col7 TEXT,
    col8 TEXT,
    col9 TEXT,
    col10 TEXT,
    col11 TEXT

)
""")

# Step 5: Insert data into the database
for record in data:
    cursor.execute(
        "INSERT INTO records (col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        record
    )

conn.commit()
conn.close()

print("Data has been inserted into the database!")
print(record)