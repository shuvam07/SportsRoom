from django.conf.urls import url
from SportsEquipment import views
from django.urls import path

app_name = 'SportsEquipment'

urlpatterns = [
    path('home/',views.home,name='home'),
    path(r'eqpRequest/',views.eqpRequest,name='eqpRequest'),
    path(r'pendingRequest/',views.pendingRequest,name='pendingRequest'),
    path(r'approvedRequest/',views.approvedRequest,name='approvedRequest'),
    path(r'processRequest/$',views.processRequest,name='processRequest'),
    path(r'processReturnRequest/$',views.processReturnRequest,name='processReturnRequest'),
    path(r'viewRequest/$',views.viewRequest,name='viewRequest'),
]
