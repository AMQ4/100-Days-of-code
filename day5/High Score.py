students_score = input("Input a list of student scores ").split()

max = int(students_score[0])

for i in students_score:

    if max < int(i):
        max = int(i)
print(f"The highest score in the class is: {max}")