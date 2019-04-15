from django import forms
from .models import *
class EqpmntRequestForm(forms.Form):
    lstEqpmnt = Equipments.objects.all().order_by('eqpName')
    # print(lstEqpmnt)
    EqpName = forms.ChoiceField(choices = [(x.eqpId, x.eqpName) for x in lstEqpmnt])
    EqpQuantity = forms.IntegerField(min_value=1, max_value=2)
    # class Meta:
    #     model = Equipments
    #     fields = {'eqpName','eqpQuantity'}
