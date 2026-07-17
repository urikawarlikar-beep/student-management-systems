students = {}

def add_student(student_id, name):
    if student_id in students:
        return False
    students[student_id] = name
    return True

def remove_student(student_id):
    if student_id in students:
        del students[student_id]
        return True
    return False

def search_student(student_id):
    if student_id in students:
        return students[student_id]
    return None

def update_student(student_id, name):
    if student_id in students:
        students[student_id] = name
        return True
    return False