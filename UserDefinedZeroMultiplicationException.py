# Create a user-defined exception to display a proper message when the value of (b*d) is zero.
class ZeroProductError(Exception):
    def __init__(self, message="The product of b and d should not be zero."):
        self.message = message
        super().__init__(self.message)

# Example usage:
b = 0
d = 5

if b * d == 0:
    raise ZeroProductError()
