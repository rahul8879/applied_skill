from django.shortcuts import render
from django.shortcuts import render, redirect
from twilio.rest import Client
from django.urls import reverse

from django.http import FileResponse
from django.conf import settings
import os
# Create your views here.


def home(request):
    return render(request,'home.html')

from twilio.base.exceptions import TwilioRestException

def send_sms(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')

        # Send the SMS message using Twilio
        try:
            account_sid = 'AC30ea225fb3d74b63c9368b5e593e5572'
            auth_token = '3c2fabcd0e07d6f70fb336934272922f'
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                    body=f'New message from {name}, mobile number: {mobile}',
                    from_='+15076232533',
                    to='+919152091676'
                )
        except TwilioRestException as e:
            # Handle exception
            return render(request, 'error.html', {'error': e})
        
        # Redirect to home page and show popup
        return render(request, 'home.html')
    
    return render(request, 'home.html')


from django.shortcuts import render
from .models import Enquiry

def submit_enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        experience = request.POST.get('experience')
        education = request.POST.get('education')
        comments = request.POST.get('comments')

        enquiry = Enquiry(name=name, email=email, phone=phone, country=country, experience=experience, education=education, comments=comments)
        enquiry.save()

        #later, create a success page

        return render(request, 'home.html')

    return render(request, 'home.html')


def cancel_sms(request):
    # Redirect to home page
    return redirect(reverse('home'))



def download_csv(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'Applied_skill_ds.csv')
    with open(file_path, 'rb') as f:
        response = FileResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        return response