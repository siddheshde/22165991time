import os
import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BirthdateForm, SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from pathlib import Path




def calculate_age(request):
    if request.method == 'POST':
        form = BirthdateForm(request.POST)
        if form.is_valid():
            birthdate = form.cleaned_data['birthdate']
            response = requests.get(f'https://sgki2tax58.execute-api.us-east-1.amazonaws.com/getSidd?birthdate={birthdate}')
            age_data = response.json()
            return render(request, 'calculator/results.html', {'age_data': age_data})
    else:
        form = BirthdateForm()

    return render(request, 'calculator/home.html', {'form': form})



def days_countdown(request):
    # Assuming you're taking the dates as input from GET parameters or form submission
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        api_url = 'https://vxej5md2q9.execute-api.eu-west-1.amazonaws.com/default/x22208038-dayscountdown'
        params = {'start_date': start_date, 'end_date': end_date}
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            countdown_data = response.json()
            # Now countdown_data contains the response from the API
            # Render it in a template or return it as JSON
            return render(request, 'calculator/results.html', {'countdown_data': countdown_data})
        else:
            # Assuming you want to display errors on the home page
            return render(request, 'calculator/s', {'error': 'API request failed.'})
    else:
        # Render the date input form if dates are not provided
        return render(request, 'calculator/days_countdown.html')
    


# Sign Up View
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('calculator/home')  # Redirect to a home page
    else:
        form = SignUpForm()
    return render(request, 'calculator/signup.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('calculator/home')  # Redirect to a home page
    else:
        form = LoginForm()
    return render(request, 'calculator/login.html', {'form': form})





def astrology_facts_view(request):
    # Ensure that 'astrology_facts.json' exists within 'calculator/static/'
    file_path = Path(settings.STATICFILES_DIRS[0]) / 'astrology_facts.json'
    with open(file_path, 'r') as file:
        facts = json.load(file)
    return render(request, 'calculator/astrology_facts.html', {'facts': facts})







# Make sure to include your other view functions as well
