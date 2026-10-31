
def formula(mass:int) -> int:
    speed_of_light = pow(300000000,2)
    Energy = mass * speed_of_light
    return Energy


def main() -> None :
    mass = int(input("m: "))
    print("E: ",formula(mass))

if __name__ == "__main__":
    main()
