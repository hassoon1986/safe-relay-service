from django.test import TestCase

from .factories import TokenFactory


class TestModels(TestCase):
    def test_token_eth_value(self):
        fixed_eth_conversion = 0.1
        token = TokenFactory(fixed_eth_conversion=fixed_eth_conversion)
        self.assertEqual(token.get_eth_value(), fixed_eth_conversion)

        token = TokenFactory(decimals=17, fixed_eth_conversion=fixed_eth_conversion)
        self.assertEqual(token.get_eth_value(), fixed_eth_conversion * 10)

        token = TokenFactory(decimals=19, fixed_eth_conversion=fixed_eth_conversion)
        self.assertEqual(token.get_eth_value(),fixed_eth_conversion / 10)