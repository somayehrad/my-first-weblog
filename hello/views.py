from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_salam(request):
    return HttpResponse("سلام")

def bye(request):
    return HttpResponse("خداحافظ")


def print_factorial(request):
    s=""
    for i in range(1,1001):
       s+= f"<br>{i}! = {get_factorial(i)}"
    return HttpResponse(s)

def get_factorial(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r