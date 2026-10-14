


def average(total:float,days:int) ->float :
    return total/days


def main() -> None :
    total = 0
    for i in range(5):
        number = float(input("Enter a number : "))
        total = total + number
    print ("Total: ",float(total))
    print("Average : ",average(total,5))
if __name__ == "__main__" :
    main()
    
   