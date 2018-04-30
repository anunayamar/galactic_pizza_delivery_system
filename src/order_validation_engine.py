'''
Created on Apr 30, 2018

@author: eanuama
'''

class OrderValidationEngine(object):
    '''
    classdocs
    
    validates each order, according to the various rules
    '''
    def __init__(self, order_repository, order):
        self.order_repository = order_repository
        self.order = order
        
    '''
    Calls all different rules and returns the validate order object
    '''
    def validate_all(self):
        if self.is_valid_update():
            self.order_id = self.order.orderId
            self.update_id = self.order.updateId
            self.status = self.order.status
            if self.is_update_new():
                return self.order 
            elif (self.is_unique_update() and self.is_update_in_order() and self.is_valid_transition()):
                self.current_order.status = self.order.status
                self.current_order.updateId = self.order.updateId
                if self.order.is_valid_attribute('amount'):
                    self.current_order.amount = self.order.amount
                return self.current_order
        return None
        
    '''
    Checks whether order update contains the mandatory fields
    '''
    def is_valid_update(self):
        if self.order.is_valid_attribute("orderId") and \
           self.order.is_valid_attribute("status") and \
           self.order.is_valid_attribute("updateId"):
            return True
        return False
    
    '''
    Checks whether order with new status is valid
    '''
    def is_update_new(self):
        if not self.order_repository.is_order_exists(self.order) and self.status == 'NEW':
            return True
        return False
        
    '''
    Checks whether the update is unique
    '''
    def is_unique_update(self):
        self.current_order = self.order_repository.get_order(self.order)
        self.current_update_id = self.current_order.updateId
        self.current_status = self.current_order.status
        if self.update_id == self.current_update_id:
            return False
        return True
    
    '''
    Checks whether updateId is greater than the previous updateId of the same order
    '''
    def is_update_in_order(self):
        if self.update_id > self.current_update_id:
            return True
        return False 
            
    '''
    Checks whether status transition is valid for the order_updates
    '''
    def is_valid_transition(self):
        if self.current_status == "NEW" and (self.status == "COOKING" or self.status == 'CANCELED'):
            return True
        elif self.current_status == "COOKING" and (self.status == "DELIVERING" or self.status == 'CANCELED'):
            return True
        elif self.current_status == "DELIVERING" and (self.status == "DELIVERED" or self.status == 'CANCELED'):
            return True
        elif self.current_status == "DELIVERED" and self.status == "REFUNDED":
            return True
        return False       