from apscheduler.schedulers.background import BackgroundScheduler

from app.jobs.pricing import update_product_price
from app.jobs.monitor import watch_for_price_decrease
from app.jobs.alert import send_alerts

scheduler = BackgroundScheduler()

scheduler.add_job(send_alerts, 'interval', minutes=10, max_instances=2)
scheduler.add_job(update_product_price, 'interval', minutes=15, max_instances=2)
scheduler.add_job(watch_for_price_decrease, 'interval', minutes=10, max_instances=2)

def init():
    scheduler.start()
