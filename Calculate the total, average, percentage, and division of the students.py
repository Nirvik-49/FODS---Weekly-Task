'''
Program takes the marks of 5 subjects from the user, calculates the total, average, percentage,
and determines the division based on the specified criteria.
'''

# Function to calculate total, average, percentage, and division
def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    percentage = (total / 500) * 100  # Assuming each subject is out of 100

    # Determine division based on percentage
    if percentage >= 80:
        division = "Distinction"
    elif percentage > 60:
        division = "First Division"
    elif percentage > 50:
        division = "Second Division"
    elif percentage > 45:
        division = "Third Division"
    else:
        division = "Fail Division"

    return total, average, percentage, division

# Input from user
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter the marks for subject {i}: "))
    marks.append(mark)


# Calculate results
total, average, percentage, division = calculate_results(marks)

# Display output of the program
print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Division: {division}")
