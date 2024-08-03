import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        self.assertTrue((getDataPoint(quotes[0])[-1] ==
                         (float(quotes[0]['top_bid']['price']) + float(quotes[0]['top_ask']['price'])) / 2) and (
                            (getDataPoint(quotes[1])[-1] == (float(quotes[1]['top_bid']['price']) + float(
                                quotes[1]['top_ask']['price'])) / 2)))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        self.assertTrue((getDataPoint(quotes[0])[-1] ==
                         (float(quotes[0]['top_bid']['price']) + float(quotes[0]['top_ask']['price'])) / 2) and (
                          (getDataPoint(quotes[1])[-1] == (float(quotes[1]['top_bid']['price']) + float(
                            quotes[1]['top_ask']['price'])) / 2)))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_price_b_is_zero(self):
        price_a = 120.48
        price_b = 0

        self.assertEquals(getRatio(price_a, price_b), None)

    def test_getRatio_calculate_ratio(self):
        price_a = 120.48
        price_b = 121.68

        self.assertEquals(getRatio(price_a, price_b), price_a / price_b)

if __name__ == '__main__':
    unittest.main()
