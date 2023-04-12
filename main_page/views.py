from twilio.base.exceptions import TwilioRestException
from .models import Enquiry
from django.shortcuts import render
from django.shortcuts import render, redirect
from twilio.rest import Client
from django.urls import reverse

from django.utils import timezone
from datetime import datetime, timedelta

from django.http import FileResponse
from django.conf import settings
import os
# Create your views here.


def home(request):
    # Get the current time in the server's timezone
    now = timezone.now()

    # Calculate the datetime of the next countdown end
    countdown_end = now + timedelta(days=7) - timedelta(seconds=1)
    # Calculate the time remaining until the countdown end
    remaining_time = countdown_end - now
    # Pass the remaining time to the template

    # Calculate the remaining days, hours and minutes
    remaining_days = remaining_time.days
    remaining_hours, remainder = divmod(remaining_time.seconds, 3600)
    remaining_minutes, remaining_seconds = divmod(remainder, 60)

    # Pass the remaining time to the template
    context = {
        'remaining_days': remaining_days,
        'remaining_hours': remaining_hours,
        'remaining_minutes': remaining_minutes,
    }

    return render(request, 'home.html', context)


def send_sms(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')

        # Send the SMS message using Twilio
        try:
            account_sid = 'ACcf41e466ed5bd377f0c14a3f217bdac6'
            auth_token = '98dab3c4e1fc909bc4e265353a109e0e'
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                    body=f'New message from {name}, mobile number: {mobile}',
                    from_='+15075686859',
                    to='+919152091676'
                )
        except TwilioRestException as e:
            # Handle exception
            return render(request, 'error.html', {'error': e})

        # Redirect to home page and show popup
        return render(request, 'success.html')

    return render(request, 'home.html')


def submit_enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        experience = request.POST.get('experience')
        education = request.POST.get('education')
        comments = request.POST.get('comments')

        enquiry = Enquiry(name=name, email=email, phone=phone, country=country,
                          experience=experience, education=education, comments=comments)
        enquiry.save()

        # later, create a success page

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
