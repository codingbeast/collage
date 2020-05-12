from django.shortcuts import render,HttpResponse,redirect
import validators
from . import helper
# Create your views here.
def home(request):
    return HttpResponse("hello world")
def frenq(request):
    return render(request,"frenq.html")
def result(request):
    if request.method == "POST":
        url=request.POST['url']
        if not validators.url(url):
            return redirect("frenq")
        if helper.dataisavailable(url):
            fdata=[]
            temp=helper.getdata(url)
            for i in temp:
                ss=(i.word,i.count)
                fdata.append(ss)
            dnotice="From Database"
        else:
            dnotice="Freshly Processed"
            fdata=helper.CompleteLogic(url)
            for i,j in fdata:
                mydict={
                    "url": url,
                    "word": i,
                    "count": j
                }
                helper.dbinsert(mydict)
        
        return render(request,"result.html",context={
            "frenq" : fdata,
            "datanotice": dnotice
            })
        



    else:
        return redirect("frenq")
