# This is a sample Python script.

### Example: Integrate \( \sin(x^2) \) with respect to x


import sympy as sp

# Define the symbol for x (the variable of integration)
x = sp.symbols('x')

# Define the expression to integrate: sin(x^2)
expression = sp.sin(x**2)

# Compute the indefinite integral of sin(x^2) with respect to x
integral_result = sp.integrate(expression, x)

# Pretty Print the original equation and its integral
print("Integral of sin(x^2) dx:")
sp.pprint(integral_result)

from sympy import symbols, sin, Integral
import webbrowser

# Define symbol and expression
x = symbols('x')
expression = sin(x**2)
integral_expression = Integral(expression, x).doit()

# Convert expression to a LaTeX formatted string
latex_code = f"\\[ {sp.latex(integral_expression)} \\]"

# Simple HTML content incorporating MathJax for rendering LaTeX
html_content = f"""
<html>
<head>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"></script>
</head>
<body>
    <h1>Integral Result:</h1>
    {latex_code}
</body>
</html>"""

# Print out `os.getcwd()` before writing and opening files to confirm the current working directory.
import os
print("Current Working Directory:", os.getcwd())


# Write html content into an html file.
os.getcwd()
with open("integral_output.html", "w") as file:
    file.write(html_content)

print("HTML file has been created.")
webbrowser.open_new_tab('integral_output.html')  # Open the result in default browser.


