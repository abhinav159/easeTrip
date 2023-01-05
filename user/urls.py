from django.urls import path
from . import views

app_name = 'ease_ad'

urlpatterns = [
    path('book_now',views.book_now, name='book_now'),
    path('book_package',views.book_package, name='book_package'),
    path('book_room',views.book_room, name='book_room'),
    path('flight_details',views.flight_details, name='flight_details'),
    path('flight_list',views.flight_list, name='flight_list'),
    path('hotel_details',views.hotel_details, name='hotel_details'),
    path('hotel_list',views.hotel_list, name='hotel_list'),
    path('package_details',views.package_details, name='package_details'),
    path('packages',views.packages, name='packages'),
]