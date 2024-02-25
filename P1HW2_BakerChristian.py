# Christian Baker
# February 25th, 2024
# P1HW2
# This program calculates and displays travel expenses.
# remaining_balance = a-(b + c + d) 

a = int(input('Enter Budget:'))
where = input("Enter your travel destination:")
b = int(input("How much do you think you will spend on gas?"))
c = int(input("Approximately, how much will you need for accomodation/hotel?"))
d = int(input("Last, how much do you need for food?"))

print()

print('-------------', 'Travel Expenses' '-------------')

print('Location:', where)
print("Initial Budget:", a)
print()
print("Fuel:", b)
print("Accomodation:", c)
print("Food:", d)
print()
remaining_balance = a - (b + c + d)
print("Remaining Balance:", remaining_balance)

