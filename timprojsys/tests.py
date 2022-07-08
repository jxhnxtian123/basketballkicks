from django.test import TestCase
from timprojsys.views import MainPage
from .models import BuyerItems
'''
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
'''

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')


	def test_save_POST_request(self):
		response = self.client.post('/', {'name' :'John Christian M. Basijan',
	 		'email': 'jcbasijan5@gmail.com',
	 		'phone': '09123456789',
	 		'topic': 'Some Questions',
	 		'msg': 'BASKETBALL'})
		self.assertEqual(BuyerItems.objects.count(),1)
		inputData = BuyerItems.objects.first()
		self.assertEqual(inputData.JcName, 'John Christian M. Basijan')
		self.assertEqual(inputData.JcEmail, 'jcbasijan5@gmail.com')
		self.assertEqual(inputData.JcPhone, '09123456789')
		self.assertEqual(inputData.JcTopic, 'Some Questions')
		self.assertEqual(inputData.JcMsg, 'BASKETBALL')

	def test_only_saves_items_uf_necessary(self):
		self.client.get('/')
		self.assertEqual(BuyerItems.objects.count(), 0)

	def test_POST_redirect(self):
		response = self.client.post('/', {'name' :'John Christian M. Basijan',
	 		'email': 'jcbasijan5@gmail.com',
	 		'phone': '09123456789',
	 		'topic': 'Some Questions',
	 		'msg': 'BASKETBALL'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	class ORMTEST(TestCase):
		def test_saving_retrive(self):
			BuyerItems_list = BuyerItems()
			BuyerItems_list.JcName = 'John Christian M. Basijan'
			BuyerItems_list.JcEmail = 'jcbasijan5@gmail.com'
			BuyerItems_list.JcPhone = '09123456789'
			BuyerItems_list.JcTopic = 'Some Questions'
			BuyerItems_list.JcMsg = 'BASKETBALL'
			BuyerItems_list.save()

			BuyerItems_list = BuyerItems()
			BuyerItems_list.JcName = 'John Basijan'
			BuyerItems_list.JcEmail = 'jcbasijan531@gmail.com'
			BuyerItems_list.JcPhone = '09123456789'
			BuyerItems_list.JcTopic = 'Any Questions'
			BuyerItems_list.JcMsg = 'BASKETBALL ITEMS'
			BuyerItems_list.save()

			BuyerItems_Data = BuyerItems.objects.all()
			self.assertEqual(BuyerItems_Data.count(), 2)

			Buyerdata1 = BuyerItems_Data[0]
			Buyerdata2 = BuyerItems_Data[1]

			self.assertEqual(Buyerdata1.JcName, 'John Christian M. Basijan')
			self.assertEqual(Buyerdata1.JcEmail, 'jcbasijan5@gmail.com')
			self.assertEqual(Buyerdata1.JcPhone, '09123456789')
			self.assertEqual(Buyerdata1.JcTopic, 'Some Questions')
			self.assertEqual(Buyerdata1.JcMsg, 'BASKETBALL')

			self.assertEqual(Buyerdata2.JcName, 'John Basijan')
			self.assertEqual(Buyerdata2.JcEmail, 'jcbasijan531@gmail.com')
			self.assertEqual(Buyerdata2.JcPhone, '09123456789')
			self.assertEqual(Buyerdata2.JcTopic, 'Any Questions')
			self.assertEqual(Buyerdata2.JcMsg, 'BASKETBALL ITEMS')


	def test_template_display_list(self):
		BuyerItems.objects.create(JcName = 'John Christian M. Basijan',
			JcEmail = 'jcbasijan5@gmail.com',
			JcPhone = '09123456789',
			JcTopic = 'Some Questions',
			JcMsg = 'BASKETBALL')

		BuyerItems.objects.create(JcName = 'John Basijan',
			JcEmail = 'jcbasijan531@gmail.com',
			JcPhone = '09123456789',
			JcTopic = 'Any Questions',
			JcMsg = 'BASKETBALL ITEMS')

		response = self.client.get('/')
		self.assertIn('John Christian M. Basijan, jcbasijan5@gmail.com, 09123456789, Some Questions, BASKETBALL', response.content.decode())
		self.assertIn('John Basijan, jcbasijan531@gmail.com, 09123456789, Any Questions, BASKETBALL', response.content.decode())



