import sympy as sp
import os
import webbrowser

# Define symbols and expressions
x = sp.symbols('x')
expression = sp.sin(x**2) + sp.cos(x)

# Create unevaluated Integral object
integral_expr = sp.Integral(expression, (x, 0, sp.pi))

# Convert it into LaTeX code
latex_output = sp.latex(integral_expr)
modified_latex_code = r"\Huge " + latex_output
print("LaTeX Representation:")
print(latex_output)
print("LaTeX Modified:")
print(modified_latex_code)

# Prepare full path for HTML file saving (ensure directory access)
directory_path = os.getcwd() # Gets current working directory where python script runs.
html_file_path = f"{directory_path}/math_display.html"

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Math Expression Display</title>
    <!-- Load MathJax -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<h1>Displaying Calculus Integration:</h1>

<!-- Embedding Latex Code Directly -->
<p>\\({modified_latex_code}\\)</p>

</body>
</html>
"""

# Print out `os.getcwd()` before writing and opening files to confirm the current working directory.
import os
print("Current Working Directory:", os.getcwd())

# Save the HTML content into a local file
with open(html_file_path, "w") as html_file:
    html_file.write(html_content)

# Using 'file://' schema to make sure browsers allow opening of local files directly if needed.
web_browser_url = 'file://' + html_file_path.replace('\\', '/')
print("Opening browser at:", web_browser_url)
webbrowser.open_new_tab(web_browser_url)
