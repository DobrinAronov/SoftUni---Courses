import re

pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

count_of_barcodes = int(input())

for num in range(count_of_barcodes):
    current_barcode = input()
    valid_barcode = re.search(pattern, current_barcode)
    if valid_barcode:
        for match in valid_barcode.groups():
            number = re.findall(r"\d+", match)
            if not number:
                print(f"Product group: 00")
            else:
                print(f"Product group: {''.join(number)}")
    else:
        print("Invalid barcode")
