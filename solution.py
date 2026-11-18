from fractions import Fraction

def solve(value):
    return (lambda f: {"numerator": f.numerator, "denominator": f.denominator})(Fraction(value[0], value[1]))
