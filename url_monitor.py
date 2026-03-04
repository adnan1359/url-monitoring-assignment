import requests
import smtplib
import time
import os
from datetime import datetime
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))

urls = [
    "https://www.microsoft.com",
    "https://www.github.com",
    "https://www.stackoverflow.com"
]


def send_email(url, error_message):
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")

    subject = "Website Down Alert - " + url

    body = f"""
Website Monitoring Alert

Website: {url}
Time: {time_str}

Error:
{error_message}
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()

        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

        server.quit()

        print("Alert email sent for", url)

    except Exception as e:
        print("Email sending failed:", e)


def check_websites():
    for site in urls:
        print("Checking website:", site)

        try:
            response = requests.get(site, timeout=5)

            if response.status_code == 200:
                print(datetime.now(), "-", site, "is working")

            else:
                error_msg = "Status code was " + str(response.status_code)
                print("Something wrong with", site)
                send_email(site, error_msg)

        except Exception as err:
            print("Error while checking", site)
            send_email(site, str(err))


# We are using infinite loop so it always checks for WEbsite availability
while True:
    print("Checking websites..")
    check_websites()

    print("Sleeping for", CHECK_INTERVAL, "seconds")
    time.sleep(CHECK_INTERVAL)
