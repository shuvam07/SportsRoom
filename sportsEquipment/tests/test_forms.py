from django.test import SimpleTestCase
from sportsEquipment.forms import editForm,addEqpForm,EqpmntRequestForm



class TestForms(SimpleTestCase):

	def test_editForm_valid_data(self):
		form = editForm(data={
			'eqpName': 'Ball',
			'eqpQuantity': 10
			})

		self.assertTrue(form.is_valid())

	def test_editForm_no_data(self):
		form = editForm(data={})


		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors),2)


	def test_addEqpForm_valid_data(self):
		form = addEqpForm(data={
			'eqpName': 'Ball',
			'eqpQuantity': 10
			})

		self.assertTrue(form.is_valid())

	def test_addEqpForm_no_data(self):
		form = addEqpForm(data={})


		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors),2)


	# def test_EqpmntRequestForm_valid_data(self):
	# 	form = EqpmntRequestForm(data={
	# 		'eqpName': 'Ball',
	# 		'eqpQuantity': 10
	# 		})

	# 	self.assertTrue(form.is_valid())

	def test_EqpmntRequestForm_no_data(self):
		form = EqpmntRequestForm(data={})


		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors),2)
