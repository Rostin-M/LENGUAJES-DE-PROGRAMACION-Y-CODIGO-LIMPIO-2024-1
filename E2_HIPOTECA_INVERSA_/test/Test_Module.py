import unittest
from src.logic import Calculations as CM
from src.logic import Exceptions as E

class Test_ReverseMortgage(unittest.TestCase):

    """
        Normal cases with all the right parameters (6)
    """

    def test_case_normal_1(self):
        total_amount = 200000000
        interest = 0.007974
        age = 66
        quotas = 204
        interest_housing = 0.3
        result = round(CM.MortgageSingleReverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 294117.65
        self.assertEqual(result, expected)

    def test_case_normal_2(self):
        total_amount = 150000000
        interest = 0.007974
        age = 69
        quotas = 156
        interest_housing = 0.35
        result = round(CM.MortgageLifetimeInverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 336538.46
        self.assertEqual(result, expected)

    def test_case_normal_3(self):
        total_amount = 234000000
        interest = 0.007974
        age = 71
        quotas = 156
        interest_housing = 0.45
        result = round(CM.MortgageLifetimeInverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 675000
        self.assertEqual(result, expected)

    def test_case_normal_4(self):
        total_amount = 65000000
        interest = 0.007974
        age = 69
        quotas = 228
        interest_housing = 0.40
        result = round(CM.MortgageLifetimeInverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 114035.09
        self.assertEqual(result, expected)

    def test_case_normal_5(self):
        total_amount = 115000000
        interest = 0.007974
        age = 72
        quotas = 72
        interest_housing = 0.1
        result = round(CM.MortgageLifetimeInverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 159722.22
        self.assertEqual(result, expected)

    def test_case_normal_6(self):
        total_amount = 534000000
        interest = 0.007974
        age = 71
        quotas = 228
        interest_housing = 0.48
        result = round(CM.MortgageLifetimeInverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 1124210.53
        self.assertEqual(result, expected)

    # 6 casos extraordinarios

    def test_case_extraordinary_1(self):

        """
        1 year life expectancy
        """

        total_amount = 89000000
        interest = 0.007974
        age = 81
        quotas = 12
        interest_housing = 0.10
        result = round(CM.MortgageTemporaryReverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 741666.67
        self.assertEqual(result, expected)

    def test_case_extraordinary_2(self):

        """
        Very low housing price
        """

        total_amount = 53000000
        interest = 0.007974
        age = 72
        quotas = 120
        interest_housing = 0.40
        result = round(CM.MortgageTemporaryReverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 176666.67
        self.assertEqual(result, expected)

    def test_case_extraordinary_3(self):

        """
        Very high housing price
        """

        total_amount = 1000000000
        interest = 0.007974
        age = 65
        quotas = 180
        interest_housing = 0.20
        result = round(CM.MortgageTemporaryReverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 1111111.11
        self.assertEqual(result, expected)

    def test_case_extraordinary_4(self): 
        
        """
        Interest Low
        """

        total_amount = 230000000
        interest = 0.001
        age = 68
        quotas = 264
        interest_housing = 0.9
        result = round(CM.MortgageTemporaryReverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 784090.91
        self.assertEqual(result, expected)

    def test_case_extraordinary_5(self):
               
        """
        Interest hight
        """

        total_amount = 1200000000
        interest = 0.007974
        age = 65
        quotas = 300
        interest_housing = 0.85
        result = round(CM.MortgageTemporaryReverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 3400000
        self.assertEqual(result, expected)

    def test_case_extraordinary_6(self):
                
        """
        Life expectancy almost reached
        """

        total_amount = 54000000
        interest = 0.007974
        age = 81
        quotas = 12
        interest_housing = 0.10
        result = round(CM.MortgageTemporaryReverse(total_amount, interest, quotas, interest_housing), 2)
        expected = 450000
        self.assertEqual(result, expected)

    # 8 casos de error
        
    def test_quota_negative(self):
        with self.assertRaises(E.invalid_valor):
            total_amount = 48900000
            interest = 0.0023
            quotas = -43
            interest_housing = 0.10
            result = round(CM.MortgageSingleReverse(total_amount, interest, quotas, interest_housing), 2) 

    def test_invalid_age(self):
        with self.assertRaises(E.invalid_age):
            age = 64
            gender = "M"
            interest_housing = 0.10
            result = CM.LifeExpectancyCalculation(age, gender)

    def test_hight_interest(self):
        with self.assertRaises(E.hight_interest):
            total_amount = 54000000
            expectancy_calculation = 12
            interest = 0.0080
            quotas = 34
            interest_housing = 0.10
            result = round(CM.MortgageSingleReverse(total_amount, interest, quotas, interest_housing), 2)

    def test_interest_negative(self):
        with self.assertRaises(E.invalid_valor):
            total_amount = 26700000
            interest = -0.0034
            quotas = 0
            interest_housing = 0.10
            result = round(CM.MortgageSingleReverse(total_amount, interest, quotas, interest_housing), 2) 

    def test_cero_interest(self):
        with self.assertRaises(E.invalid_interest):
            total_amount = 53000000
            expectancy_calculation = 12
            interest = 0
            age = 67
            quotas = 19
            interest_housing = 0.10
            result = round(CM.MortgageSingleReverse(total_amount, interest, quotas, interest_housing), 2)

    def test_low_amount_property(self):
        with self.assertRaises(E.low_amount_property):
            total_amount = 51000000
            expectancy_calculation = 12
            interest = 0.007974
            quotas = 34
            interest_housing = 0.10
            result = round(CM.MortgageSingleReverse(total_amount, interest, quotas, interest_housing), 2)

    def test_cero_quotas(self):
        with self.assertRaises(E.invalid_quotas):
            total_amount = 53000000
            interest = 0.007974
            quotas = 0
            interest_housing = 0.10
            result = round(CM.MortgageSingleReverse(total_amount, interest, quotas, interest_housing), 2)

    def test_amount_negative(self):
        with self.assertRaises(E.invalid_valor):
            total_amount = -53000000
            interest = 0.007974
            quotas = 0
            interest_housing = 0.10
            result = round(CM.MortgageSingleReverse(total_amount, interest, quotas, interest_housing), 2)   

if __name__ == '__main__':
    unittest.main()