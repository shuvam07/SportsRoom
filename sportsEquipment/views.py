from django.shortcuts import render, redirect
from login.forms import UserForm,UserProfileInfoForm
from login.models import UserProfileInfo
from datetime import *
from django.db import transaction
from django.shortcuts import render, get_object_or_404

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *
from .forms import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.core.urlresolvers import reverse_lazy

# Create your views here.

#method to render home page ater login
@login_required
def home(request):
    userProfile = UserProfileInfo.objects.get(user=request.user)
    if request.user.is_superuser:
        totalPenalty = 0
    else:
        totalPenalty = userProfile.totalPenalty
    return render(request,'home.html',{'userProfile': userProfile})

#method to perform an insert or update

def insertOrUpdate(model):
    model.save()
    # try:
    #     with transaction.atomic():
    #         model.save()
    # except IntegrityError:
    #     handle_exception()

#method to make requests for equipments by students

#method to make requests for equipments by students

@login_required
def checkAvailability(request):
    print(request.POST)
    reqId = request.POST['reqId']
    print(reqId)
    penReq = EquipmentRequest.objects.get(reqId=reqId)
    availability = penReq.eqp.eqpQuantity- penReq.eqp.eqpQuantityTaken
    print('availability',availability)
    # data = {
    #     'availability' : availability,
    #     'id' : reqId
    # }
    return HttpResponse(availability)
    # equipments = Equipments.objects.get(eqpName=penReq.eqp)
    # print(equipments)

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
                user = request.user
                equipmentRequest = EquipmentRequest()
                currentDateTime = datetime.today()
                requestedQuantity = request.POST['EqpQuantity']
                
                
                equipmentRequest.quantity       = requestedQuantity
                equipmentRequest.eqp            = Equipments.objects.get(pk=int(request.POST['EqpName'],10))
                equipmentRequest.user           = user
                equipmentRequest.dtOfRequest    = currentDateTime
                equipmentRequest.dtAvailed      = datetime.today()
                equipmentRequest.dtOfExpRet     = currentDateTime + timedelta(days=7)
                insertOrUpdate(equipmentRequest)
                return redirect(reverse('sportsEquipment:viewRequest'))
            else:
                return HttpResponse("Equipment not available")
               
                

    else:
        # lstEqpmnt = Equipments.objects.all().order_by('eqpName')
        form = EqpmntRequestForm()
        print(form.lstEqpmnt)
        # form.EqpName = choices = [(x.eqpId, x.eqpName) for x in lstEqpmnt]
        return render(request, 'EndUser/eqpRequest.html', {'form' : form});
    # return home(request);

#method to add equiment by admin
@login_required
def addEquip(request):
    if(request.method=="POST"):
        form = addEqpForm(request.POST)
        if form.is_valid():
            form.save()
        return viewInventory(request)
    else:
        form = addEqpForm()
        context ={
            'form' : form
        }
        return render(request, "AdminUser/addEquip.html",context)



#method to check penalty of users
@login_required
def penalty(request):
    context = list(UserProfileInfo.objects.order_by('totalPenalty'))
    print(context)
    #print("No of requests: ", len(context))
    return render(request, 'AdminUser/viewPenalty.html', {'context': context});
    #return render(request, "AdminUser/viewPenalty.html")
    # print("Check penalty is working!!")
    # return viewInventory(request)
    # if(request.method=="POST"):
    #     form = penaltyForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         #viewPenalty(request)
    #         userProfile = UserProfileInfo.objects.get(user=request.user)
    #         totalPenalty = userProfile.totalPenalty
    #         print(totalPenalty)
    #         print("form is valid!!")
    #         return render(request, "AdminUser/viewPenalty.html")
    #     else:
    #         print("form invalid!")
    #         return render(request, "AdminUser/viewPenalty.html")
    # else:
    #     form = penaltyForm()
    #     context ={
    #         'form' : form
    #     }
    #     #SSviewPenalty(request)
    #     print("Method is not post!!!")
    #     return render(request, "AdminUser/checkPenalty.html",context)


#method to edit equipment list by Admin
@login_required
def editEquipList(request,pk):
    
    item = get_object_or_404(Equipments,eqpId = pk)

    if request.method == "POST":
        form = editForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # return render(request,'AdminUser/editEquipList.html',{'form':form})
            return viewInventory(request)

    else:
        form = editForm(instance = item)
        return render(request,'AdminUser/editEquipList.html',{'form':form})




#method to delete a equip
#@login_required
def deleteEqp(request,pk):
    Equipments.objects.filter(eqpId=pk).delete()
    items = Equipments.objects.all()
    print (items)
    context = {
        'items' : items
    }
    return render(request,'AdminUser/deleteEquip.html',context)
    #return redirect('AdminUser/viewEquipList.html')


#method to view request status for equipments by students
@login_required
def viewRequest(request):
    user = request.user
    print(user)
    lstRequest = list(EquipmentRequest.objects.filter(user=user).order_by('-dtOfRequest'))
    print(lstRequest)
    print("No of requests: ", len(lstRequest))
    return render(request, 'EndUser/viewRequest.html', {'lstRequest': lstRequest});



#method to view inventory
@login_required
def viewInventory(request):
    #user = request.user
    #print(user)
    context = list(Equipments.objects.order_by('-eqpId'))
    for req in context:
        req.eqpQuantityTaken = req.eqpQuantity - req.eqpQuantityTaken
    print(context)
    #print("No of requests: ", len(context))
    return render(request, 'AdminUser/viewEquipList.html', {'context': context});


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
    penReq = EquipmentRequest.objects.get(reqId=reqId)
    print(penReq.eqp)
    currentTime = datetime.today()
    if(int(isAcceptRequest) == 1):
        eqp = penReq.eqp
        requestedQuantity = penReq.quantity
        print(requestedQuantity)
        print(eqp.eqpQuantity - eqp.eqpQuantityTaken)
        if(requestedQuantity <= (eqp.eqpQuantity - eqp.eqpQuantityTaken)) :    
            penReq.reqStatus    = 1
            penReq.dtAvailed    = currentTime
            penReq.dtOfExpRet   = currentTime + timedelta(days=1)
            eqp.eqpQuantityTaken += requestedQuantity
            insertOrUpdate(eqp)
        else :
            return HttpResponse("Equipment not available")
    else:
        penReq.reqStatus    = 2
        penReq.dtAvailed    = currentTime
        penReq.dtOfExpRet   = currentTime
        penReq.dtOfActualRet= currentTime

    insertOrUpdate(penReq)
    return pendingRequest(request)

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
    eqp = returnRequest.eqp
    eqp.eqpQuantityTaken -= returnRequest.quantity
    returnRequest.reqStatus    = 3
    returnRequest.dtOfActualRet= currentTime
    returnRequest.penalty      = penaltyAmount
    insertOrUpdate(returnRequest)
    insertOrUpdate(eqp)
    # insertOrUpdate(UserProfileInfo)
    return approvedRequest(request)