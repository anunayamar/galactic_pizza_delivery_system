'''
Created on Apr 30, 2018

@author: eanuama
'''
from concurrent.futures.thread import ThreadPoolExecutor

from threading import Thread
from src.order_repo import OrderRepo
from src.order_validation_engine import OrderValidationEngine
from src.order_wrapper import OrderWrapper

class OrderConsumer(object):
    '''
    classdocs
    '''
    #maximum number of consumer thread
    MAX_THREAD_NUM = 10
    
    '''
    Creates thread pool, so that jobs can be submitted to the available thread from the thread pool.
    '''
    def __init__(self, queue, order_repository):
        '''
        Constructor
        '''
        self.order_queue = queue
        self.order_repository = order_repository
        self.thread_pool = list()
        self.initalize_threads()
        self.create_consumer_thread()
        
    '''
    Creating thread pools, each thread pool contain 1 worker thread. 
    '''
    def initalize_threads(self):
        for i in range(self.MAX_THREAD_NUM):
            self.thread_pool.append(ThreadPoolExecutor(max_workers=1, thread_name_prefix="Thread_"+str(i+1)))
            
    '''
    Creates consumer thread. Makes sure that main thread wait for consumer_thread to die. 
    '''
    def create_consumer_thread(self):
        consumer_thread = Thread(target=self.fetch_order)
        consumer_thread.start()
        consumer_thread.join()

    '''
    Takes order from the queue and submit it to the thread pool for execution.
    '''
    def fetch_order(self):
        while True:
            order = self.order_queue.get()
            if order is None:
                break
            executor = self.thread_pool[order['orderId']%10]
            executor.submit(self.process_order, order)

    '''
    Calls order_validators and stores the order in the repo.
    '''
    def process_order(self, order):
        order_wrapper = OrderWrapper(order)
        order_validator = OrderValidationEngine(self.order_repository, order_wrapper)
        order_wrapper = order_validator.validate_all()
        if order_wrapper:
            self.order_repository.add_order(order_wrapper)