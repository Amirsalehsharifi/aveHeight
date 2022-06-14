
# .split will make a list of inputs seperated with spaces in input

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# not use len() and sum()
total_height = 0
for i in student_heights:
    total_height +=i

num_students = 0
for i in student_heights:
    num_students +=1

ave_students_height = total_height/num_students
print(round(ave_students_height))
