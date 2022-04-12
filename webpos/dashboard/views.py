from django.shortcuts import render

# Create your views here.
# only working
def home (request):
    return render (request,'dashboard/home.html')
def webPos(request):
    context = {}
    return render (request,'dashboard/webpos.html',context)