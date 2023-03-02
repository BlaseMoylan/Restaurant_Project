from pizza import Pizza
from pasta import Pasta
from salad import Salad
from validation import Order_Validation
#As a developer, I want to create an Order Factory class 
# with a static create_order method.
#create instance of an order
 #Factory pattern
 #return the corresponding type of Order child class instantiation
class Order_Factory:
    @staticmethod
    def create_order():
        menu_items=[Pizza(),Pasta(),Salad()]
        order=Order_Validation.real_order(menu_items)
        return menu_items[order]