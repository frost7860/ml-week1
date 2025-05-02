n = int(input("enter number of student: "))
d = {}
for i in range(n):
    key = input("rollNumber: ")
    value = input("Name: ")
    d[key] = value

print(d)
