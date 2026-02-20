from django.shortcuts import render
from tours.models import TourPackage

# Create your views here.

def home(request):
    packages = TourPackage.objects.all()[:6]
    return render(request, 'pages/home.html', {"packages": packages})

