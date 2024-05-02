"""

1. Prints  "symbolic maths notation" to the screen to the screen, in this example an Integration formula
2. Uses HTML code to print to the screen through a web browser
3. Uses a LaTex type formula to represent the symbolic maths notation. This formula is also printed in he output consul
    and can be cut and copied as needed, for example to an MS MS Word equation
4.Includes example of parameters to alter size, font , placement etc of both the mathematical formula and the descriptive header
54. Includes code to solve the mathematical equation provided






"""



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

"""
# Example expression - integral of sin(x^2) ---this example is evaluated but not used here 
expression = sp.sin(x ** 2)
integral_expression = sp.integrate(expression)
"""

# Convert integral result into LaTeX string
latex_integral_expression = sp.latex(integral_expr)


# prepare to screen print using HTML code
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
             transform :translateX(-380px);         /* Adjust this value if more fine-tuning needed.*/
            
        }}
        h1 {{
            font-size: 5.5em;
            color: #333;
            text-align: center;
            position:relative;
            top:-200px ;
            transform :translateY(-20px);
            transform :translateX(380px);
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

# Print LaTex formula to consul.
print("LaTeX Representation:")
print(latex_integral_expression)


# Write html content into an html file.
with open("integral_output.html", "w") as file:
    file.write(html_content)

# Open result in default browser.
print("HTML file has been created.")
webbrowser.open_new_tab('integral_output.html')