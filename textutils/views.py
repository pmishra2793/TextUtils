# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyzedText(request):
    vText = request.POST.get('textVal', 'default')
    vCb_removepunc = request.POST.get('cb_removepunc')
    vCb_uppercase = request.POST.get('cb_uppercase')
    vCb_newlineremover = request.POST.get('cb_newlineremover')
    vCb_extraspaceremover = request.POST.get('cb_extraspaceremover')
    vCb_countelength = request.POST.get('cb_countelength')
    print (vCb_removepunc)
    print (vText)
    # Remove Punctuations
    if vCb_removepunc == "on":
        print ('Inside vCb_removepunc')
        punctuation = '''~`!@#$%^&*(){}[]?/|\><.:;'''
        vAnalyzedText = ''
        for char in vText:
            print ('char = ',char)
            if char not in punctuation:
                vAnalyzedText = vAnalyzedText + char
                print (vAnalyzedText)
        vText = vAnalyzedText
        params = {'purpose':'Remove Punctuations','Analyzed_text':vAnalyzedText}
        # return render(request,'analyzed.html',params)
    # UPPER CASE
    if(vCb_uppercase == "on"):
        vAnalyzedText = ''
        for char in vText:
            vAnalyzedText = vAnalyzedText + char.upper()
        vText = vAnalyzedText
        params = {'purpose':'UPPER CASE','Analyzed_text':vAnalyzedText}
        # return render(request,'analyzed.html',params)
    # New Line Remover
    if(vCb_newlineremover == "on"):
        print ('vCb_newlineremover = ',vCb_newlineremover)
        vAnalyzedText = ''
        for char in vText:
            if char != "\n" and char != "\r":
                vAnalyzedText = vAnalyzedText + char
        vText = vAnalyzedText
        params = {'purpose':'New Line Remover','Analyzed_text':vAnalyzedText}
        # return render(request,'analyzed.html',params)
    # Extra Space Remover
    if(vCb_extraspaceremover == 'on'):
        vAnalyzedText = ''
        for index, char in enumerate(vText):
            if vText[index] == ' ' and vText[index+1] == ' ':
                print ('**********',vText[index])
                print ('===========',vText[index+1])
                pass
            else:
                vAnalyzedText = vAnalyzedText + char
        vText = vAnalyzedText
        params = {'purpose':'Remove Extra Space','Analyzed_text':vAnalyzedText}
        # return render(request,'analyzed.html',params)
    # Length Count
    if(vCb_countelength == 'on'):
        vAnalyzedText = 0
        punctuation = '''~`!@#$%^&*(){}[]?/|\><.:;'''
        number = '''1,2,3,4,5,6,7,8,9,0'''
        for char in vText:
            if char != ' ' and char not in punctuation and char not in number:
                vAnalyzedText = vAnalyzedText + 1
        params = {'purpose': 'Character Count', 'Analyzed_text': vAnalyzedText}

    if(vCb_removepunc != "on" and vCb_uppercase != "on" and vCb_newlineremover != "on" and vCb_extraspaceremover != "on" and vCb_countelength != "on"):
        return HttpResponse('Please selected at least One Options')

    return render(request, 'analyzed.html', params)









# def removepunc(request):
#     return HttpResponse("removepunc")
#
#
# def capfirst(request):
#     return HttpResponse("caplitalizerfirst")
#
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
#
# def spaceremove(request):
#     return HttpResponse("spaceremove")
#
#
# def charcount(request):
#     return HttpResponse("charcount")

