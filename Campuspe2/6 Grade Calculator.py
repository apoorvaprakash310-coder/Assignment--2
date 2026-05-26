# Grade Calculator Program

marks = []

# Ask the user to enter marks for 5 subjects
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Show the marks entered by the user
print("\nMarks in each subject:")
for i, mark in enumerate(marks, start=1):
    print(f"Subject {i}: {mark}")

# Find total marks and percentage
total_marks = sum(marks)
percentage = (total_marks / 500) * 100

print("\nTotal Marks:", total_marks)
print("Percentage:", round(percentage, 2))

# Decide the grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# Check if the student passed in all subjects
if all(mark >= 40 for mark in marks):
    print("Result: Pass")
else:
    print("Result: Fail")