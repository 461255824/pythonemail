import smtplib
from email.mime.text import MIMEText
msg_from='461255824@qq.com'
passwd='xacyvowfqbnubijg001'
msg_to='yangqiyan_iov@chinamobile.com'

subject="python邮件测试"
hello = "这是我使用python smtplib及email模块发送的邮件"
msg = MIMEText(hello)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except s.SMTPException:
    print ("发送失败")
finally:
    s.quit()