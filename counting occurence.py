# Global constant
PASS_MARK = 50

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

def get_student_mark(student_number):
    while True:
        try:
            mark = int(input(f"Enter mark for student {student_number}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Error: must be between 0 and 100")
        except ValueError:
            print("Error: enter an integer")

def count_passes(class_size):
    passes = 0
    for i in range(1, class_size + 1):
        mark = get_student_mark(i)
        if mark >= PASS_MARK:
            passes += 1   # Counting Occurrences
    return passes

def main():
    print("---------------------------------")
    print("   AberClyde Exam Pass Checker")
    print("---------------------------------")
    class_size = get_class_size()
    passes = count_passes(class_size)
    print(f"\nNumber of students who passed: {passes}")
    print("---------------------------------")

if __name__ == "__main__":
    main()
