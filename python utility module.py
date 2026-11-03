"""
Python Utility Module
Contains reusable functions for validation,
formatting, calculations, and file handling.
"""


def validate_email(email):
    """Check whether an email address is valid."""
    return "@" in email and "." in email


def format_name(name):
    """Format a name with proper capitalization."""
    return name.strip().title()


def calculate_percentage(part, total):
    """Calculate percentage of a value."""
    if total == 0:
        return 0
    return (part / total) * 100


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def write_to_file(filename, content):
    """Write content to a text file."""
    with open(filename, "w") as file:
        file.write(content)


def read_from_file(filename):
    """Read content from a text file."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."


def main():
    """Example program demonstrating utility functions."""
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    name = format_name(name)

    print("Formatted Name:", name)
    print("Valid Email:", validate_email(email))

    marks = [85, 90, 78, 88]
    average = calculate_average(marks)
    percentage = calculate_percentage(average, 100)

    print("Average Marks:", average)
    print("Percentage:", percentage)

    write_to_file("output.txt", "Name: " + name)

    print("File Content:")
    print(read_from_file("output.txt"))


if __name__ == "__main__":
    main()
