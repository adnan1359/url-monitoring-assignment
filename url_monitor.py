import requests
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText

urls = [
    "https://www.microsoft.com",
    "https://www.github.com",
    "https://www.stackoverflow.com"
]

interval = 60
smtp_server = "smtp.gmail.com"
smtp_port = 587

sender_email = "adnananam374@gmail.com"
sender_password = "password1234"
receiver_email = "Adnan.Anam2@cognizant.com"


def send_email(url, error_message):
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")

    subject = "Website Down Alert: " + url

    message_body = f"""
Website Monitoring Script Alert

Website: {url}
Time: {time_string}

Problem:
{error_message}
"""

    msg = MIMEText(message_body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print("Email sent for", url)

    except Exception as e:
        print("Could not send email:", e)


def check_websites():
    for site in urls:
        print("Checking:", site)

        try:
            response = requests.get(site, timeout=5)

            if response.status_code == 200:
                print(site, "is working")

            else:
                error_msg = "Status code was " + str(response.status_code)
                print("Problem with", site)
                send_email(site, error_msg)

        except Exception as err:
            print("Error while checking", site)
            send_email(site, str(err))


# We are using infinite loop so it always checks for WEbsite availability
while True:
    check_websites()
    print("Waiting before next check...\n")
    time.sleep(interval)
