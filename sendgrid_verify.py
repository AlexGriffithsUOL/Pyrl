# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
api_key = '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'
staging_api_key = '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'
message = Mail(
    from_email='admin@pyrl.uk',
    to_emails=['conor.p.murphy2@gmail.com', 'alex.john.griffiths.2001@gmail.com'],
    subject='Test Email via Pyrl (DEV)',
    html_content='This is a test email to verify the SendGrid Email integration')
try:
    sg = SendGridAPIClient(api_key=api_key)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)