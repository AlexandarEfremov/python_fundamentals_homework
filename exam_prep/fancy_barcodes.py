import re

barcode_pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
product_group_pattern = r"[0-9]"

count_of_barcodes = int(input())

for i in range(count_of_barcodes):
    input_line = input()
    match = re.search(barcode_pattern, input_line)
    if match:
        product_group_match = re.search(product_group_pattern, input_line)
        if product_group_match:
            result = re.findall(product_group_pattern, input_line)
            print(f"Product group: {''.join(result)}")
        else:
            print(f"Product group: {'00'}")
    else:
        print("Invalid barcode")
