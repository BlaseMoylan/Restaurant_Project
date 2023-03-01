from order import Order
class Pizza(Order):
    def __init__(self) -> None:
        super().__init__('Pizza', 25)