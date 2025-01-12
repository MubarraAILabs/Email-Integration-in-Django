from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def emailDemo(request):
    if request.method == 'POST':
        subject = 'Booking order'
        email_body = 'order get placed'
        from_email = settings.EMAIL_HOST_USER
        
        send_mail(subject=subject, message = email_body, from_email = from_email, recipient_list = ['mubarra.dev@gmail.com'])
        return HttpResponse('Email sent successfully!')
        
    else:
        return render(request,'form.html')