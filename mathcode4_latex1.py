import sympy as sp

# Enable pretty printing
sp.init_printing(use_unicode=True)

# Define symbols
x = sp.symbols('x')

# Define the expression inside the integral
expression = sp.sin(x**2) + sp.cos(x)

# Create unevaluated Integral object
integral_expr = sp.Integral(expression, (x, 0, sp.pi))

# Print out the formatted integral expression
print("Integral Expression:")
sp.pprint(integral_expr)

'''
### Additional Considerations for Advanced Formatting Needs

If your goal extends beyond just viewing these equations in PyCharm into creating documents (like exams), consider
exporting these equations into LaTeX format which can then be embedded into document creation tools such as LaTeX editors or even Word documents with MathType:

The script below outputs LaTeX code which visually represents your mathematical formula when compiled with a LaTeX editor.

Using this approach provides flexibility:
1. Directly view mathematically well-formatted expressions within development environments supporting Unicode rendering.
2. Export complex mathematical notations into standard documentation formats ensuring high-quality representations suitable for 
academic purposes including but not limited to exams preparation/distribution tasks!

'''


latex_output = sp.latex(integral_expr)
print("LaTeX Representation:")
print(latex_output)