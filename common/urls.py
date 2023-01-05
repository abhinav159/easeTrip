from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [

    path('commonhome',views.commonhome, name='commonhome'),
    path('agency_login',views.agency_login, name='agency_login'),
    path('traveller_login',views.traveller_login, name= 'traveller_login'),
    path('agency_reg',views.agency_reg, name='agency_reg'),
    path('traveller_reg',views.traveller_reg, name = 'traveller_reg'),
]