from django.db import models


class BuyerItems(models.Model):
	JcFName = models.CharField(blank = True, max_length=100)
	JcLName = models.CharField(blank = True, max_length=100)
	JcPhone = models.CharField(blank = True, max_length=100)
	JcEmail = models.CharField(blank = True, max_length=100)
	JcAddress = models.CharField(blank = True, max_length=100)


class ProductItems(models.Model):
	JcShoes = models.CharField(blank = True, max_length=100)
	JcQuantity= models.CharField(blank = True, max_length=100)
	JcColor = models.CharField(blank = True, max_length=100)
	JcSize= models.CharField(blank = True, max_length=100)
	Jcpayment = models.CharField(blank = True, max_length=100)
	Jcdelivery = models.CharField(blank = True, max_length=100)


