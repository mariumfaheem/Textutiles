from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')

def analyze(request):
    text = request.POST.get('text', 'default')
    fullcaps=request.POST.get('fullcaps','off')
    removepun=request.POST.get('removepunc','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')


    print(removepun)
    if removepun=="on":
        punctuation_list='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyze=""
        for char in text:
            if char not in punctuation_list:
                analyze=analyze+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyze}
        text=analyze

    if (fullcaps=="on"):
        analyze = text.upper()
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyze}
        text = analyze

    if (newlineremover == "on"):
        analyze = ""
        for char in text:
            if char !='\n' and char !='\r':
                analyze = analyze + char
        params = {'purpose': 'Line is Removed', 'analyzed_text': analyze}
        text = analyze


    if (extraspaceremover == "on"):
        analyze = ""
        for index,char in enumerate(text):
            if text[index]== " " and text[index+1]==" ":
                pass
            else:
                analyze = analyze + char
        params = {'purpose': 'Space is Removed', 'analyzed_text': analyze}
        text = analyze

    if(charcount=='on'):
        analyze=""
        analyze=len(text)
        params = {'purpose': 'Character Count', 'analyzed_text': analyze}
        text = analyze

    if(charcount=='off' and extraspaceremover=='off' and removepun=='off' and  fullcaps=='off' and newlineremover=='off'):
        return HttpResponse('Error')


    return render(request, 'analyze.html', params)



def capitalizefirst(request):
    return HttpResponse("capitalizefirst")


def newlineremove(request):
    return HttpResponse("newlineremove")


def spaceremove(request):
    return HttpResponse("spaceremove")


def charcount(request):
    return HttpResponse("charcount")

