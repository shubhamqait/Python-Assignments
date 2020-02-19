# I have created this website
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
   
def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    #Check checkbox values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params) 

    elif(newlineremover == 'on'):
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose':'Remove New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover == "on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Remove New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(charcount == "on"):
        analyzed=0
        for x in djtext:
            if x == " ":
                pass
            else:
                analyzed = analyzed + 1
        countString = "Total Character Count-"+str(analyzed)
        params = {'purpose':'Charactor Count', 'analyzed_text': countString}
        return render(request, 'analyze.html', params)

    else: 
        return HttpResponse("Error")