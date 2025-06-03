import subprocess
#subprocess.run('pip3 install re --break-system-packages',shell=True)
subprocess.run('pip3 install sympy --break-system-packages',shell=True)
import re
from sympy import symbols, Eq, solve, sympify

num_equations = int(input("How many equations do you want to enter? "))

equations = []
variables_set = set()

for i in range(num_equations):
    eq = input(f"Enter equation {i+1} (e.g., x**2 + y = 3): ")
    equations.append(eq)
    variables_set.update(re.findall(r'[a-zA-Z_]\w*', eq))

variables = sorted(list(variables_set))
symbols_dict = {var: symbols(var) for var in variables}

sympy_eqs = []
for eq in equations:
    if '=' not in eq:
        print(f"Invalid equation '{eq}' (missing '=').")
        exit()
    left, right = eq.split('=')
    left_expr = sympify(left, locals=symbols_dict)
    right_expr = sympify(right, locals=symbols_dict)
    sympy_eqs.append(Eq(left_expr, right_expr))

solution = solve(sympy_eqs, list(symbols_dict.values()), dict=True)

if not solution:
    print("No solution found.")
else:
    for sol in solution:
        for var in variables:
            print(f"{var} = {sol.get(symbols_dict[var])}")
        print('-' * 20)
