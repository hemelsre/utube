import mysql.connector
import logging

def init_db():
    logging.info("Database initialized")

def get_niches():
    logging.info("Fetched niches")

def get_script_count():
    logging.info("Fetched script counts")

def save_script(niche, script):
    logging.info(f"Saved script for niche: {niche}")