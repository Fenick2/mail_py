import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv


load_dotenv()


def send_email():
    sender = "fenikk@gmail.com"
    password = os.getenv("GMAIL_PASS")
    receiver = 'fenick2@yandex.ru'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    with open('index.html') as file:
        text = file.read()

    try:
        server.login(sender, password)
        msg = MIMEText(text, 'html')
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = 'Прочти меня!'
        server.sendmail(sender, receiver, msg.as_string())

        return 'The message was sent successfully!'
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password!"


def main():
    print(send_email())


if __name__ == '__main__':
    main()
