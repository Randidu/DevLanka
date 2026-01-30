from app.utils.email import send_email
from app.config import settings

print(f"Testing email with:")
print(f"User: {settings.MAIL_USERNAME}")
print(f"From: {settings.MAIL_FROM}")
print(f"Server: {settings.MAIL_SERVER}:{settings.MAIL_PORT}")
# Mask password for safety in logs
masked_pwd = settings.MAIL_PASSWORD[:2] + "****" + settings.MAIL_PASSWORD[-2:] if settings.MAIL_PASSWORD else "None"
print(f"Password: {masked_pwd}")

success = send_email(
    subject="Test Verify Email", 
    recipients=["randidudamsith96@gmail.com"], 
    body="<h1>This is a test email</h1>"
)

if success:
    print("Email Sent Successfully!")
else:
    print("Email Sending Failed.")
