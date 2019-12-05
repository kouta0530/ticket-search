
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import search
import time

@csrf_protect
# Create your views here.

def index(request):
    return render(request,'index.html')

def hello(request):
    key = request.POST.get("search")
    time.sleep(1)
    list = search.search_live_pocket(key)
    time.sleep(1)
    list2 = search.search_street(key)
    #list3 = search.search_e_plus(key)
    
    list.extend(list2)
    #list.extend(list3)
    
    lives = {"datas":list,}
    
    return render(request,'index.html',lives)