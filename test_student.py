import sys
import io
import pytest
from student import calculate_grade, main

# -------- Grade S (90-100) --------
def test_grade_S_lower():
    assert calculate_grade(90) == "S"

def test_grade_S_middle():
    assert calculate_grade(95) == "S"

def test_grade_S_upper():
    assert calculate_grade(100) == "S"


# -------- Grade A (80-89) --------
def test_grade_A_lower():
    assert calculate_grade(80) == "A"

def test_grade_A_middle():
    assert calculate_grade(85) == "A"

def test_grade_A_upper():
    assert calculate_grade(89) == "A"


# -------- Grade B (65-79) --------
def test_grade_B_lower():
    assert calculate_grade(65) == "B"

def test_grade_B_middle():
    assert calculate_grade(72) == "B"

def test_grade_B_upper():
    assert calculate_grade(79) == "B"


# -------- Grade C (50-64) --------
def test_grade_C_lower():
    assert calculate_grade(50) == "C"

def test_grade_C_middle():
    assert calculate_grade(57) == "C"

def test_grade_C_upper():
    assert calculate_grade(64) == "C"


# -------- Grade D (40-49) --------
def test_grade_D_lower():
    assert calculate_grade(40) == "D"

def test_grade_D_middle():
    assert calculate_grade(45) == "D"

def test_grade_D_upper():
    assert calculate_grade(49) == "D"


# -------- Grade F (Below 40) --------
def test_grade_F_zero():
    assert calculate_grade(0) == "F"

def test_grade_F_middle():
    assert calculate_grade(25) == "F"

def test_grade_F_upper():
    assert calculate_grade(39) == "F"


# -------- Test main() output --------
def test_main_output(monkeypatch, capsys):
    test_args = [
        "student.py",
        "Chinmayee V Gandhad",
        "ICA",
        "3",
        "85",
        "78",
        "90"
    ]

    monkeypatch.setattr(sys, "argv", test_args)

    main()

    captured = capsys.readouterr()
    output = captured.out

    assert "GRADING CRITERIA" in output
    assert "STUDENT DETAILS" in output
    assert "Name       : Chinmayee V Gandhad" in output
    assert "Department : ICA" in output
    assert "Semester   : 3" in output
    assert "Average    : 84.33" in output
    assert "Grade      : A" in output
