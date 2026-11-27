classes = [["Alice", "Ben"], ["Chloe", "David"]]
class_number = 1

for class_list in classes:          # outer loop: each class
    print(f"Class {class_number}:")
    for student in class_list:      # inner loop: each student
        print(f"  - {student}")
    class_number += 1
