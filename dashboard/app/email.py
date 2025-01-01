import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, recipients):
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"        # Replace with your password
    smtp_server = "smtp.gmail.com"           # Replace if you're not using Gmail
    smtp_port = 587

    try:
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

