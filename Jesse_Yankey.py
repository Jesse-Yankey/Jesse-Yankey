name = input("Enter name: ")
print (name, " You're welcome to this section")
number = int(input("Enter any number to find it's multiplication table: "))
numberlimit = int(input("Enter limit of the multiplication table: "))
print("Multiplication table of ", number, "from 1 to", numberlimit)
for a in range(1, numberlimit +1):
	print(number, " * ", a, " = ", number * a)