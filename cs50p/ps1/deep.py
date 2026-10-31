
Great_Question = input("What is the Answer to the Great Question of Life, the Universe, and Everything ? ").strip().lower()

if Great_Question == "42":
    print("Yes")
elif Great_Question == "forty-two":
    print("Yes")
elif Great_Question == "forty two":
    print("Yes")
else:
    print("No")

