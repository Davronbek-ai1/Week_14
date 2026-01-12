manifest = [
    {'barcode': "A123", 'product_name': "Laptop", 'price': 1000.00},
    {'barcode': "B456", 'product_name': "Mouse", 'price': 25.50},
    {'barcode': "C789", 'product_name': "Monitor", 'price': 200.00}
]

scanned = ["A123", "B456", "D000"]

"""
Accepts a list of dictionaries: {'barcode': str, 'product_name': str, 'price': float}.
Returns a Dictionary where keys are barcodes and values are product names.
"""
def map_products(manifest):
    return {dictionary['barcode']: dictionary['product_name'] for dictionary in manifest}

"""
Accepts the product map and a list of scanned barcode strings.
Returns two Sets:
missing_items: Barcodes in the map but NOT scanned.
extra_items: Barcodes scanned but NOT in the map (unexpected items).
"""
def compare_shipment(product_map, scanned_barcodes):
    map_set = {barcode for barcode in product_map}
    scanned_set = set(scanned_barcodes)
    return map_set - scanned_set, scanned_set - map_set

"""
Accepts the original manifest list and the set of missing barcodes.
Uses a List Comprehension (or sum with a generator) to calculate the total price of the missing items.
Returns the total float value formatted or rounded to 2 decimal places.
"""
def calculate_missing_value(manifest, missing_set):
    return sum(dic['price'] for dic in manifest if dic['barcode'] in missing_set)

def main():
    product_map = map_products(manifest)
    missing_items, extra_items = compare_shipment(product_map, scanned)
    total_price = calculate_missing_value(manifest, missing_items)
    print(f"Missing Barcodes: {missing_items}")
    print(f"Extra Barcodes: {extra_items}")
    print(f"Total Value Lost: {round(total_price, 3)}")

main()

#print(f"Missing Barcodes: {compare_shipment(map_products(manifest), scanned)[0]}")
#print(f"Extra Barcodes: {compare_shipment(map_products(manifest), scanned)[1]}")
#print(f"Total Value Lost: {calculate_missing_value(manifest, compare_shipment(map_products(manifest), scanned)[0])}")
