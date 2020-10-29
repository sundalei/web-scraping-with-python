import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.163.com'
mail_user = 'sundalei2011@163.com'
mail_password = 'YTKPXXRKISOTASSV'

sender = 'sundalei2011@163.com'
receivers = ['sundalei1988@gmail.com']

msg = MIMEText('The body of the email is here')

msg['Subject'] = 'An Email Alert'
msg['From'] = '{}'.format(sender)
msg['To'] = ','.join(receivers)

s = smtplib.SMTP('')
s.connect(mail_host, 25)
s.login(mail_user, mail_password)
s.send_message(msg)
s.quit()