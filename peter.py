# read the number of students

n  = int(input("Enter the number of students:: "))

# read the names and scores of all students

students = []
for _ in range (n):
    name  = input("name:: ")
    score = float(input("score:: "))
    students.append([name,score])
# find all unique scores 

scores_list = []

for student in students:
    score = student[1]
    if score not in scores_list:
        scores_list.append(score)

# sort the scores and get the second lowest

scores_list.sort()
second_lowest = scores_list[1]

# find all students with the second lowest score

second_lowest_students = [] 
for student in students:
    if student[1] ==second_lowest:
        second_lowest_students.append(student[0])

# sort  names alphabetically 

second_lowest_students.sort()

#print each name 

for name in second_lowest_students:
    print(name,"::")
    