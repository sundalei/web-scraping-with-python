import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

mail_host = 'smtp.163.com'
mail_user = 'sundalei2011@163.com'
mail_password = 'YTKPXXRKISOTASSV'

sender = 'sundalei2011@163.com'
receivers = ['sundalei1988@gmail.com']

def send_mail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = '{}'.format(sender)
    msg['To'] = ','.join(receivers)
    
    s = smtplib.SMTP('')
    s.connect(mail_host, 25)
    s.login(mail_user, mail_password)
    s.send_message(msg)
    s.quit()

bs = BeautifulSoup(urlopen('https://isitchristmas.com/'), 'html.parser')
while(bs.find('a', {'id':'answer'}).attrs['title'] == 'NO'):
    print('It is not Christmas yet.')
    time.sleep(3600)
    bs = BeautifulSoup(urlopen('https://isitchristmas.com/'), 'html.parser')

send_mail('It\'s Christmas!', 'According to http://itischristmas.com, it is Christmas!')