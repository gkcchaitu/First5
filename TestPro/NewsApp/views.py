from django.shortcuts import render

from django.shortcuts import HttpResponse
def Home(request):
    context={ "name" : "chaitu"}
    return render(request,'home.html',context)

def News(request):
    return render(request, 'news.html')

def Contact(request):
    return render(request, 'contact.html')
