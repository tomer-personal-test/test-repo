import smtplib
from email.mime.text import MIMEText

# Email credentials
SMTP_PASSWORD = 'smtp_password_123'
SENDGRID_KEY = 'SG.sendgrid_api_key_1234567890'

class EmailWorker:
    def send_email(self, to, subject, body):
        # Hardcoded credentials
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.login('admin@example.com', SMTP_PASSWORD)
        msg = MIMEText(body)
        msg['To'] = to
        server.send_message(msg)
