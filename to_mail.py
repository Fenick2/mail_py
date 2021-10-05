import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv


load_dotenv()


def send_email(message):
    sender = "fenikk@gmail.com"
    password = os.getenv("GMAIL_PASS")
    receiver = 'fenick2@yandex.ru'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'Прочти меня!'
        server.sendmail(sender, receiver, msg.as_string())

        # server.sendmail(sender, 'fenick@ya.ru', f"Subject: HI THERE!\n{message}")

        return 'The message was sent successfully!'
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password!"


def main():
    message = input('Type your message: ')
    print(send_email(message=message))


if __name__ == '__main__':
    main()
