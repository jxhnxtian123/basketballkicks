from django.db.models import fields
from django.forms import ModelForm
from .models import *

class Buyerform(ModelForm):
    class Meta:
        model= BuyerItems
        fields = ['JcFName', 'JcLName', 'JcPhone', 'JcEmail', 'JcAddress',]
class Productform(ModelForm):
    class Meta:
        model= ProductItems
        fields = ['JcShoes', 'JcQuantity', 'JcColor', 'JcSize', 'Jcpayment', 'Jcdelivery',]

