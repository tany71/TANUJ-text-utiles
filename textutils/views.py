from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    global param
    djtext = request.POST.get("text", "default")
    # check which checkbox is on
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newline = request.POST.get("newline", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    # charcount = request.GET.get("charcount", "off")

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        param = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        param = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        param = {'purpose': 'New Line remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        param = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newline != "on" and extraspaceremover != "on":
        return HttpResponse("Please Select any Opration and Try again Later")

    return render(request, 'analyze.html', param)
