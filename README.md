# Programming-Fundamental

This repository contains example programs, lecture notes, and lab exercises for an introductory Programming Fundamentals course (Python).

**Repository summary**
- **Total files analyzed:** 23 (primarily Python scripts and one text file). One media file (`recording.mp4`) is present in `All Lectures/Programs` and was not analyzed in-text.
- **Primary topics:** basic I/O, arithmetic, control flow (if/else), loops (for/while), functions, modules, simple calculations, and small lab problems.

**Quick structure**
- `first.py`: Collection of short examples demonstrating variables, constants, arithmetic, and printing.
- `test.py`: Small program computing cylinder area and volume using user input.
- `All Labs/`:
  - `lab_01.py` ... `lab_04.py`: Lab exercises (commented examples and small programs exploring control flow and basic I/O).
- `All Lectures/`:
  - `lect_01.py` ... `lect_14.py`: Lecture example scripts covering topics such as loops, functions, file I/O, math operations, and exercises.
  - `first.txt`: Example text file used by some scripts.
  - `Programs/`:
    - `calculator.py`: Interactive calculator program (multiple operation choices).
    - `santinal_loop_three_programs.py`: Examples of loops and small interactive utilities.
    - `recording.mp4`: Video recording (binary file — not included in textual analysis).

**Key observations from analysis**
- Many files are interactive and expect user input via `input()` or `eval(input())`.
- `eval()` is used widely (e.g., `eval(input(...))` and `map(eval, input().split())`). This is unsafe for untrusted input — consider replacing with `int()`, `float()`, or parsing functions.
- Some scripts use newer Python syntax (e.g., `int | float` union types in annotations), which requires Python 3.10+.
- The codebase is a set of independent example scripts; there is no central test harness or packaging.

**How to run**
1. Ensure you have Python 3.10 or newer installed.
2. Open PowerShell in the repository root (where `README.md` is located).
3. To check Python version:
```
python --version
```
4. Run a script (examples):
```
python first.py
python test.py
python "All Lectures\Programs\calculator.py"
python "All Lectures\lect_07.py"
```
Notes:
- Many scripts prompt for input. Provide the requested values as shown in prompts.
- When running from PowerShell, use quoted paths for files in subfolders with spaces.

**Recommendations / Next steps**
- Replace all uses of `eval(input(...))` with safe parsing (for integers: `int(input(...))`, floats: `float(input(...))`, or use `ast.literal_eval` when needed).
- Add a `requirements.txt` only if external packages are needed (current code uses standard library).
- Add simple unit tests for pure functions (e.g., arithmetic functions) using `pytest` or `unittest`.
- Optionally format code with `black` and add type hints gradually.
- Create small CLI wrappers for interactive programs so they can accept command-line args for automated testing.

**Example: secure replacement for `eval(input())`**
```
# Instead of this:
# x = eval(input("Enter a number:"))

# Use:
try:
    x = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input — please enter an integer.")
```

If you want, I can:
- Add unit tests for a chosen file or function.
- Replace `eval(input(...))` occurrences with safe parsing across the repository.
- Add a `pyproject.toml` + `black` configuration and format files.

---
Generated on repository analysis (Nov 23, 2025). If you want a different README style (short README, badges, or contributing section), tell me which format you prefer and I will update it.
