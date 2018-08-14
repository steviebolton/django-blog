from django.shortcuts import render
from .models import SalonService


# Create your views here.
def list_all_the_bloody_services(request):
    all_services = SalonService.objects.all()
    return render(request, "serv/list_services.html", {'services': all_services})