import math

num_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

num_boxes = math.ceil(num_items / items_per_box)
print()

print(f"For {num_items} items packing {items_per_box} items in each box,")
print(f"you will need {num_boxes} boxes.")