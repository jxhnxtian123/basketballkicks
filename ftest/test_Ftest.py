from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	
	def test_start_list_and_retrieve(self):
		self.browser.get(self.live_server_url)
		self.assertIn('BASKETBALL ITEMS', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('BASKETBALL ITEMS', headerText)

#Type

		PersonName = self.browser.find_element_by_id('BuyerName')
		self.assertEqual(PersonName.get_attribute('placeholder'),'Name')
		PersonName.send_keys('John Christian M. Basijan')
		time.sleep(1)

		PersonEmail = self.browser.find_element_by_id('BuyerEmail')
		self.assertEqual(PersonEmail.get_attribute('placeholder'),'E-mail Address')
		PersonEmail.send_keys('jcbasijan5@gmail.com')
		time.sleep(0.3)

		PersonPhone = self.browser.find_element_by_id('BuyerPhone')
		self.assertEqual(PersonPhone.get_attribute('placeholder'),'Phone')
		PersonPhone.send_keys('09123456789')
		time.sleep(0.3)

		PersonTopic = self.browser.find_element_by_id('BuyerTopic')
		self.assertEqual(PersonTopic.get_attribute('placeholder'),'Select Your Topic:')
		selectPersonTopic = Select(PersonTopic)
		selectPersonTopic.select_by_visible_text('Some Questions')
		time.sleep(0.3)

		PersonalMsg = self.browser.find_element_by_id('BuyerMessage')
		self.assertEqual(PersonalMsg.get_attribute('placeholder'),'message')
		PersonalMsg.send_keys('BASKETBALL')
		time.sleep(0.3)

      		
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(0.3)
#Table
		
		# inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_tag_name('table')
		outline = table.find_element_by_tag_name('tr')
		self.assertIn('John Christian M. Basijan, jcbasijan5@gmail.com, 09123456789, Some Questions, BASKETBALL', outline.text)

	def test_start_list_and_retrieve_2(self):
		self.browser.get(self.live_server_url)
		self.assertIn('BASKETBALL ITEMS', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('BASKETBALL ITEMS', headerText)

#Type

		PersonName = self.browser.find_element_by_id('BuyerName')
		self.assertEqual(PersonName.get_attribute('placeholder'),'Name')
		PersonName.send_keys('John Christian M. Basijan')
		time.sleep(1)

		PersonEmail = self.browser.find_element_by_id('BuyerEmail')
		self.assertEqual(PersonEmail.get_attribute('placeholder'),'E-mail Address')
		PersonEmail.send_keys('jcbasijan5@gmail.com')
		time.sleep(0.3)

		PersonPhone = self.browser.find_element_by_id('BuyerPhone')
		self.assertEqual(PersonPhone.get_attribute('placeholder'),'Phone')
		PersonPhone.send_keys('09123456789')
		time.sleep(0.3)

		PersonTopic = self.browser.find_element_by_id('BuyerTopic')
		self.assertEqual(PersonTopic.get_attribute('placeholder'),'Select Your Topic:')
		selectPersonTopic = Select(PersonTopic)
		selectPersonTopic.select_by_visible_text('Some Questions')
		time.sleep(0.3)

		PersonalMsg = self.browser.find_element_by_id('BuyerMessage')
		self.assertEqual(PersonalMsg.get_attribute('placeholder'),'message')
		PersonalMsg.send_keys('GOOD ITEMS')
		time.sleep(0.3)

      		
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(0.3)
		
		self.browser.get(self.live_server_url)
		self.assertIn('BASKETBALL ITEMS', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('BASKETBALL ITEMS', headerText)

#Type

		PersonName = self.browser.find_element_by_id('BuyerName')
		self.assertEqual(PersonName.get_attribute('placeholder'),'Name')
		PersonName.send_keys('Jayce')
		time.sleep(1)

		PersonEmail = self.browser.find_element_by_id('BuyerEmail')
		self.assertEqual(PersonEmail.get_attribute('placeholder'),'E-mail Address')
		PersonEmail.send_keys('john5@gmail.com')
		time.sleep(0.3)

		PersonPhone = self.browser.find_element_by_id('BuyerPhone')
		self.assertEqual(PersonPhone.get_attribute('placeholder'),'Phone')
		PersonPhone.send_keys('09123456789')
		time.sleep(0.3)

		PersonTopic = self.browser.find_element_by_id('BuyerTopic')
		self.assertEqual(PersonTopic.get_attribute('placeholder'),'Select Your Topic:')
		selectPersonTopic = Select(PersonTopic)
		selectPersonTopic.select_by_visible_text('About Features')
		time.sleep(0.3)

		PersonalMsg = self.browser.find_element_by_id('BuyerMessage')
		self.assertEqual(PersonalMsg.get_attribute('placeholder'),'message')
		PersonalMsg.send_keys('THANKYOU')
		time.sleep(0.3)

      		
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(0.3)

		# inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_tag_name('table')
		outline = table.find_elements_by_tag_name('tr')
		self.assertIn('Entry 1: John Christian M. Basijan, jcbasijan5@gmail.com, 09123456789, Some Questions, GOOD ITEMS', [row.text for row in outline])
		self.assertIn('Entry 2: Jayce, john5@gmail.com, 09123456789, About Features, THANKYOU', [row.text for row in outline])

# if __name__ == '__main__' :
# 	unittest.main(warnings='ignore')


