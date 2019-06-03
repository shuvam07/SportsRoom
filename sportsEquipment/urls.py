from django.conf.urls import url
from sportsEquipment import views,apiviews
from django.urls import path,include
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'eqpmnts', apiviews.EquipmentsViewSet)
# router.register(r'eqpmntsList', apiviews.EquipmentRequestViewSet)

app_name = 'sportsEquipment'
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
urlpatterns = [
    # Return view response
    path('home/',views.home,name='home'),
    path(r'eqpRequest/',views.eqpRequest,name='eqpRequest'),
    path(r'pendingRequest/',views.pendingRequest,name='pendingRequest'),
    path(r'approvedRequest/',views.approvedRequest,name='approvedRequest'),
    path(r'checkAvailability/',views.checkAvailability,name='checkAvailability'),
    path(r'processRequest/',views.processRequest,name='processRequest'),
    path(r'processReturnRequest/',views.processReturnRequest,name='processReturnRequest'),
    path(r'viewRequest/',views.viewRequest,name='viewRequest'),
    path(r'addEquip/',views.addEquip,name='addEquip'),
    path(r'viewEquipList/',views.viewInventory,name='viewEquipList'),
    path(r'editEquipList/(?P<pk>\d+)',views.editEquipList,name='editEquipList'),
    path(r'deleteEqp/(?P<pk>\d+)',views.deleteEqp,name='deleteEqp'),
    path(r'penalty/',views.penalty,name='penalty'),
    # View response

    # Return API response
    path(r'getAllEqps/',apiviews.getAllEqps,name='getAllEqps'),
    path(r'getAllEqpReqs/',apiviews.getAllEqpReqs,name='getAllEqpReqs'),
    path(r'checkAvailability/<reqId>',apiviews.checkAvailability,name='checkAvailability')
    # API response
]
