from django.http import HttpResponse
from django.shortcuts import render , redirect
from datetime import datetime
from techapp.models import Contact

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(email=email,password=password,date=datetime.today())
        contact.save()

    return render(request, 'index.html')
