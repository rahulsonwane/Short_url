from django.shortcuts import render
from django.http import  HttpResponse 
from root.models import Url
from django.shortcuts import render, redirect


# Create your views here.
def createUrl(request):
    if request.method == 'POST':
        full_url=request.POST.get('full_url')
        obj = Url.create(full_url)
        return render(request, 'root/index.html',{
            'full_url': obj.full_url,
            'short_url':request.get_host()+ '/' + obj.short_url
        })
    
    return render(request, 'root/index.html')


def routeToURL(request, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        obj = None
    
    return redirect(createUrl)