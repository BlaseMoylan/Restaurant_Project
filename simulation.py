from franchise import Franchise
from  Log_transaction_validation import Log_Transaction_validation
class Simulation:
    """
    The `Simulation` class represents a simulation of a franchise-based store system.

    Methods:
    - run_simulation(): Runs the simulation by creating franchise instances, placing orders, and logging transactions.

    Example Usage:
    >>> simulation = Simulation()
    >>> simulation.run_simulation()
    """

    def run_simulation(self):
        """
        Runs the simulation by creating franchise instances, placing orders, and logging transactions.
        """
        # Perform transaction validation logging
        Log_Transaction_validation.log_transaction_validation()

        # Create franchise instances
        store_one = Franchise(1)
        store_two = Franchise(2)
        store_three = Franchise(3)

        # Place orders at different franchise stores
        store_one.place_order()
        store_two.place_order()
        store_one.place_order()
        store_two.place_order()
        store_three.place_order()
        store_three.place_order()
        store_one.place_order()
        store_one.place_order()