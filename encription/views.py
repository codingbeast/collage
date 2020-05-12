from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
	if request.method == request.GET:
		return render(request,"encresult.html")
	return render(request,"encindex.html")

def result(request):
	return HttpResponse("ihi")
