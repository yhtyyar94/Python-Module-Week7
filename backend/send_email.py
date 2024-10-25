import smtplib
from email.mime.text import MIMEText


def send_email(sender_email, receiver_email, password, message):
    email = MIMEText(message, "plain")
    email["From"] = sender_email
    email["To"] = receiver_email

    try:
        # SMTP sunucusuna bağlan
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Güvenli bağlantı kur

        # Giriş yap
        server.login(sender_email, password)

        # Email gönder
        server.sendmail(sender_email, receiver_email, email.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
    finally:
        # Sunucudan çıkış yap
        server.quit()
