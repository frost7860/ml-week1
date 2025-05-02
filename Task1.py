
marks = []

for i in range(3):
    print(f"\nEnter marks for Student {i+1}:")
    student_marks = []
    for j in range(3):
        mark = int(input(f"  Subject {j+1} marks: "))
        student_marks.append(mark)
    marks.append(student_marks)

# Display the matrix with total and average
print("\nMarks Matrix with Total and Average:")
for i, student in enumerate(marks, start=1):
    total = sum(student)
    average = total / len(student)
    print(f"Student {i}: Marks = {student}, Total = {total}, Average = {average:.2f}")
