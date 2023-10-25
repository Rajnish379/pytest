import pytest
from source.school import Classroom, Student, Teacher, TooManyStudents

# Fixtures
@pytest.fixture
def student():
    return Student("Harry Potter")

@pytest.fixture
def teacher():
    return Teacher("Professor McGonagall")

@pytest.fixture
def classroom(teacher):
    students = [Student(f"Student{i}") for i in range(10)]
    return Classroom(teacher, students, "Transfiguration")

# Tests
def test_add_student(classroom, student):
    classroom.add_student(student)
    assert student in classroom.students

def test_remove_student(classroom):
    hermione = Student("Hermione Granger")
    classroom.add_student(hermione)
    classroom.remove_student("Hermione Granger")
    assert hermione not in classroom.students

def test_change_teacher(classroom, teacher):
    new_teacher = Teacher("Professor Snape")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher == new_teacher

def test_too_many_students_exception(classroom, student):
    with pytest.raises(TooManyStudents):
        for _ in range(2):
            classroom.add_student(student)

def test_remove_student_not_found(classroom):
    with pytest.raises(ValueError):
        classroom.remove_student("Luna Lovegood")

# Parameterized Tests
subject_teachers = [
    ("Professor Snape", "Potions"),
    ("Professor Flitwick", "Charms"),
    ("Professor Sprout", "Herbology")
]
@pytest.mark.parametrize("teacher_name, course_title", subject_teachers)
def test_teacher_subject_changes(classroom, teacher_name, course_title):
    classroom.change_teacher(Teacher(teacher_name))
    assert classroom.teacher.name == teacher_name
    classroom.course_title = course_title
    assert classroom.course_title == course_title

# Test for initialization
def test_classroom_initialization():
    teacher = Teacher("Professor Dumbledore")
    students = [Student(f"Student{i}") for i in range(5)]
    classroom = Classroom(teacher, students, "Defense Against the Dark Arts")
    assert classroom.teacher == teacher
    assert classroom.course_title == "Defense Against the Dark Arts"
