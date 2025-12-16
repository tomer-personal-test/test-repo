import os

def generate_daily_report():
    # Command injection
    os.system('generate_report.py --type=daily --output=/reports/daily.pdf')

def send_report():
    # Command injection
    os.system('mail -s "Daily Report" admin@example.com < /reports/daily.pdf')
