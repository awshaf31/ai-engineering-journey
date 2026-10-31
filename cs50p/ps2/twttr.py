s = input("Input: ")
vowels = ['A','E','I','O','U','a','e','i','o','u']
print("Output : ", end="")

for c in s:
    if c in vowels:
        continue
    else:
        print(c, end="")
print()
