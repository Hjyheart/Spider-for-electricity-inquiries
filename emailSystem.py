# -*- coding:UTF-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr

# email地址和smtp授权密码 一般不是你的邮箱密码
EMAIL_ADDRESS = ''
EMAIL_PASSWORD = ''

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def sendEmail(toAddr, fare = '0'):
    msg = MIMEText('<h1>充电费啦!!!</h1><br><p>还有<strong>' + fare + '</strong>' + '元</p><br>', 'html', 'utf-8')
    # From要和你的邮箱对上
    msg['From'] = _format_addr(u'island <>')
    msg['To'] = _format_addr(u'傻鸡们 <囧>')
    msg['Subject'] = Header(u'充电费啦!!!!!', 'utf-8').encode()

    server = smtplib.SMTP('smtp.163.com', 25)
    server.set_debuglevel(1)
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    # 要对上发件箱
    server.sendmail('From: ', [toAddr], msg.as_string())
    server.quit()

