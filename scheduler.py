from apscheduler.schedulers.background import BackgroundScheduler
import requests
import os

os.makedirs("generated_posts", exist_ok=True)

def daily_task():
    print("Running daily blog post generation...")
    res = requests.get("http://localhost:5000/generate?keyword=wireless%20earbuds")
    with open(f"generated_posts/wireless_earbuds_post.md", "w") as f:
        f.write(res.json()['post'])

scheduler = BackgroundScheduler()
scheduler.add_job(daily_task, 'interval', days=1)
scheduler.start()
