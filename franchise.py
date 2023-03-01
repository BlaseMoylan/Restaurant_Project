from logger import Logger
from order_factory import Order_Factory

class Franchise:
    def __init__(self,location_number:int) -> None:
        self.location_number=location_number
    def place_order(self,order:str):
        # ask a user what food they would like to order
        #call the static OrderFactory.create_order() method 
        # to instantiate an order object.
        #call the logger.log_transaction() method 
        # to log the order to the log.txt file

        pass