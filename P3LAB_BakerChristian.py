#Christian Baker
#P3LAB
#March 14th, 2024
#Write a code that produces the results required of lab assignment "Leap Year" in Zybooks.

input_year = int(input('Enter a year:'))

if (input_year%400==0) or (input_year%4==0):
    print(input_year, '-', 'leap year')
    is_leap_year = True
else:
    print(input_year, '-', 'not a leap year')
    is_leap_year = False

    
