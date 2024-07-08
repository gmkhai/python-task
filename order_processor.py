"""
Untuk class ini nanti inheritance dengan order
kemudian mencoba mengakses beberapa attribute order yang bersifat private
"""
from order import Order


class OrderProcessor(Order):
    total_tax = 0

    def __init__(self):
        self.__orders = []

    def add_order(self, order: Order):
        self.__orders.append(order)

    def calculate_total_revenue(self):
        total_revenue = 0
        for order in self.__orders:
            total_revenue += order.total_amount
        return total_revenue

    def calculate_total_tax(self, tax_rate: float):
        for order in self.__orders:
            self.total_tax += order.calculation_tax(tax_rate=tax_rate)
        return self.total_tax

    def display_order(self):
        display = "="*50
        for order in self.__orders:
            display += order.display_order()
            display += "\n"
        display += "="*50
        display += f"\nTotal Revenue\t\t\t: Rp.{self.calculate_total_revenue()}"
        display += f"\nTotal Tax\t\t\t\t: Rp.{self.total_tax}"
        return display

