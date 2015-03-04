import unittest
from fizzbuzz import fizzbuzz
from fizzbuzz import fizzbuzz_list

class FizzBuzzTestCase(unittest.TestCase):
	def test_fizzbuzz_recebe_um_e_retorna_um(self):
		self.assertEqual(fizzbuzz(1), 1)

	def test_fizzbuzz_recebe_dois_e_retorna_dois(self):
		self.assertEqual(fizzbuzz(2), 2)

	def test_fizzbuzz_recebe_tres_retorna_fizz(self):
		self.assertEqual(fizzbuzz(3), "fizz")

	def test_fizzbuzz_recebe_quatro_e_retorna_quatro(self):
		self.assertEqual(fizzbuzz(4), 4)

	def test_fizzbuzz_recebe_cinco_e_retorna_buzz(self):
		self.assertEqual(fizzbuzz(5), "buzz")

	def test_fizzbuzz_recebe_seis_e_retorna_fizz(self):
		self.assertEqual(fizzbuzz(6), "fizz")

	def test_fizzbuzz_recebe_nove_e_retorna_fizz(self):
		self.assertEqual(fizzbuzz(9), "fizz")		

	def test_fizzbuzz_recebe_doze_e_retorna_fizz(self):
		self.assertEqual(fizzbuzz(12), "fizz")

	def test_fizzbuzz_recebe_dez_e_retorna_buzz(self):
		self.assertEqual(fizzbuzz(10), "buzz")	

	def test_fizzbuzz_recebe_quinze_retorna_fizzbuzz(self):
		self.assertEqual(fizzbuzz(15), "fizzbuzz")

	def test_fizzbuzz_list_de_um_a_cinco(self):
		self.assertEqual(fizzbuzz_list([1,2,3,4,5]), [1, 2, "fizz", 4, "buzz"])

	def test_fizzbuzz_list_de_cinco_em_cinco(self):
		self.assertEqual(fizzbuzz_list([5, 10, 15, 20, 25, 30]), ["buzz", "buzz", "fizzbuzz", "buzz", "buzz", "fizzbuzz"])