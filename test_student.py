import subprocess
import sys

# ---------- UNIT TESTS for calculate_grade ----------

def test_grade_s():
    from student import calculate_grade
    assert calculate_grade(95) == "S"


def test_grade_a():
    from student import calculate_grade
    assert calculate_grade(85) == "A"


def test_grade_b():
    from student import calculate_grade
    assert calculate_grade(70) == "B"


def test_grade_c():
    from student import calculate_grade
    assert calculate_grade(55) == "C"


def test_grade_d():
    from student import calculate_grade
    assert calculate_grade(45) == "D"


def test_grade_f():
    from student import calculate_grade
    assert calculate_grade(30) == "F"


# ---------- INTEGRATION TEST (FULL SCRIPT RUN) ----------

def test_student_program_execution():
    result = subprocess.run(
        [
            sys.executable,
            "student.py",
            "Chinmayee V Gandhad",
            "Integrated MCA",
            "3",
            "89",
            "98",
            "78",
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Chinmayee V Gandhad" in result.stdout
    assert "Integrated MCA" in result.stdout
    assert "Average" in result.stdout
    assert "Grade" in result.stdout
