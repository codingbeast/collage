from django.shortcuts import render,HttpResponse
from django.shortcuts import reverse
import requests
import json
def home(request):
    iptool = getdata()

    return render(request,"ip_index.html",context={"iptool": iptool})

def getdata():
    base="http://ip-api.com/json/"
    res = requests.get(base).json()
    return res

