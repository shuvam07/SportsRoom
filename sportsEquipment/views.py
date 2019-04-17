from django.shortcuts import render, redirect
from login.forms import UserForm,UserProfileInfoForm
from login.models import UserProfileInfo
from datetime import *
from django.db import transaction


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *
from .forms import *

# Create your views here.

#method to render home page ater login
@login_required
def home(request):
    if request.user.is_superuser:
        totalPenalty = 0
    else:
        userProfile = UserProfileInfo.objects.get(user=request.user)
        totalPenalty = userProfile.totalPenalty
    return render(request,'home.html',{'totalPenalty': totalPenalty})

#method to perform an insert or update
@login_required
def insertOrUpdate(model):
    try:
        with transaction.atomic():
            model.save()
    except IntegrityError:
        handle_exception()

#method to make requests for equipments by students
@login_required
def eqpRequest(request):
    if(request.method == "POST"):
        if(request.user.is_authenticated):
            form = EqpmntRequestForm(request.POST)
            # print(form)
            # print(request.POST)
            myDict = dict(request.POST.items())
            # print(myDict)
            if form.is_valid():
                user1 = request.user
                equipmentRequest = EquipmentRequest()
                currentDateTime = datetime.today()
                requestedQuantity = request.POST['EqpQuantity']
                eqp = Equipments.objects.get(eqpId=int(request.POST['EqpName'],10))
                #Populating equipment request member wise
                print(requestedQuantity)
                print(eqp.eqpQuantity - eqp.eqpQuantityTaken)
                if (int(requestedQuantity) <= (eqp.eqpQuantity - eqp.eqpQuantityTaken)):
                    eqp.eqpQuantityTaken+=int(requestedQuantity)
                    insertOrUpdate(eqp)
                    equipmentRequest.quantity       = requestedQuantity
                    equipmentRequest.eqp            = eqp
                    equipmentRequest.user           = user1
                    equipmentRequest.dtOfRequest    = currentDateTime
                    equipmentRequest.dtAvailed      = datetime.today()
                    equipmentRequest.dtOfExpRet     = currentDateTime + timedelta(days=7)
                    insertOrUpdate(equipmentRequest)
                    return viewRequest(request)
                else:
                    return HttpResponse("Equipment not available")
               
                

    else:
        # lstEqpmnt = Equipments.objects.all().order_by('eqpName')
        form = EqpmntRequestForm()
        print(form.lstEqpmnt)
        # form.EqpName = choices = [(x.eqpId, x.eqpName) for x in lstEqpmnt]
        return render(request, 'EndUser/eqpRequest.html', {'form' : form});
    # return home(request);

#method to view request status for equipments by students
@login_required
def viewRequest(request):
    user = request.user
    print(user)
    lstRequest = list(EquipmentRequest.objects.filter(user=user).order_by('-dtOfRequest'))
    print(lstRequest)
    print("No of requests: ", len(lstRequest))
    return render(request, 'EndUser/viewRequest.html', {'lstRequest': lstRequest});


#method to view all pending requests to be processed by the sports room admin
@login_required
def pendingRequest(request):
    lstPendingRequest = list(EquipmentRequest.objects.filter(reqStatus = 0).order_by('-dtOfRequest'))
    print("No of pending requests: ",len(lstPendingRequest))
    return render(request, 'AdminUser/pendingRequest.html', {'lstPendingRequest' : lstPendingRequest});

#method to view all processed requests to be by the sports room admin
@login_required
def approvedRequest(request):
    lstProcessedRequest = list(EquipmentRequest.objects.filter(reqStatus__in = [1,2,3]).order_by('-dtOfRequest'))
    print("No of processed requests: ", len(lstProcessedRequest))
    return render(request, 'AdminUser/processedRequest.html', {'lstProcessedRequest': lstProcessedRequest});

#method to process a pending requests by the sports room admin
@login_required
def processRequest(request):
    isAcceptRequest = request.GET.get('isAcceptRequest')
    print(isAcceptRequest)
    reqId = request.GET.get('reqId')
    print(reqId)
    pendingRequest = EquipmentRequest.objects.get(reqId=reqId)
    print(pendingRequest)
    currentTime = datetime.today()
    if(int(isAcceptRequest) == 1):
        pendingRequest.reqStatus    = 1
        pendingRequest.dtAvailed    = currentTime
        pendingRequest.dtOfExpRet   = currentTime + timedelta(days=1)
    else:
        pendingRequest.reqStatus    = 2
        pendingRequest.dtAvailed    = currentTime
        pendingRequest.dtOfExpRet   = currentTime
        pendingRequest.dtOfActualRet= currentTime

    insertOrUpdate(pendingRequest)
    return home(request)

#method to process return request by the sports room admin
@login_required
def processReturnRequest(request):
    reqId = request.GET.get('reqId')
    print(reqId)
    returnRequest = EquipmentRequest.objects.get(reqId=reqId)
    print(returnRequest)
    currentTime = datetime.today()
    dailyPenalty = settings.DAILY_PENALTY
    delta = currentTime.date() - returnRequest.dtOfExpRet.date()
    print(delta.days)
    penaltyAmount = 0
    if (delta.days > 0):
        penaltyAmount = dailyPenalty * delta.days


    returnRequest.reqStatus    = 3
    returnRequest.dtOfActualRet= currentTime
    returnRequest.penalty      = penaltyAmount
    insertOrUpdate(returnRequest)
    insertOrUpdate(UserProfileInfo)
    return approvedRequest(request)