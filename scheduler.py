from apscheduler.schedulers.background import BackgroundScheduler
import requests
import os

# Ensure output directory exists
os.makedirs("generated_posts", exist_ok=True)

# List of keywords you want to generate posts for daily
KEYWORDS = ["wireless earbuds", "best fitness trackers", "laptop cooling pads"]

def daily_task():
    print("Running daily blog post generation...")
    for keyword in KEYWORDS:
        try:
            formatted_keyword = keyword.replace(" ", "%20")
            response = requests.get(f"http://localhost:5000/generate?keyword={formatted_keyword}")
            
            if response.status_code == 200:
                safe_filename = keyword.lower().replace(" ", "_")
                post = response.json().get('post', '')
                with open(f"generated_posts/{safe_filename}.md", "w", encoding="utf-8") as f:
                    f.write(post)
                print(f"Generated post for: {keyword}")
            else:
                print(f"❌ Failed to generate post for: {keyword} - Status {response.status_code}")
        except Exception as e:
            print(f"❌ Error generating post for: {keyword} - {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(daily_task, 'interval', days=1)  # or use 'seconds=60' to test quickly
