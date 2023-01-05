from django.urls import path
from . import views

app_name = 'ease_adm'

urlpatterns = [

    path('add_hotel',views.add_hotel, name ='add_hotel'),
    path('add_package',views.add_package, name ='add_package'),
    path('add_plane',views.add_plane, name ='add_plane'),
    path('view_hotel',views.view_hotel, name ='view_hotel'),
    path('view_packages',views.view_packages, name ='view_packages'),
    path('view_plane',views.view_plane, name ='view_plane'),
]