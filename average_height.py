student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
total_height = 0
number_of_students = 0 
average_height = 0

for height in student_heights:
    total_height += height

print(total_height)

for number in student_heights:
    number_of_students = number_of_students + 1    
  
print(number_of_students)
  
average_height = total_height / number_of_students

print(average_height)
    
    