from logger import logger
from order_factory import Order_Factory

class Franchise:
    def __init__(self,location_number:int) -> None:
        self.location_number=location_number
    def place_order(self):
        # ask a user what food they would like to order
        user_order=self.real_order()
        #call the static OrderFactory.create_order() method 
        order=Order_Factory.create_order(user_order)
        # to instantiate an order object.
        #call the logger.log_transaction() method 
        logger.log_transaction(order,self.location_number)
        # to log the order to the log.txt file

    def real_order(self):
        user_input=False
        while user_input==False:
            user_order=input('what are you ordering? \npress 0 for Pizza\npress 1 for Pasta\npress 2 for Salad')
            if user_order.isnumeric():
                user_order=int(user_order)
                menu=['Pizza','Pasta','Salad']
                if user_order<len(menu):
                    user_input=True
                    return user_order
                else:
                    print('this is not one of the options! Please order something else.')
            else:
                print('this is not one of the options! Please order something else.')