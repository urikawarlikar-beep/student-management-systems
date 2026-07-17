import pytest
from student import *

def setup_function():
    students.clear()

def test_add_student():
    assert add_student(1, "Rahul") == True

def test_add_duplicate():
    add_student(1, "Rahul")
    assert add_student(1, "Amit") == False

def test_search_student():
    add_student(1, "Rahul")
    assert search_student(1) == "Rahul"

def test_search_not_found():
    assert search_student(10) is None

def test_remove_student():
    add_student(1, "Rahul")
    assert remove_student(1) == True

def test_remove_not_found():
    assert remove_student(10) == False

def test_update_student():
    add_student(1, "Rahul")
    assert update_student(1, "Rohan") == True

def test_update_not_found():
    assert update_student(5, "Raj") == False

def test_after_update():
    add_student(1, "Rahul")
    update_student(1, "Rohan")
    assert search_student(1) == "Rohan"

def test_after_remove():
    add_student(1, "Rahul")
    remove_student(1)
    assert search_student(1) is None