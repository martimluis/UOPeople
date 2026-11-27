grades = []
prompt = "Enter a grade between 0 and 100 (or 'done' to finish): "
entry = input(prompt).strip().lower()

while entry != "done":
    try:
        grade = float(entry)  # check that the input is a number
        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Invalid grade: it must be between 0 and 100.")
    except ValueError:
        print("Invalid input: please enter a number or 'done'.")
    entry = input(prompt).strip().lower()

print("Grades entered:", grades)