import unittest
from Solution import main
class Test_Sol(unittest.TestCase):
	def test_main1(self):
		Capacity=1150
		Hours=1
		print('Capacity:',Capacity,'Hours:',Hours)
		print('')
		List1=[
			{'region': 'New York', 'total_cost': '$10150','machines': {'8XLarge': 7, 'XLarge': 1, 'Large': 1}},
			{'region': 'India', 'total_cost': '$9520', 'machines': {'8XLarge': 7, 'Large': 3}},
			{'region': 'China', 'total_cost': '$8570', 'machines': {'8XLarge': 7, 'XLarge': 1, 'Large': 1}}]
        
		print('Expected Output:',List1)
		List2=main(Capacity,Hours)
		print('')
		print('Output Generated:',List2)
		print('')
		self.assertListEqual(List1,List2)

	def test_main2(self):
		Capacity=230
		Hours=5
		print('Capacity:',Capacity,'Hours:',Hours)
		print('')
		List1=[
			{'region': 'New York', 'total_cost': '$10150','machines': {'8XLarge': 7, 'XLarge': 1, 'Large': 1}},
			{'region': 'India', 'total_cost': '$9520', 'machines': {'8XLarge': 7, 'Large': 3}},
			{'region': 'China', 'total_cost': '$8570', 'machines': {'8XLarge': 7, 'XLarge': 1, 'Large': 1}}]
        
		print('Expected Output:',List1)
		List2=main(Capacity,Hours)
		print('')
		print('Output Generated:',List2)
		print('')
		self.assertListEqual(List1,List2)

	def test_main3(self):
		Capacity=100
		Hours=24
		print('Capacity:',Capacity,'Hours:',Hours)
		print('')
		List1=[
			{'region': 'New York', 'total_cost': '$21000', 'machines': {'8XLarge': 15}},
			{'region': 'India', 'total_cost': '$19500', 'machines': {'8XLarge': 15}},
			{'region': 'China', 'total_cost': '$17700', 'machines': {'8XLarge': 15}}]

		print('Expected Output:',List1)
		List2=main(Capacity,Hours)
		print('')
		print('Output Generated:',List2)
		self.assertListEqual(List1,List2)




