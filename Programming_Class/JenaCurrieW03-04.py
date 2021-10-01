print("\n")
childprice = float(input("How much does a child's meal cost? $"))
childamount = int(input("How many child meals? "))
adultprice = float(input("How much does an adult's meal cost? $"))
adultamount = int(input("How many adult meals? "))
taxrate = float(input("What is the sales tax rate? "))
subtotal= childprice*childamount+adultprice*adultamount
tax= taxrate/100*subtotal
total= tax+subtotal

print("\n")
print("------------------------------")
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("------------------------------")
print("\n")

payment = float(input("Amount paid: $"))
change = payment-total
print(f"Change due: ${change:.2f}")
print("\n")
