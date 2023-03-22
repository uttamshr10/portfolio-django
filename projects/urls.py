from django.urls import path
from projects import views

urlpatterns =[
    path('home', views.uttam, name = 'uttam')
]
