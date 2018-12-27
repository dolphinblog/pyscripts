# 直接命令行输入
export MAIL_USERNAME=网易邮箱
export MAIL_PASSWORD=授权码

# 发信客户端配置
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True

# Python shell中输入
from flask_mail import Message
from hello import mail
msg = Message('邮件标题', sender='网易邮箱', recipients=['收件邮箱'])
msg.body = '邮件内容'
msg.html = '邮件正文，支持html'
with app.app_context():
    mail.send(msg)
    