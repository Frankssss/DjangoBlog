__author__ = "Frank Shen"

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import ConfirmString


import hashlib


def hash_code(s, salt='MySite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def make_confirm_string(user):
    code = hash_code(user.email)
    ConfirmString.objects.create(code=code, user=user,)
    return code


def send_ack_mail(email, code):
    title = '注册确认'
    ip = '127.0.0.1:8000'
    text_content = '''感谢注册，专注于Python和Django技术的分享！\
        如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''
    html_content = f'''
        <p>感谢注册<a href="http://{ip}/user/confirm/?code={code}" target=blank>Frank's Blog</a>，\
        专注于Python和Django技术的分享！</p>
        <p>请点击站点链接完成注册确认！</p>
        <p>此链接有效期为{settings.CONFIRM_DAYS}天！</p>
        '''
    msg = EmailMultiAlternatives(title, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()