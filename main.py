from datetime import datetime
from order import Order
from order_processor import OrderProcessor

order_process = OrderProcessor()
is_more = True
is_error_command = False
order_id = 0
while is_more:
    try:
        if not is_error_command:
            order_id += 1
            customer_name = input("Customer Name\t\t\t\t\t: ")
            total_amount = int(input("Total Amount\t\t\t\t\t: "))
            print("")
            order = Order(order_id=f"ORD-{order_id}", customer_name=customer_name,
                          order_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                          total_amount=total_amount)
            order_process.add_order(order)
            command_order = input("Are you add more order?[Y/N]\t: ")
            if command_order.lower() == "y":
                is_more = True
                is_error_command = False
            elif command_order.lower() == "n":
                is_more = False
                is_error_command = False
            else:
                is_error_command = True
                print("Sorry, your command not available")
        else:
            while is_error_command:
                command_order = input("Are you add more order?[Y/N]\t: ")
                if command_order.lower() == "y":
                    is_more = True
                    is_error_command = False
                elif command_order.lower() == "n":
                    is_more = False
                    is_error_command = False
                else:
                    is_error_command = True
                    print("Sorry, your command not available")

    except ValueError:
        print("Sorry, You input value is not a number")
    except Exception as e:
        print("Sorry, You have problem when add this order")
        continue
tax_rate = float(input("Please input tax_rate\t\t\t: "))
# validation tax_rate
if 0 <= tax_rate >= 1:
    print("Tax rate out of range")
else:
    order_process.calculate_total_tax(tax_rate=tax_rate)
    print(order_process.display_order())