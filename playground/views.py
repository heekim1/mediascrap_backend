
from django.core.mail import EmailMessage, send_mail, mail_admins, BadHeaderError
from templated_mail.mail import BaseEmailMessage

from django.shortcuts import render
from django.http import HttpResponse
from .tasks import notify_customers

def say_hello(request):
    notify_customers.delay("I am saying hello")
    return render(request, 'hello.html', {'name': 'Hee'})


def send_email(request):
    try:
        #send_mail('subject','message','info@ecars.com',['bob@ecars.com','heekim1@gmail.com'])
        #mail_admins('subject','message', html_message='message')
        """
        message = EmailMessage('subject','message',
                               'from@ecars.com', ['bob@ecars.com','heekim1@gmail.com'])
        message.attach_file('playground/static/images/mycar.jpeg')
        message.send()
        """
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Hee'}
        )
        message.send(['heekim1@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
