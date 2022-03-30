from django.shortcuts import render

# Create your views here.
# only working

def webPos(request):
    context = {}
    return render (request,'dashboard/webpos.html',context)