import sendgrid
from sendgrid.helpers.mail import Mail

# SendGrid credentials
SENDGRID_API_KEY = 'SG.1234567890abcdefghijklmnopqrstuvwxyz'

class SendGridIntegration:
    def __init__(self):
        # Hardcoded API key
        self.sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    
    def send_email(self, to, subject, body):
        message = Mail(from_email='noreply@example.com', to_emails=to, subject=subject, html_content=body)
        return self.sg.send(message)
