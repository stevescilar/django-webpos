from django.shortcuts import render

# Create your views here.
# only working
def index(request):
    return render (request,'index.html')