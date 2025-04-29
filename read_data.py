import sqlite3

# Connection to database
conn = sqlite3.connect('database/home.db')
cursor = conn.cursor()

# Creation of table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Homes (
#    home_id INTEGER PRIMARY KEY AUTOINCREMENT,
#    sensor_name TEXT NOT NULL,
#    data DECIMAL(10, 2) NOT NULL)
# ''')


# Insert data
def insert_data(sensor_name, data):
    cursor.execute('''
    INSERT INTO Homes (sensor_name, data) VALUES (?, ?)
    ''', (sensor_name, data))
    conn.commit()


# Read data
def read_data():
    data = cursor.execute('SELECT * FROM Homes')
    return data.fetchall()


# Update data
def update_data(new_sensor_name, new_data, home_id):
    cursor.execute('''
    UPDATE Homes SET sensor_name = ?, data = ? WHERE home_id = ?
    ''', (new_sensor_name, new_data, home_id))
    conn.commit()


# Delete data
def delete_data(home_id):
    cursor.execute('''
    DELETE FROM Homes WHERE home_id = ?
    ''', (home_id))
    conn.commit()
