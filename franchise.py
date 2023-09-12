
from logger import logger
from order_factory import Order_Factory
from validation import Order_Validation

class Franchise:
    """
    The `Franchise` class represents a franchise store in a retail system.

    Attributes:
    - location_number (int): The unique identifier for the franchise store.

    Methods:
    - __init__(self, location_number: int): Initializes a new franchise store with a specified location number.
    - place_order(self): Places an order at the franchise store using the Order_Factory and logs the transaction.

    Example Usage:
    >>> store_one = Franchise(1)
    >>> store_one.place_order()
    """

    def __init__(self, location_number: int) -> None:
        """
        Initializes a new franchise store with a specified location number.

        Args:
        - location_number (int): The unique identifier for the franchise store.
        """
        self.location_number = location_number

    def place_order(self):
        """
        Places an order at the franchise store using the Order_Factory and logs the transaction.
        """
        # Create an order using the Order_Factory
        order = Order_Factory.create_order()

        # Log the transaction, associating it with the store's location number
        logger.log_transaction(order, self.location_number)