from apscheduler.schedulers.background import BackgroundScheduler
import logging

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.start()
    logging.info("Scheduler started")

def stop_scheduler():
    scheduler.shutdown()
    logging.info("Scheduler stopped")