from order import Order
class Salad(Order):
    def __init__(self) -> None:
        super().__init__('Salad', 50)