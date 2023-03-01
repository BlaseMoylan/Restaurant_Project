from pizza import Pizza
from pasta import Pasta
from salad import Salad
#As a developer, I want to create an Order Factory class 
# with a static create_order method.
#create instance of an order
 #Factory pattern
 #return the corresponding type of Order child class instantiation
class Order_Factory:
    @staticmethod
    def create_order(order):
        menu_items=[Pizza(),Pasta(),Salad()]
        return menu_items[order]