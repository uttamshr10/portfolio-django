from django.urls import path
from projects import views

urlpatterns =[
    path('uttam', views.uttam, name = 'uttam')
]
