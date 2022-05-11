import random
import string

from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail
from random_id.utils import LENGTH


def sendmail(subject,template,to,context):
    subject='Subject'
    template_str='toll/'+template+'.html'
    html_message=render_to_string(template_str, {'data': context})
    html_message.attach('context.qr_code.url')
    plain_message=strip_tags(html_message)
    from_email='emailid'
    send_mail(subject,plain_message,from_email,[to],html_message=html_message)


def generate_random_string():
    """
    Generates random ID.
    """
    random_string = string.digits + string.ascii_uppercase
    new_id = ''.join([random.SystemRandom().choice(random_string) for i in range(random.randint(11, LENGTH))])
    return new_id


