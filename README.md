# URL Monitoring Tool

A simple Python-based monitoring tool designed to keep an eye on a list of websites and send an email if any of them go down or return an error.

### What it does
* **Checks Availability**: It pings a list of URLs (Microsoft, GitHub, and StackOverflow by default).
* **Automatic Looping**: The script runs in an infinite loop, checking the sites based on a configurable time interval.
* **Email Alerts**: If a site isn't returning a "200 OK" status, the script automatically sends an email notification with the error details and a timestamp.
* **Configurable Settings**: You can easily change how often it checks or which email it sends from using environment variables.

### Project Structure
* `url_monitor.py`: The main script that contains the monitoring logic and the email alert function.
* `config/settings.py`: A dedicated script to handle loading all your environment variables safely via `python-dotenv`.
* `requirements.txt`: Lists the external libraries (like `requests`) needed to run the code.
* `.env.example`: A template for the private credentials so we know what keys to set up.
* `.gitignore`: Configured to ensure the private `.env` file and Python cache files aren't accidentally pushed to GitHub.

### How to get it running

1. **Install dependencies**:
   You'll need the `requests` library. You also need `python-dotenv` to read the configuration.
   ```bash
   pip install -r requirements.txt
