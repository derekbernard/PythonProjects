import smtplib
from email.mime.text import MIMEText

class Bot():
    def __init__(self):
        print("Bot starting")
        email = 'realestatebotalert@gmail.com'
        password = 'darkderek42'
        content = "https://duproprio.com/en/laval/vimont/semi-detached-for-sale/hab-2294-casault-897766#description"
        content = MIMEText(content ,'html')
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.ehlo()

        server.login(email,password)

        server.sendmail(email,'derekbernard@hotmail.com',content.as_string())
        server.close()
        print("email sent")
        

    
    

bot = Bot()

