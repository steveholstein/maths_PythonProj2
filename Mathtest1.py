


import sympy as sp
from IPython.display import display, Math
import webbrowser

# Define symbols and expressions
x = sp.symbols('x')
expression = sp.sin(x**2)

# Calculate the indefinite integral (do not evaluate it)
unevaluated_integral = sp.Integral(expression, x)

# Evaluate the integral expression explicitly
evaluated_integral = unevaluated_integral.doit()

# Convert both expressions to LaTeX formatted strings
latex_unevaluated = sp.latex(unevaluated_integral)
latex_evaluated = sp.latex(evaluated_integral)

# Construct an HTML content with MathJax for rendering LaTeX
html_content = f"""
<html>
<head>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"></script>
</head>
<body>
    <h1>Integral of sin(x^2) dx:</h1>
    <p>Unevalulated Integral: \\({latex_unevaluated}\\)</p> 
    <p>Evalutated Integral: \\({latex_evaluated}\\)</p>  
</body>
</html>"""

# Write html content into an html file.
with open("integral_output.html", "w") as file:
    file.write(html_content)

print("HTML file has been created.")
webbrowser.open_new_tab('integral_output.html')  # Open the result in default browser.