'''
Created on Apr 30, 2018

@author: eanuama
'''
from src.order_producer_engine import OrderProducer
from src.order_consumer_engine import OrderConsumer
from src.order_repo import OrderRepo
from queue import Queue

class OrderEngine(object):
    """
    Creates producer and consumer threads for that processes the order updates. This improves the performance.
    Also, creates a blocking queue to store the order while it is processed
    order_repository stores the order updates
    """
    def __init__(self):
        order_queue = Queue()
        self.order_repository = OrderRepo() 
        self.producer = OrderProducer(order_queue)
        self.consumer = OrderConsumer(order_queue, self.order_repository)        
    
    """
    prints order summary
    """    
    def print_summary(self):
        self.order_repository.show_summary()
    
    
if __name__== '__main__':
    order_engine_obj = OrderEngine()
    order_engine_obj.print_summary()    