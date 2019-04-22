from django import forms
from .models import *
from login.models import UserProfileInfo
class EqpmntRequestForm(forms.Form):
    lstEqpmnt = Equipments.objects.all().order_by('eqpName')
    #print(lstEqpmnt)
    EqpName = forms.ChoiceField(choices = [(x.eqpId, x.eqpName) for x in lstEqpmnt])
    EqpQuantity = forms.IntegerField(min_value=1, max_value=2)
    # class Meta:
    #     model = Equipments
    #     fields = {'eqpName','eqpQuantity'}


class addEqpForm(forms.ModelForm):
	class Meta:
		model = Equipments
		fields = [
				'eqpName'   ,
				'eqpQuantity'
		]
    #EqpName = forms.CharField(label='eqp name', max_length=100)
    #EqpQuantity = forms.IntegerField(min_value=1)



class editForm(forms.ModelForm):
	class Meta:
		model = Equipments
		fields = [
			'eqpName',
			'eqpQuantity'
		]

