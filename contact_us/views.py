from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def address(request):
    return HttpResponse("address")

def email(request):
    return HttpResponse("email")

def phone(request):
    return HttpResponse("phone")


def get_fib(n):
    if n==1 or n==2:
        return 1
    f=[0,1,1]
    for i in range(3,n+1):
        f.append(sum(f[-2:]))
    return f
def get_fibN(n):
    f=get_fib(n)
    return f[-1]
def print_fibonachi(request):
    f=get_fib(1000)
    s=""
    for i in f:
        s+=str(i)+"<br>"
    return HttpResponse(s) 
def print_fibonachiN(request,m):
    f=get_fibN(m)
    return HttpResponse(str(f))




def details(request):
    return render(request,'hello\details.html',{})



