'''
Created on Apr 30, 2018

@author: eanuama
'''

import json

from threading import Thread
from json.decoder import JSONDecodeError

class OrderProducer(object):
    '''
    classdocs
    
    '''

    def __init__(self, queue):
        '''
        Constructor
        '''
        self.order_queue = queue
        self.create_producer_thread()
        
    '''
    Creates producer thread that listens for order_updates
    '''    
    def create_producer_thread(self):
        producer_thread = Thread(target=self.listen_order_updates)
        producer_thread.start()
        
    '''
    Listens to the order_updates sent from kitchen and delivery ship
    '''    
    def listen_order_updates(self):
        EOF = ""
        print ("Provide the order updates:")
        while True:
            individual_order_update = input()
            if individual_order_update == EOF:
                break
            self.process_order(individual_order_update)
        self.process_order(None)
        
    '''
    Adds order updates in queue
    '''    
    def process_order(self, json_order_string):
        if json_order_string is None:
            self.order_queue.put(None)
        else:
            order = self.json_to_order_object(json_order_string)
            if order:
                self.order_queue.put(order)
                
    '''
    converts json string to dictionary
    '''
    def json_to_order_object(self, json_order_string):
        try:   
            order = json.loads(json_order_string)
            return order
        except JSONDecodeError as e:
            print ("Invalid Json format: " + e.msg)
            return None