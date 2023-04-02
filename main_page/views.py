from django.shortcuts import render
from django.shortcuts import render, redirect
from twilio.rest import Client
# Create your views here.


def home(request):
    return render(request,'home.html')

def send_sms(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        
        # Send the SMS message using Twilio
        # account_sid = 'your_account_sid'
        account_sid = 'AC30ea225fb3d74b63c9368b5e593e5572'
        auth_token = '3c2fabcd0e07d6f70fb336934272922f'
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                             body=f'New message from {name}, mobile number: {mobile}',
                             from_='+15076232533',
                             to='+919152091676'
                         )
        
        # Redirect to home page and show popup
        return render(request, 'home.html')
    return render(request, 'home.html')