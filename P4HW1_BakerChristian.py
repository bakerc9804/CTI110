# Christian Baker
# April 11th, 2024
# P4HW1
# This program will use a loop to collect scores, and after displaying score average (after dropping lowest score), the program is to display a letter grade for the calculated average.

#1 Ask the user to type their desired score amount
# score_amount = int(input("How many scores do you want to enter?"))
#2 Build a list for storing scores
# list_of_scores = []
#3 Make loop to get score input from user
# for i in range(score_amount):
      #3a Use while loop to make sure that a VALID score in input
       # while True:
              ## Ask the user to enter scores
             #score = float(input("Enter score #:"))

              ## See if the inputted score is valid
            #if score < 0 or score > 100:
                    #print("invalid score entered! Score should be between 0 and 100!")
                    #while True:
                    #score = float(input("Enter score {} again: ".format(i + 1)))
                    #if 0 <= score <= 100:
                               #BREAK the loop
                    #list_of_scores.append(score)

#4 Calculate the lowest score from input
# lowest_score = min(list_of_scores)
#5 Remove the lowest score from list
#list_of_scores.remove(lowest_score)
#6 Calculate the score average of the refined list
#average = sum(list_of_scores) / len(list_of_scores)
#7 Determine the letter grade for average
#if 90 <= average <= 100:
     #print('A')
#elif 80 <= average < 90:
     #print('B')
#elif 70 <= average < 80:
     #print('C')
#elif 60 <= average < 70:
     #print('D')
#else:
     #print('F')
#8 Display results
##print("Lowest Score: (lowest_score)")
##print("Modified List: (list_of_scores)")
##print("average: (average)")
##print("Letter grade: (letter_grade)")



score_amount = int(input("How many scores do you want to enter?"))

list_of_scores = []

for i in range(score_amount):
            score = float(input("Enter score:"))

            if score < 0 or score > 100:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
                while True:
                   score = float(input("Enter score {} again: ".format(i + 1)))
                   if 0 <= score <= 100:
                       break
            list_of_scores.append(score)

lowest_score = min(list_of_scores)

list_of_scores.remove(lowest_score)

average = sum(list_of_scores) / len(list_of_scores)

if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average < 90:
    grade = 'B'
elif 70 <= average < 80:
    grade = 'C'
elif 60 <= average < 70:
    grade = 'D'
else:
    grade = 'F'

print("--------------Results--------------")
print("Lowest Score:", lowest_score)
print("Modified List: {}".format(list_of_scores))
print(f"Scores Average: {average:.2f}")
print("Grade:", grade)

