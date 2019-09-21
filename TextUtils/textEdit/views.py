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
    print(removepunc)
    print(djtext)

    if removepunc=="on":
        punctuations  = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': "Remove Punctuations" , 'analyzed_text': analyzed }
    #analyze thetext
        return render(request , 'analyze.html' , params)
    elif(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Convert text into upper case" , 'analyzed_text': analyzed }
    #analyze thetext
        return render(request , 'analyze.html' , params)

    elif(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char !='\n':
                analyzed = analyzed + char
        
        params = {'purpose': "Remove newLine" , 'analyzed_text': analyzed }
    #analyze thetext
        return render(request , 'analyze.html' , params)

    elif(extraspaceremover=='on'):
        analyzed=""
        for index , char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': "Extra Space Remove" , 'analyzed_text': analyzed }
    #analyze thetext
        return render(request , 'analyze.html' , params)  

    elif(countChar=='on'):
        analyzed=0
        for char in djtext:
            analyzed=analyzed+1
        params = {'purpose': "Extra Space Remove" , 'analyzed_text': analyzed }
    #analyze thetext
        return render(request , 'analyze.html' , params)  
        


    else:
        return HttpResponse("Error")

'''
def removepunc(request):
    #get the text
    djtext = (request.GET.get('text','default'))
    print(djtext)
    #analyze thetext
    return HttpResponse("<h1>removepunc</h1><br> <a href='/'>Back</a>")


def capitalizefirst(request):
    return HttpResponse("<h1> capitalizefirst</h1> <br> <a href='/'>Back</a>")


def newlineremove(request):
    return HttpResponse(" <h1> newlineremove</h1><br> <a href='/'>Back</a>")


def spaceremove(request):
    return HttpResponse(" <h1> spaceremove</h1><br> <a href='/'>Back</a>")


def charcount(request):
    return HttpResponse(" <h1> char count</h1><br> <a href='/'>Back</a>")

'''