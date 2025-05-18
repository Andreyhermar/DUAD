
number_list = []
print("Enter 3 numbers to find the highest among them")
for i in range(3):
    number = int(input(f"Enter number {i + 1}: "))  # Ask for each number
    number_list.append(number)
highest = max(number_list)

print(f"The highest number among {number_list} is: {highest}")