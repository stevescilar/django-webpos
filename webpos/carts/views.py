from django.shortcuts import render

# new cart.
def cart(request):
    return render(request,'store/cart.html')

