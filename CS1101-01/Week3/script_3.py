grades = []

while True:
    entry = input("Enter a grade between 0 and 100 (or 'done' to stop): ").strip().lower()

    if entry == "done":
        break  # stop entering grades completely

    try:
        grade = float(entry)  # check that the input is a number
    except ValueError:
        print("Invalid input: please enter a number or 'done'.")
        continue  # skip text that is not a number

    if grade < 0 or grade > 100:
        print("Invalid grade: it must be between 0 and 100.")
        continue  # skip grades outside the valid range

    grades.append(grade)

if grades:
    average = sum(grades) / len(grades)
    print(f"Average grade: {average:.2f}")
else:
    print("No grades were entered.")