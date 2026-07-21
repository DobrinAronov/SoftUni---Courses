import re


def check_valid_barcode(barcode: str) -> bool:
    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
    match = re.search(pattern, barcode)
    if match:
        return True
    return False


number_of_barcodes = int(input())

for number in range(number_of_barcodes):
    current_string = input()
    is_valid = check_valid_barcode(current_string)
    if is_valid:
        digits_pattern = r"\d"
        match_digits = re.findall(digits_pattern, current_string)
        if not match_digits:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(match_digits)}")
    else:
        print("Invalid barcode")
