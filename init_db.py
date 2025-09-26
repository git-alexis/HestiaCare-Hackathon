import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS HestiaCare")
cursor.execute("USE HestiaCare")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Favourite_ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    User_id INT,
    name VARCHAR(100) NOT NULL UNIQUE,
    carbs FLOAT,
    protein FLOAT,
    fat FLOAT,
    calories FLOAT,
    FOREIGN KEY (User_id) REFERENCES Users(id)
)
""")

connection.commit()
cursor.close()
connection.close()
