"""PROGRAM NO:01"""


my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

smallest = my_list[0]

for num in my_list:
    if num < smallest:
        smallest = num

print("Smallest number is:", smallest)


"""PROGRAM NO:02"""


my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

total = 0

for num in my_list:
    total = total + num

average = total / len(my_list)

print("Average is:", average)


"""PROGRAM NO:03"""


students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]

name = input("Enter student name: ")

if name in students:
    print("Student Found")
else:
    print("Student Not Found")



"""PROGRAM NO:04"""

shopping = []

for i in range(5):
    item = input("Enter shopping item: ")
    shopping.append(item)

print("Shopping List:", shopping)