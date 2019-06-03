from django.shortcuts import render, redirect
from login.forms import UserForm,UserProfileInfoForm
from login.models import UserProfileInfo
from datetime import *
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from pytz import timezone
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *
from .forms import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers


def getAllEqps(request):
    lstEquipments = Equipments.objects.all()
    lstSerialize = []
    for eqp in lstEquipments:
        s = EquipmentsSerializer(eqp)
        print(s.data)
        lstSerialize.append(s.data)
    return JsonResponse(lstSerialize, safe=False)

def getAllEqpReqs(request):
    lstEquipmentRequests = EquipmentRequest.objects.all()
    data = list(lstEquipmentRequests.values())
    return JsonResponse(data, safe=False)

def checkAvailability(request,reqId):
    penReq = EquipmentRequest.objects.get(reqId=int(reqId,10))
    availability = penReq.eqp.eqpQuantity- penReq.eqp.eqpQuantityTaken
    print('availability',availability)
    return JsonResponse(availability, safe=False)
