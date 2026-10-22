
def sum_to(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

def count_even(numbers_to: int) -> int:
    count = 0
    for i in range(1, numbers_to + 1):
        if i % 2 == 0 :
            count = count + 1
    return count
    
def main() -> None:
    assert sum_to(5) == 15
    assert sum_to(0) == 0
    assert count_even(10) == 5
    assert count_even(1) == 0
    print("All checks passed")
    
  
if __name__ == "__main__":
    main()
