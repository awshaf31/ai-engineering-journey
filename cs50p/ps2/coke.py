amount_due = 50
print("Amount Due:", amount_due)
accepted_coin = [25,10,5]


while True:
    insert_coin = int(input("Insert Coin : "))

    if insert_coin in accepted_coin:
        amount_due -= insert_coin
        print("Amount Due:", amount_due)

        if amount_due <= 0:
            change_owed = abs(amount_due)
            print("Change Owed:", change_owed)
            break
    else:
        print("Amount Due:", amount_due)

