import sympy as sp
import os
import webbrowser

import sympy as sp
import webbrowser

# Define symbols and expressions
x = sp.symbols('x')
expression = sp.sin(x**2) + sp.cos(x)

# Create unevaluated Integral object
integral_expr = sp.Integral(expression, (x, 0, sp.pi))

''''''
# Define symbols
x = sp.symbols('x')

# Example expression - integral of sin(x^2)
expression = sp.sin(x ** 2)
integral_expression = sp.integrate(expression)
''''''

# Convert integral result into LaTeX string
latex_integral_expression = sp.latex(integral_expression)


html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Math Display</title>
    <!-- MathJax Configuration -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <!-- Custom Styles -->
    <style type="text/css">
        body {{
            margin: 0;
            padding: 0;
            height: 100vh; /* Full viewport height */
            display: flex;
            justify-content: center; /* Center content horizontally */
            align-items: center;     /* Center content vertically */
        }}
        
        .math-container {{
            font-size: 5.5em;           /* Increased size by about 25% from initial value of '2em' */

            /* Move container up by adjusting its position relative to its normal position */
            position:relative;
             top:100px ;                 /* Moves upwards approximately equivalent to around ~3 -4 lines depending on line-height.*/
             transform :translateY(-20px);         /* Adjust this value if more fine-tuning needed.*/
             transform :translateX(-80px);         /* Adjust this value if more fine-tuning needed.*/
            
        }}
        
   </style>

</head>
<body>

<h1>Displaying Calculus Integration:</h1>

<!-- Embedding Latex Code Directly with class for styling -->
<div class=\"math-container\">\\({latex_integral_expression}\\)</div>

</body>
</html>
"""


# Write html content into an html file.
with open("integral_output.html", "w") as file:
    file.write(html_content)

print("HTML file has been created.")
webbrowser.open_new_tab('integral_output.html')  # Open result in default browser.