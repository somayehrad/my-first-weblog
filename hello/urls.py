from django.urls import path
from . import views




urlpatterns = [
    path('',views.view_salam,name='view_salam'),
    path('bye/',views.bye,name='view_bye'),
    path('f',views.print_factorial,name='print_factorial')

]

