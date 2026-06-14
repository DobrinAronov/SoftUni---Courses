def computer_receipt(total: float, price: float) -> tuple[float, str]:
    if price < 0:
        return total, "Invalid price!"
    total += price
    return total, ''


price_without_taxes = 0
taxes = 0
#is_special = False

while (current_command := input()) not in ('special', 'regular'):

    part_price = float(current_command)

    price_without_taxes, message = computer_receipt(price_without_taxes, part_price)
    if message:
        print(message)

if price_without_taxes == 0:
    print("Invalid order!")
else:
    taxes = price_without_taxes * 0.2
    total_price = price_without_taxes + taxes
    if current_command == 'special':
        total_price -= total_price * 0.1
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price_without_taxes:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\nTotal price: {total_price:.2f}$")