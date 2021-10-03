from django.urls import path
from . import views


urlpatterns = [

    path('address/',views.address,name='address'),
    path('email/',views.email,name='email'),
    path('phone/',views.phone,name='phone'),
    path('fib/',views.print_fibonachi,name='print_fibonachi'),
    path('fib/<int:m>/', views.print_fibonachiN,name='print_fibonachi'),
    path('details',views.details,name='details')



    
]