from franchise import Franchise
from  Log_transaction_validation import Log_Transaction_validation
class Simulation:
    def run_simulation(self):
        #a run_simulation() method to act as a facade pattern. 
        #Instantiate 3 separate Franchise objects.
        #Call place_order() on each franchise object multiple times.
        Log_Transaction_validation.log_transaction_validation()
        store_one= Franchise(1)
        store_two= Franchise(2)
        store_three= Franchise(3)

        store_one.place_order()
        store_two.place_order()
        store_one.place_order()
        store_two.place_order()
        store_three.place_order()
        store_three.place_order()
        store_one.place_order()
        store_one.place_order()