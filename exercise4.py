# Write a python program to enter three subject of marks from the user and store them into a dictionary.

# start with empty dictionary and add one by one marks.

# Initialize an empty dictionary to store marks
marks_dict = {}

# List of subjects
subjects = ["Math", "Science", "English"]

# Loop to enter marks for each subject
for subject in subjects:
    while True:
        try:
            # Input marks from the user
            marks = float(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:  # Assuming marks are out of 100
                marks_dict[subject] = marks
                break  # Exit the loop if input is valid
            else:
                print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Display the marks dictionary
print("\nMarks Dictionary:")
print(marks_dict)
