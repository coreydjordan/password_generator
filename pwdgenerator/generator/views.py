from django.shortcuts import render
from django.http import HttpResponse
import string
import random
# Create your views here.

def home(request):
    # return HttpResponse('hello world')
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    chars = list(string.ascii_lowercase)
    
    if request.GET.get('uppercase'):
        chars.extend(list(string.ascii_uppercase))
    
    if request.GET.get('numbers'):
        chars.extend(list(string.digits))
        
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()'))
    
    length = int(request.GET.get('length'))
    
    pwd = ''
    
    for i in range(length):
        pwd += random.choice(chars)
    return render(request, 'generator/password.html', {'password': pwd})
