from app.utils.email import send_verification_email

success = send_verification_email(
    email="randidudamsith55@gmail.com",
    code="123456"
)

if success:
    print("Email Sent Successfully!")
else:
    print("Email Sending Failed.")
