# 📘 Programming Fundamentals -- Coursework Repository

A collection of lecture examples, lab exercises, and small practice
programmes completed during my University Programming Fundamentals
(Python) course. This repository serves as a proof of study, documenting
the concepts, logic-building tasks, and hands-on coding I covered
throughout the semester.

## 📑 Table of Contents

-   🎯 Purpose of This Repository
-   🗂️ Repository Structure
-   📚 Topics Covered
-   📝 File Overview
-   ▶️ How to Run the Programs
-   ⚠️ Notes & Recommendations
-   📄 Educational Use Notice

## 🎯 Purpose of This Repository

This repository represents my journey through the Programming
Fundamentals course. It includes all major components of the subject
such as:

-   Writing basic Python scripts
-   Understanding variables, data types, and expressions
-   Working with conditional logic and loops
-   Building simple interactive programmes
-   Practicing lecture and lab tasks

## 🗂️ Repository Structure

    Programming-Fundamental/
    │
    ├── first.py                      
    ├── test.py                       
    │
    ├── All Labs/
    │   ├── lab_01.py
    │   ├── lab_02.py
    │   ├── lab_03.py
    │   └── lab_04.py                 
    │
    ├── All Lectures/
    │   ├── lect_01.py ... lect_14.py 
    │   ├── first.txt                 
    │   └── Programs/
    │       ├── calculator.py         
    │       ├── santinal_loop_three_programs.py
    │       └── recording.mp4         
    │
    └── README.md

The repository contains 23 Python files, each demonstrating a specific
concept from the course.

## 📚 Topics Covered

-   Basic Input/Output
-   Arithmetic and expressions
-   If--Else decision making
-   Loops (for, while, sentinel loops)
-   Functions
-   Simple modules
-   File handling
-   Logic building exercises
-   Interactive console programmes

## 📝 File Overview

| File / Folder | Description |
|---|---|
| `first.py` | Intro examples: variables, printing, arithmetic |
| `test.py` | Calculates area & volume of a cylinder using user input |
| `All Labs/lab_01.py` | Basic input/output tasks |
| `All Labs/lab_02.py` | If–else and simple calculations |
| `All Labs/lab_03.py` | Loops and repetitive tasks |
| `All Labs/lab_04.py` | Mixed exercises and logic-building |
| `All Lectures/lect_01.py` → `lect_14.py` | Lecture demonstration scripts covering course topics |
| `All Lectures/first.txt` | Example text file used by some scripts |
| `All Lectures/Programs/calculator.py` | Multi-operation interactive calculator |
| `All Lectures/Programs/santinal_loop_three_programs.py` | Small utilities and loop examples |
| `All Lectures/Programs/recording.mp4` | Video recording (binary file — not analyzed in-text) |


## ▶️ How to Run the Programs

You only need Python 3.10 or newer.

### 1. Check Python Version

    python --version

### 2. Run a Python Script

    python first.py
    python test.py
    python "All Lectures/lect_07.py"
    python "All Lectures/Programs/calculator.py"

## ⚠️ Notes & Recommendations

### Replace eval(input())

    # ❌ Avoid
    value = eval(input("Enter number: "))

    # ✔️ Safe alternative
    value = int(input("Enter number: "))

### Optional improvements

-   Add unit tests\
-   Use black formatter\
-   Add type hints\
-   Support CLI arguments

## 📄 Educational Use Notice

This repository is for educational and demonstration purposes only.
