import match
import unittest

string_a_0 = '{}[][[]]()((()))'
string_a_1 = '(((([{}]))))'
string_a_2 = '()()()(){}[]{}'

string_r_0 = ')()()'
string_r_1 = '{}()}{'
string_r_2 = '[][[]]]'


class TestStack(unittest.TestCase):
	
	def test_accepted0(self):
		self.assertTrue(match.match(string_a_0))
	
	def test_accepted1(self):
		self.assertTrue(match.match(string_a_1))

	def test_accepted2(self):
		self.assertTrue(match.match(string_a_2))

	def test_rejected0(self):
		self.assertFalse(match.match(string_r_0))

	def test_rejected1(self):
		self.assertFalse(match.match(string_r_1))

	def test_rejected2(self):
		self.assertFalse(match.match(string_r_2))


if __name__ == '__main__':
    unittest.main()
