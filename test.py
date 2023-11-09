import unittest
from unittest.mock import patch, MagicMock
from app import app, convert

class CurrencyConverterTest(unittest.TestCase):
    def setUp(self):
        self.mock_currency_rates = patch("app.CurrencyRates").start()
        self.mock_currency_convert = self.mock_currency_rates.return_value.convert

    def tearDown(self):
        patch.stopall()
    
    def test_calls_convert_currency_correctly(self):
        m = MagicMock()
        m.form = {
            'c1': 'USD',
            'c2': 'EUR',
            'amt': 200
        }
        with app.app_context():
            with patch("app.request", m):
                convert()
                self.mock_currency_convert.assert_called_with("USD", "EUR", 200.0)

            



if __name__ == '__main__':
    unittest.main()

