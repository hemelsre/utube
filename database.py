import mysql.connector
import logging
from mysql.connector import Error
from config import DB_CONFIG

def init_db():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            logging.info("Connected to MariaDB")
        connection.close()
    except Error as e:
        logging.error(f"Error connecting to MariaDB: {e}")

def get_niches():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT niche FROM scripts")
        niches = [row[0] for row in cursor.fetchall()]
        connection.close()
        return niches
    except Error as e:
        logging.error(f"Error fetching niches: {e}")
        return []

def get_niches_with_counts():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT niche, COUNT(*) FROM scripts GROUP BY niche")
        data = cursor.fetchall()
        connection.close()
        return data
    except Error as e:
        logging.error(f"Error fetching niche counts: {e}")
        return []

def save_script(niche, script):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO scripts (niche, script) VALUES (%s, %s)", (niche, script))
        connection.commit()
        connection.close()
        logging.info(f"Saved script for niche: {niche}")
    except Error as e:
        logging.error(f"Error saving script: {e}")
