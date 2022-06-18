# Ask user to input the list of student heights
# Store heights into a list
student_heights = input("Input a list of student heights ").split()
# Convert each list item to int
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Declare new variable to store sum of heights and also the number of student as couter
sum_of_heights = 0
counter = 0
for x in student_heights:
    sum_of_heights += x
    counter += 1
average = round(sum_of_heights / counter)
print(average)