# *_*coding:utf-8 *_*
#导入 smtplib 发邮件模块
import smtplib
import time
import os
#导入 email 模块，MIMEText 和 Header 主要用来完邮件内容与邮件标题的定义

from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#发送邮箱
sender = '18435122843@163.com'
#接收邮箱
receiver = 'hanym@lierda.com'
#发送邮件主题
subject = '你好'
#发送邮箱服务器
smtpserver = 'smtp.163.com'
#发送邮箱用户/密码
username = '18435122843@163.com'
password = 'hanyanmei86'
#中文需参数‘utf-8’，单字节字符不需要
msg = MIMEText('<h1>你好!请查收邮件</h1>','text','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From']='18435122843@163.com'
msg['To']='hanym@lierda.com'
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()


#定义发送邮件
def sentmail(file_new):
    #发信邮箱
    mail_from = '18435122843@163.com'
    #收信邮箱
    mail_to = 'hanym@lierda.com'
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=u"测试报告" #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp.connect('smtp.126.com')
    #用户名密码
    smtp.login('18435122843@163.com','hanyanmei86')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'email has send out !'
#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'D:\\selenium_python\\report'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print file_new
    #调用发邮件模块
    sentmail(file_new)
if __name__ == "__main__":
    #执行测试用例
    runner.run(alltestnames)
    #执行发邮件
    sendreport()