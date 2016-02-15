# coding=utf-8


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def mail(user):
    ret = True
    try:
        msg = MIMEText('使用python發送郵件，非常方便！！！', 'plain', 'utf-8')
        msg['from'] = formataddr(['smile', 'shen_wandong@163.com'])
        msg['To'] = formataddr(['Hello', '844843463@qq.com'])
        msg['Subject'] = "Email"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("shen_wandong@163.com", "jeiidde520")
        server.sendmail("shen_wandong@163.com", [user, ], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret


ret = mail('80470335@qq.com')
ret = mail('844843463@qq.com')
ret = mail("shen_wandong@163.com")
if ret:
    print("發送成功")
else:
    print("發送失敗")
