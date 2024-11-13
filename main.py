bill=int(input("Enter units used:"))

if bill<50:
    amount=50 * 2.60
    tax=25
    total=amount+tax
    print("Amount that shold be payed is ",total)
elif bill<100:
    amount=100 * 3.25
    tax=35
    total=amount+tax
    print("Amount that shold be payed is ",total)
elif bill<200:
    amount=200 * 5.26
    tax=45
    total=amount+tax
    print("Amount that shold be payed is ",total)