from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')

def short(request):
    long_url = request.GET['long_url']
    response=requests.post('https://cleanuri.com/api/v1/shorten', data={'url':long_url}).json()
    return render(request, 'result.htm', {'response':response['result_url']})