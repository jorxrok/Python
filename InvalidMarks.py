# Make an "Invalid Marks" exception class that is thrown when marks obtained by a student exceed 100.
class InvalidMarksError(Exception):
    def __init__(self, message="Invalid Marks: Marks should not exceed 100."):
        self.message = message
        super().__init__(self.message)

# Example usage:
def check_marks(marks):
    if marks > 100:
        raise InvalidMarksError("Marks should not exceed 100.")
    else:
        print("Marks are valid.")

# Test with marks
student_marks = 105

try:
    check_marks(student_marks)
except InvalidMarksError as e:
    print(e)
