import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings

def send_email(subject: str, recipients: list[str], body: str):
    msg = MIMEMultipart()
    msg['From'] = settings.MAIL_FROM
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP(settings.MAIL_SERVER, settings.MAIL_PORT)
        server.starttls()
        server.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(settings.MAIL_FROM, recipients, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def send_verification_email(email: str, code: str):
    subject = "Verify your account - SL Tech Platform"
    body = f"""
    <html>
        <body>
            <h2>Welcome to SL Tech Platform!</h2>
            <p>Please use the following code to verify your email address:</p>
            <h1>{code}</h1>
            <p>If you did not register for an account, please ignore this email.</p>
        </body>
    </html>
    """
    return send_email(subject, [email], body)
