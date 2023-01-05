from django.shortcuts import render

# Create your views here.
def book_now(request):
    return render(request,'book_now.html')
def book_package(request):
    return render(request,'book_package.html')
def book_room(request):
    return render(request,'book_room.html')
def flight_details(request):
    return render(request,'flight_details.html')
def flight_list(request):
    return render(request,'flight_list.html')
def hotel_details(request):
    return render(request,'hotel_details.html')
def hotel_list(request):
    return render(request,'hotel_list.html')
def package_details(request):
    return render(request,'package_details.html')
def packages(request):
    return render(request,'packages.html')