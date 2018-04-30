class OrderRepo:
    '''
    Stores the order in the dict with key as orderId and value as order
    '''
    def __init__(self):
        self.order_map = dict()
    
    def add_order(self, order):
        self.order_map[order.orderId] = order
        
    def remove_order(self, order):
        del self.order_map[order.orderId]
        
    def get_order(self, order):
        return self.order_map[order.orderId]
        
    def is_order_exists(self, order):
        if order.orderId in self.order_map:
            return True
        return False

    '''
    prints summary according to the set rules
    '''        
    def show_summary(self):
        new_count = cooking_count = delivering_count = delivered_count = canceled_count = refunded_count = amount_charged = 0
        for order_id, order in self.order_map.items():
            status = order.status        
            if status == "NEW":
                new_count += 1
            elif status == "COOKING":
                cooking_count += 1
                amount_charged += order.amount
            elif status == "DELIVERING":
                delivering_count += 1
                amount_charged += order.amount
            elif status == "DELIVERED":
                delivered_count += 1
                amount_charged += order.amount
            elif status == "CANCELED":
                canceled_count += 1
            elif status == "REFUNDED":
                refunded_count += 1
                                
        print ("New: " + str(new_count))
        print ("Cooking: " + str(cooking_count))
        print ("Delivering: " + str(delivering_count))
        print ("Delivered: " + str(delivered_count))                
        print ("Canceled: " + str(canceled_count))
        print ("Refunded: " + str(refunded_count))
        print ("Total amount charged: $" + str(amount_charged))