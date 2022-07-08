from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import Buyerform, Productform
def index(request):
    return render(request, 'finalcust.html')

def products(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        number = request.POST['number']
        email = request.POST['email']
        Address = request.POST['Address']
        info = BuyerItems.objects.create(JcFName = fname, JcLName = lname, JcPhone = number, 
        JcEmail = email, JcAddress = Address,)
        info.save()
    return render(request, 'finalpro.html')


def records(request):
    if request.method == 'POST':
        shoes = request.POST['shoes']
        price = request.POST['price']
        color = request.POST['color']
        size = request.POST['size']
        payment = request.POST['payment']
        deliver = request.POST['deliver']
        product = ProductItems.objects.create(JcShoes = shoes, JcQuantity = price, JcColor = color, 
        JcSize = size, Jcpayment = payment, Jcdelivery = deliver)
        product.save()
    Item = ProductItems.objects.all() 
    Items = BuyerItems.objects.all()
    
    return render(request, 'table1.html',{'BuyerItems':Items, 'ProductItems':Item},)

def update(request, id):
	info = BuyerItems.objects.get(id=id)
	form = Buyerform(instance=info)
	if request.method == 'POST':
		form = Buyerform(request.POST, instance = info)
		if form.is_valid():
			form.save()
			return redirect('/records')

	return render(request, 'update.html', {'form':form})
		
def cancel(request, id):
    q = BuyerItems.objects.get(id=id)
    for x in BuyerItems.objects.only('id'):
        if q == x:
            x = BuyerItems.objects.get(id=id).delete()
            break
    return redirect('/records')

def update1(request, id):
	information = ProductItems.objects.get(id=id)
	form = Productform(instance=information)
	if request.method == 'POST':
		form = Productform(request.POST, instance = information)
		if form.is_valid():
			form.save()
			return redirect('/records')

	return render(request, 'update1.html', {'form':form})
		
def cancel1(request, id):
    idss = ProductItems.objects.get(id=id)
    for x in ProductItems.objects.only('id'):
        if idss == x:
            x = ProductItems.objects.get(id=id).delete()
            break
    return redirect('/records')