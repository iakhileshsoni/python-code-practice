import time

from apscheduler.schedulers.background import BackgroundScheduler
from motivator import send_whatsapp_txt, client, quote

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

job = scheduler.add_job(send_whatsapp_txt, 'cron', [client, quote], hour="1", minute="10")

print(job)

while True:
    time.sleep(1)
