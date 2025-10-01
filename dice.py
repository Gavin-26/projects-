import random

def generate_numbers():
    """Generate 50 random numbers between 1 and 10."""
    numbers = []
    for _ in range(50):
        numbers.append(random.randint(1, 10))
    return numbers

def count_occurrences(numbers):
    """Count how many times each number (1–10) occurs."""
    counts = [0] * 11   # index 0 not used
    for num in numbers:
        counts[num] += 1
    return counts

def display_results(counts):
    """Display numbers generated more than 4 times."""
    print("Numbers generated more than 4 times:")
    for number in range(1, 11):
        if counts[number] > 4:
            print(f"Number {number} occurred {counts[number]} times")

def main():
    numbers = generate_numbers()
    counts = count_occurrences(numbers)
    display_results(counts)

if __name__ == "__main__":
    main()
