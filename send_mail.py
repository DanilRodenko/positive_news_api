import smtplib

def send_mail(message):
    user = "rodenko.d96@gmail.com"
    passwd = "vhdfhpnglrvwelsd"

    server = "smtp.gmail.com"
    port = 587

    receiver = "rodenko.d96@gmail.com"


    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.ehlo()

    smtp.login(user, passwd)

    smtp.sendmail(user, receiver, message.encode('utf-8'))




