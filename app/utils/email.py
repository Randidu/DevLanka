import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings

def send_email(subject: str, recipients: list[str], body_html: str, body_text: str):
    msg = MIMEMultipart('alternative')
    msg['From'] = settings.MAIL_FROM
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Attach both plain text and HTML versions
    part1 = MIMEText(body_text, 'plain')
    part2 = MIMEText(body_html, 'html')

    msg.attach(part1)
    msg.attach(part2)

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
    subject = "DevLanka Hub - Email Verification Code"
    
    # Plain text version
    text_body = f"""Welcome to DevLanka Hub!

Please use the following code to verify your email address:
{code}

If you did not register for an account, please ignore this email.
"""

    # HTML version with modern styling
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f6f9;
                color: #333333;
            }}
            .container {{
                max-width: 600px;
                margin: 40px auto;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.05);
                overflow: hidden;
            }}
            .header {{
                background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                color: #ffffff;
                padding: 30px;
                text-align: center;
            }}
            .header h1 {{
                margin: 0;
                font-size: 24px;
                font-weight: 600;
                letter-spacing: 0.5px;
            }}
            .content {{
                padding: 40px 30px;
                text-align: center;
            }}
            .greeting {{
                font-size: 20px;
                margin-bottom: 20px;
                color: #1e293b;
            }}
            .message {{
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 30px;
                color: #555555;
            }}
            .code-box {{
                background-color: #f1f5f9;
                border: 2px dashed #cbd5e1;
                border-radius: 8px;
                padding: 20px;
                margin: 0 auto 30px;
                width: fit-content;
                min-width: 200px;
            }}
            .code {{
                font-size: 32px;
                font-weight: 700;
                color: #2563eb;
                letter-spacing: 8px;
                font-family: 'Courier New', monospace;
            }}
            .footer {{
                background-color: #f8fafc;
                padding: 20px;
                text-align: center;
                font-size: 12px;
                color: #94a3b8;
                border-top: 1px solid #e2e8f0;
            }}
            .footer a {{
                color: #2563eb;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>DevLanka Hub</h1>
            </div>
            <div class="content">
                <h2 class="greeting">Verify Your Account</h2>
                <p class="message">
                    Welcome to DevLanka Hub! Please use the code below to complete your verification.
                </p>
                <div class="code-box">
                    <span class="code">{code}</span>
                </div>
                <p class="message" style="margin-bottom: 0; font-size: 14px;">
                    This code will expire in 10 minutes.<br>
                    If you didn't define this action, please just ignore this email.
                </p>
            </div>
            <div class="footer">
                You received this email because you registered on DevLanka Hub.<br>
                &copy; 2026 DevLanka Hub. All rights reserved.
            </div>
        </div>
    </body>
    </html>
    """
    return send_email(subject, [email], html_body, text_body)

def send_password_reset_email(email: str, reset_link: str):
    subject = "DevLanka Hub - Reset Your Password"
    
    # Plain text version
    text_body = f"""Reset Your Password

We received a request to reset your password for your DevLanka Hub account.
Please visit the following link to reset it:

{reset_link}

This link will expire in 30 minutes.
If you did not request a password reset, please ignore this email.
"""

    # HTML version with modern styling
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f6f9;
                color: #333333;
            }}
            .container {{
                max-width: 600px;
                margin: 40px auto;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.05);
                overflow: hidden;
            }}
            .header {{
                background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                color: #ffffff;
                padding: 30px;
                text-align: center;
            }}
            .header h1 {{
                margin: 0;
                font-size: 24px;
                font-weight: 600;
                letter-spacing: 0.5px;
            }}
            .content {{
                padding: 40px 30px;
                text-align: center;
            }}
            .greeting {{
                font-size: 20px;
                margin-bottom: 20px;
                color: #1e293b;
            }}
            .message {{
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 30px;
                color: #555555;
            }}
            .button {{
                display: inline-block;
                background-color: #2563eb;
                color: #ffffff;
                text-decoration: none;
                padding: 12px 30px;
                border-radius: 6px;
                font-weight: 600;
                font-size: 16px;
                margin-bottom: 30px;
                transition: background-color 0.3s;
            }}
            .button:hover {{
                background-color: #1d4ed8;
            }}
            .footer {{
                background-color: #f8fafc;
                padding: 20px;
                text-align: center;
                font-size: 12px;
                color: #94a3b8;
                border-top: 1px solid #e2e8f0;
            }}
            .footer a {{
                color: #2563eb;
                text-decoration: none;
            }}
            .link-text {{
                word-break: break-all;
                font-size: 12px;
                color: #2563eb;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>DevLanka Hub</h1>
            </div>
            <div class="content">
                <h2 class="greeting">Reset Your Password</h2>
                <p class="message">
                    We received a request to reset the password for your DevLanka Hub account. Click the button below to set up a new password.
                </p>
                
                <a href="{reset_link}" class="button" style="color: white !important;">Reset Password</a>
                
                <p class="message" style="margin-bottom: 0; font-size: 14px;">
                    This link will expire in 30 minutes.<br>
                    If you didn't request a password reset, you can safely ignore this email.
                </p>
                
                <p class="link-text">
                    Button not working? Copy and paste this link:<br>
                    {reset_link}
                </p>
            </div>
            <div class="footer">
                You received this email because a password reset was requested for your account.<br>
                &copy; 2026 DevLanka Hub. All rights reserved.
            </div>
        </div>
    </body>
    </html>
    """
    return send_email(subject, [email], html_body, text_body)
