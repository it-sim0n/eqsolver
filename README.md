## 🔢 Python Equation Solver

This is a simple Python script that lets you solve a system of algebraic equations using the SymPy library.

### 📌 Features & Usage

- Automatically installs `sympy` using pip (with `--break-system-packages` for compatibility in restricted environments like Termux).
- Accepts multiple equations from user input.
- Parses equations like `x + y = 5` or `x**2 + y = 3` and solves them symbolically.
- Supports any number of variables and equations.

### ✅ Example

```bash
$ python3 n.py
How many equations do you want to enter? 2
Enter equation 1 (e.g., x**2 + y = 3): x + y = 5
Enter equation 2 (e.g., x**2 + y = 3): x - y = 1
x = 3
y = 2
--------------------
```

### 📦 Requirements

- Python 3.x  
- Internet access (for automatic `sympy` installation)

---

Made with 💻 by SIMON – feel free to fork and modify!
