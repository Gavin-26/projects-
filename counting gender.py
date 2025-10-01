def get_class_size():
    while True:
        try:
            size = int(input("Enter class size (1–80): "))
            if 1 <= size <= 80:
                return size
            else:
                print("Error: must be between 1 and 80")
        except ValueError:
            print("Error: enter an integer")

def get_gender(student_number):
    while True:
        gender = input(f"Enter gender for student {student_number} (M/F): ").strip().upper()
        if gender in ("M", "F"):
            return gender
        else:
            print("Error: enter M or F")

def count_genders(class_size):
    boys = 0
    girls = 0
    for i in range(1, class_size + 1):
        gender = get_gender(i)
        if gender == "M":
            boys += 1
        else:
            girls += 1
    return boys, girls

def main():
    print("---------------------------------")
    print("      Class Gender Splitter")
    print("---------------------------------")
    class_size = get_class_size()
    boys, girls = count_genders(class_size)
    boy_percent = (boys / class_size) * 100
    girl_percent = (girls / class_size) * 100
    print(f"\nPercentage of boys: {boy_percent:.1f}%")
    print(f"Percentage of girls: {girl_percent:.1f}%")
    print("---------------------------------")

if __name__ == "__main__":
    main()
