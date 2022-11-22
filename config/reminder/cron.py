from .models import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def reminder_mail():
    obj = Reminders.objects.filter(is_sent=False)
    
    if obj:
        for i in obj:
            if i.should_sent() and not i.is_completed():
                i.is_sent = True
                i.save()
                
                header = 'Django Reminder App'
                html_message = render_to_string('reminder/email.html', {'data': i})
                plain_message = strip_tags(html_message)
                
                send_mail(header, plain_message, 
                        settings.EMAIL_HOST_USER, 
                        [i.author.email], 
                        fail_silently=False, html_message=html_message)