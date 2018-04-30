'''
Created on Apr 30, 2018

@author: eanuama
'''
import unittest
from src.order_validation_engine import OrderValidationEngine
from src.order_wrapper import OrderWrapper
from src.order_repo import OrderRepo

class TestOrderValidationEngine(unittest.TestCase):

    def setUp(self):
        order_repository = OrderRepo()
        order1 = OrderWrapper({"orderId": 100, "status": "NEW", "updateId": 287, "amount": 20})
        order2 = OrderWrapper({"orderId": 101, "status": "NEW", "updateId": 289, "amount": 13})
        order_repository.order_map[order1.orderId] = order1        
        order_repository.order_map[order2.orderId] = order2
        
        #Dummy object
        order = OrderWrapper({})        
        self.order_validator = OrderValidationEngine(order_repository, order)
        
    #Checks for valid state transition
    def test_is_valid_transition(self):        
        self.order_validator.current_status = "NEW"
        self.order_validator.status = "COOKING"
        self.assertTrue(self.order_validator.is_valid_transition())

        self.order_validator.current_status = "NEW"
        self.order_validator.status = "CANCELED"
        self.assertTrue(self.order_validator.is_valid_transition())
        
        self.order_validator.current_status = "NEW"
        self.order_validator.status = "DELIVERING"
        self.assertFalse(self.order_validator.is_valid_transition())

        self.order_validator.current_status = "NEW"
        self.order_validator.status = "REFUNDED"
        self.assertFalse(self.order_validator.is_valid_transition())

        self.order_validator.current_status = "COOKING"
        self.order_validator.status = "DELIVERING"
        self.assertTrue(self.order_validator.is_valid_transition())

        self.order_validator.current_status = "COOKING"
        self.order_validator.status = "CANCELED"
        self.assertTrue(self.order_validator.is_valid_transition())

        self.order_validator.current_status = "COOKING"
        self.order_validator.status = "DELIVERED"
        self.assertFalse(self.order_validator.is_valid_transition())
        
        self.order_validator.current_status = "DELIVERING"
        self.order_validator.status = "DELIVERED"
        self.assertTrue(self.order_validator.is_valid_transition())

        self.order_validator.current_status = "DELIVERING"
        self.order_validator.status = "CANCELED"
        self.assertTrue(self.order_validator.is_valid_transition())
        
        self.order_validator.current_status = "DELIVERING"
        self.order_validator.status = "REFUNDED"
        self.assertFalse(self.order_validator.is_valid_transition())
        
        self.order_validator.current_status = "DELIVERED"
        self.order_validator.status = "REFUNDED"
        self.assertTrue(self.order_validator.is_valid_transition())

        self.order_validator.current_status = "DELIVERED"
        self.order_validator.status = "CANCELED"
        self.assertFalse(self.order_validator.is_valid_transition())
        
    
    #Checks if updateId in increasing order
    def test_is_update_in_order(self):
        self.order_validator.update_id = 288
        self.order_validator.current_update_id = 287
        self.assertTrue(self.order_validator.is_update_in_order())
                
        self.order_validator.update_id = 287
        self.assertFalse(self.order_validator.is_update_in_order())

    
    #Checks if update is unique
    def test_is_unique_update(self):
        order = self.order_validator.order
        order.orderId = 100
        order.updateId = 288
        order.status = "COOKING"

        self.order_validator.order_id = order.orderId
        self.order_validator.update_id = order.updateId
        self.order_validator.status = order.status        

        self.assertTrue(self.order_validator.is_unique_update())
        
        order.orderId = 100
        order.updateId = 287
        order.status = "NEW"

        self.order_validator.order_id = order.orderId
        self.order_validator.update_id = order.updateId
        self.order_validator.status = order.status        
        
        self.assertFalse(self.order_validator.is_unique_update())        
        
    
    #Checks for mandatory fields 
    def test_is_valid_update(self):
        order = self.order_validator.order
        order.orderId = 100
        order.updateId = 287
        order.status = "NEW"
        self.assertTrue(self.order_validator.is_valid_update())
    


if __name__ == "__main__":
    unittest.main()