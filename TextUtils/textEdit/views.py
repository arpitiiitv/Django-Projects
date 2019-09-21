from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    params = {'name' : 'Arpit' , 'place' : 'Kanpur'}
    return render(request , 'index.html',params)

## Analyzing text
def analyze(request):
    #get the text
    djtext = (request.GET.get('text','default'))
    removepunc =  (request.GET.get('removepunc','off'))
    fullcaps =(request.GET.get('fullcaps','off'))
    newlineremover =(request.GET.get('newlineremover','off'))
    extraspaceremover =(request.GET.get('extraspaceremover','off'))
    countChar =(request.GET.get('countChar','off'))
    
    print(djtext)

    if removepunc=="on":
        punctuations  = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': "Remove Punctuations" , 'analyzed_text': analyzed }
        djtext=analyzed
    
    if(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Convert text into upper case" , 'analyzed_text': analyzed }
        djtext=analyzed
    
    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char
        
        params = {'purpose': "Remove newLine" , 'analyzed_text': analyzed }
        djtext=analyzed
    
    if(extraspaceremover=='on'):
        analyzed=""
        for index , char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': "Extra Space Remove" , 'analyzed_text': analyzed }
        djtext=analyzed
    
    if(countChar=='on'):
        analyzed=0
        for char in djtext:
            analyzed=analyzed+1
        params = {'purpose': "Extra Space Remove" , 'analyzed_text': analyzed }
    else:
        params = {'purpose': "No operation " , 'analyzed_text': djtext }
    return render(request , 'analyze.html' , params)       


