from django.shortcuts import render

# Create your views here.
def add_hotel(request):
    return render(request,'add_hotel.html')
def add_package(request):
    return render(request,'add_package.html')
def add_plane(request):
    return render(request,'add_plane.html')
def view_hotel(request):
    return render(request,'view_hotel.html')
def view_packages(request):
    return render(request,'view_packages.html')
def view_plane(request):
    return render(request,'view_plane.html')

