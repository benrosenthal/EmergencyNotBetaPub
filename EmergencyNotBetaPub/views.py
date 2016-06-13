from flask import Flask
from flask_mail import Mail, Message
from twilio.rest import TwilioRestClient


app = Flask(__name__)


app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = '**********',
    MAIL_PASSWORD = '*********'
    )

mail = Mail(app)

#Attempt to send email to specified recipient(s)
@app.route('/')
def send_notifacation():
    try:
        send_email()
        send_sms()
        return "Email and SMS Sent!"
    except Exception as e:
        return(str(e))


def send_email():
    msg = Message("Send Mail Tutorial!",
          sender="email@gmail.com",
          recipients=["email.programming@gmail.com"])
    msg.body = "Yo!\nHave you heard the good word of Python???"
    mail.send(msg)
    return 'Mail sent!'

def send_sms():
    account_sid = "************"
    auth_token = "***************"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+17189384847", from_="+************",
                                         body="Hello there!")
    return 'SMS Sent!'



if __name__ == "__main__":
    app.run()
