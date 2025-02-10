import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_otp(email):
    otp = random.randint(100000, 999999)
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"  # Ensure you use an app-specific password if using Gmail.
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = "Your OTP for 2FA Authentication"
    body = f"Your OTP for authentication is: {otp}. It will expire in 5 minutes."
    message.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print(f"OTP sent to {email}")
        return otp
    except Exception as e:
        print(f"Error sending OTP: {e}")
        return None

def verify_otp(user_otp, original_otp):
    return user_otp == original_otp

if __name__ == "__main__":
    email = input("Enter your email: ")
    original_otp = send_otp(email)
    
    if original_otp:
        user_otp = int(input("Enter the OTP sent to your email: "))
        if verify_otp(user_otp, original_otp):
            print("Authentication successful!")
        else:
            print("Invalid OTP. Authentication failed.")
    else:
        print("Failed to send OTP. Please try again.")
