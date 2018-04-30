'''
Created on Apr 30, 2018

@author: eanuama
'''
import unittest
import io
import sys

from src.order_repo import OrderRepo
from src.order_wrapper import OrderWrapper

class TestOrderRepo(unittest.TestCase):

    def setUp(self):
        self.order_repository = OrderRepo()
        order1 = OrderWrapper({"orderId": 100, "status": "DELIVERING", "updateId": 294})
        order2 = OrderWrapper({"orderId": 101, "status": "CANCELED", "updateId": 290})
        order3 = OrderWrapper({"orderId": 102, "status": "NEW", "updateId": 291, "amount": 17})
        order1.amount = 20
        order2.amount = 13
        self.order_repository.order_map[order1.orderId] = order1        
        self.order_repository.order_map[order2.orderId] = order2
        self.order_repository.order_map[order3.orderId] = order3


    def test_get_order(self):
        order  = OrderWrapper({"orderId": 100, "status": "DELIVERING", "updateId": 294})
        result = self.order_repository.get_order(order)                
        self.assertEqual(result.orderId, 100)
        self.assertEqual(result.updateId, 294)
        
        order  = OrderWrapper({"orderId": 104, "status": "NEW", "updateId": 299, "amount": 20})
        self.assertRaises(KeyError, lambda: self.order_repository.get_order(order))
        
        
    def test_is_order_exists(self):
        order  = OrderWrapper({"orderId": 100, "status": "DELIVERING", "updateId": 294})
        result = self.order_repository.is_order_exists(order)                
        self.assertEqual(result, True)
        
        order  = OrderWrapper({"orderId": 104, "status": "NEW", "updateId": 299, "amount": 20})
        result = self.order_repository.is_order_exists(order)        
        self.assertEqual(result, False)
        
    
    def test_show_summary(self):
        # Create StringIO object
        captured_output = io.StringIO()
        # Redirect stdout.
        sys.stdout = captured_output
        self.order_repository.show_summary()
        # Reset redirect.
        sys.stdout = sys.__stdout__                     
        results = captured_output.getvalue()
        result = results.split("\n")
        #expected print summary        
        expected = ["New: 1", 
                    "Cooking: 0",
                    "Delivering: 1",
                    "Delivered: 0",
                    "Canceled: 1",
                    "Refunded: 0",
                    "Total amount charged: $20"]
        
        for i in range(len(result)-1):
            self.assertEqual(result[i], expected[i])
            

if __name__ == "__main__":
    unittest.main()