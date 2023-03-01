from logger import logger
from order_factory import Order_Factory
from validation import Order_Validation

class Franchise:
    def __init__(self,location_number:int) -> None:
        self.location_number=location_number
    def place_order(self):
        # ask a user what food they would like to order
        user_order=Order_Validation.real_order()
        #call the static OrderFactory.create_order() method 
        order=Order_Factory.create_order(user_order)
        # to instantiate an order object.
        #call the logger.log_transaction() method 
        logger.log_transaction(order,self.location_number)
        # to log the order to the log.txt file
