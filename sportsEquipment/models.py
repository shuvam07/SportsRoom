from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from login.models import UserProfileInfo
# Create your models here.
class Equipments(models.Model):
    eqpId       = models.AutoField(primary_key=True)
    eqpName     = models.CharField(max_length=50)
    eqpQuantity = models.IntegerField(validators=[MinValueValidator(1)])
    eqpQuantityTaken = models.IntegerField(default=0,validators=[MaxValueValidator(eqpQuantity)])

    def __str__(self):
        return str(self.eqpId)+"@"+self.eqpName+"_"+str(self.eqpQuantity)


class EquipmentRequest(models.Model):
    reqId           =   models.AutoField(primary_key=True)
    eqp             =   models.ForeignKey(Equipments,on_delete=models.CASCADE)
    quantity        =   models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    user            =   models.ForeignKey(User,on_delete=models.CASCADE)
    dtOfRequest     =   models.DateTimeField()
    dtAvailed       =   models.DateTimeField(null=True)
    dtOfExpRet      =   models.DateTimeField(null=True)
    dtOfActualRet   =   models.DateTimeField(null=True)
    penalty         =   models.IntegerField(default=0)
    choices = (
        (0, 'PENDING'),
        (1, 'ACCEPTED'),
        (2, 'REJECTED'),
        (3, 'RETURNED')
    )
    reqStatus       =   models.IntegerField(default=0,choices=choices)
    # remarks         =   models.CharField(null=True, default='')