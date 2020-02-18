from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    print("abcd")
    return render(request, 'index.html')
    