"""

"""


class Order:

    def __init__(self, order_id: str, customer_name: str, order_date: str, total_amount: float):
        self.__order_id = order_id
        self.__customer_name = customer_name
        self.__order_date = order_date
        self.__total_amount = total_amount

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, order_id: str):
        self.__order_id = order_id

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

    @property
    def order_date(self):
        return self.__order_date

    @order_date.setter
    def order_date(self, order_date: str):
        self.__order_date = order_date

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, total_amount: float):
        self.__total_amount = total_amount

    def calculation_tax(self, tax_rate: float):
        # Validation tax_rate value only 0 - 1
        if 0 <= tax_rate >= 1:
            return None
        else:
            tax_amount = self.__total_amount * tax_rate
            return tax_amount

    def display_order(self):
        display = f"\nOrder ID\t\t\t\t: {self.__order_id}"
        display += f"\nCustomer Name\t\t\t: {self.__customer_name}"
        display += f"\nOrder Date\t\t\t\t: {self.__order_date}"
        display += f"\nTotal Amount\t\t\t: Rp.{self.__total_amount}"
        return display
