
def calculate_average(marks):
    if not marks:
        raise ValueError("Marks cannot be empty")
    return sum(marks) / len(marks)


if __name__ == "__main__":
    marks = [80, 75, 90, 85, 70]
    average = calculate_average(marks)

    print("Student Management System")
    print("Marks:", marks)
    print("Average:", average)
