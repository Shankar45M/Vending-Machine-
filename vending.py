print("item A-2$")
print("item B-35")
print("Item C-5$")
p=0
cancel=False
while cancel==False:
    while True:
        slc=input("Select Item")
        if slc=='A':
            p=p+2
            break
        elif slc=='B':
            p=p+3
            break
        elif slc=='C':
            p=p+5
            break
        else:
            print("Item not available")
            break
    con=input("Do you want to continue (yes/no)")
    if con=="no":
        print("Transaction Cancelled")
        cancel=True
        break
    amt=int(input("Insert $"))
    if amt==p:
        print("Dispensing Item")
        print("Your change is $0")
    elif amt>p:
        print("Dispensing Item")
        print("Your change is $",(amt-p))
    else:
        print("Insert additional $", (p-amt))
        add_amt=int(input("Insert $"))
    if add_amt==(p-amt):
        print("Dispensing Item")
        print("Your change is $0")
    con=input("Do you want to continue (yes/no)")
    if con=="yes":
        continue
    else:
        print("Thank you See you soon")
        break
