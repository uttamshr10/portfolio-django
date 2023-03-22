from django.shortcuts import render

# Create your views here.
def uttam(request):
    return render(request, 'projects/index.html')
