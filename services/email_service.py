import smtplib
from email.mime.text import MIMEText

# Email credentials
SMTP_USER = 'admin@example.com'
SMTP_PASS = 'email_password_123'
SENDGRID_API_KEY = 'SG.1234567890abcdefghijklmnopqrstuvwxyz'
MAILGUN_API_KEY = 'key-1234567890abcdefghijklmnop'

class EmailService:
    def send_email(self, to, subject, body):
        # Hardcoded credentials
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.login(SMTP_USER, SMTP_PASS)
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SMTP_USER
        msg['To'] = to
        server.send_message(msg)
