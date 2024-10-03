class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(real_part, imaginary_part)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_part, imaginary_part)

    def modulus(self):
        return (self.real**2 + self.imaginary**2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# Example usage
if __name__ == "__main__":
    # Create two complex numbers
    c1 = ComplexNumber(3, 2)  # 3 + 2i
    c2 = ComplexNumber(1, 7)  # 1 + 7i

    # Perform operations
    print(f"c1: {c1}")
    print(f"c2: {c2}")
    
    print(f"Addition: {c1} + {c2} = {c1 + c2}")
    print(f"Subtraction: {c1} - {c2} = {c1 - c2}")
    print(f"Multiplication: {c1} * {c2} = {c1 * c2}")
    print(f"Division: {c1} / {c2} = {c1 / c2}")
    
    print(f"Modulus of c1: |{c1}| = {c1.modulus()}")
    print(f"Conjugate of c1: {c1.conjugate()}")

