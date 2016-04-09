# -*- coding:UTF-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr

EMAIL_ADDRESS = 'tj_island@163.com'
EMAIL_PASSWORD = 'ying1997'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def sendEmail(toAddr, fare = '0'):
    msg = MIMEText('<h1>充电费啦!!!</h1><br><p>还有<strong>' + fare + '</strong>' + '元</p><br>', 'html', 'utf-8')
    msg['From'] = _format_addr(u'island <tj_island@163.com>')
    msg['To'] = _format_addr(u'傻鸡们 <囧>')
    msg['Subject'] = Header(u'充电费啦!!!!!', 'utf-8').encode()

    server = smtplib.SMTP('smtp.163.com', 25)
    server.set_debuglevel(1)
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail('From: tj_island@163.com', [toAddr], msg.as_string())
    server.quit()

# sendEmail('764796124@qq.com')
