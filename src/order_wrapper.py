'''
Created on Apr 30, 2018

@author: eanuama
'''

class OrderWrapper(object):
    '''
    classdocs
    
    Wrapper class over object dictionary. Provides easy access to dictionary object. 
    For example: order.updateId can be used instead of order['updateId']
    '''
    def __init__(self, order_dict):
        '''
        Constructor
        '''
        self.__dict__ = order_dict
        
    def is_valid_attribute(self, key):
        return key in self.__dict__    