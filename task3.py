mark = int(input("Enter your mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark < 33:
    print("Fail")
elif mark < 45:
    print("D")
elif mark < 60:
    print("C")
elif mark < 80:
    print("B")
else:
    print("A")