print("Yaya's Store")
from datetime import datetime
import csv
today=datetime.now()
dow=today.weekday() # Monday is 0 and Sunday is 6
PRODUCT_NUMBER_INDEX=0
NAME_INDEX=1
PRICE_INDEX=2
TAX_RATE=0.06

def read_dictionary(filename, key_column_index):
    products_dictionary={}
    with open(filename, "rt") as infile:
        reader=csv.reader(infile)
        next(reader) # Skip the header row.
        for row in reader:
            if len(row) !=0:
                key = row[key_column_index]
                products_dictionary[key]=row

    return products_dictionary

def main ():
    try:
        products_dictionary=read_dictionary("products.csv", 0)
    
        subtotal=0
        total_items=0

        with open("request.csv", "rt") as receipt_file:
            reader=csv.reader(receipt_file)
            next(reader) # Skip the header row.
            for row in reader:
                if len(row) !=0: 
                    product_number=row[PRODUCT_NUMBER_INDEX]
                    quantity=int(row[1])
                    product=products_dictionary[product_number]
                    name=product[NAME_INDEX]
                    price=float(product[PRICE_INDEX])
                    print(f"{name} {quantity} @ {price: .2f}")
                    subtotal+=price*quantity
                    total_items+=quantity   
        tax=round(subtotal*TAX_RATE, 2)
        total=subtotal+tax
        print(f"Number of items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {tax:.2f}")
        print(f"Total: {total:.2f}")

        print("Thank you for shopping at the Yaya's Store!")
        current_date = today.strftime("%a %b %d %I:%M:%S %Y")
        print(current_date)

    except KeyError as Error:
        print(type(Error).__name__, Error)
    except FileNotFoundError as Error:
        print(type(Error).__name__, Error)  
                
                
if __name__ == "__main__":
    main()  