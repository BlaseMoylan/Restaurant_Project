from order import Order
class Pasta(Order):
    def __init__(self) -> None:
        super().__init__('Pasta',75)