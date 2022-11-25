import unittest
from datetime import datetime, timedelta

from course import Math
from staff import Student, Department, PostgraduateStudent, Professor, MathProfessor


class TestStaff(unittest.TestCase):

    # class Student tests (PostGraduate student has the same methods)

    def test_taken_courses(self):
        course = Math(title='test course', start_date=datetime.now(),
                      end_date=datetime.now() + timedelta(minutes=600),
                      description="desc test", lectures=[],
                      assignments=[], limit=1)
        student = Student(1, "student1_name", "address1", "phone_number1", "email1", "position1", "rank1", 50,
                          student_number=2,
                          average_mark=3)
        course.add_student(student)
        self.assertEqual(student.taken_courses(), [course])
        course.remove_student(student)
        self.assertEqual(student.taken_courses(), None)

    def test_send_request(self):
        student = Student(1, "student1_name", "address1", "phone_number1", "email1", "position1", "rank1", 50,
                          student_number=2,
                          average_mark=3)
        department = Department("title", [student], [], [])
        department2 = Department("title", [], [], [])
        self.assertEqual(student.send_request(department, "r"), True)
        self.assertEqual(department.requests, ["r"])
        self.assertEqual(student.send_request(department2, "r"), False)
        self.assertEqual(department2.requests, [])

    def test_ask_sick_leave(self):
        student = Student(1, "student1_name", "address1", "phone_number1", "email1", "position1", "rank1", 50,
                          student_number=2,
                          average_mark=3)
        department = Department("title", [student], [], [])
        student.ask_sick_leave(department)
        self.assertEqual(department.requests, [f'Student {student.personal_info.name} is ill'])

    # class MathProfessor tests (ProgrammingProfessor and AlgorithmsProfessor have the same methods, except one!)

    def test_add_postgraduate_student(self):
        postgraduate_student = PostgraduateStudent(4, "student3_name", "address2", "phone_number2", "email2", "position2", "rank2",
                                       60, student_number=4, average_mark=4)
        professor = MathProfessor(3, "name_surname", "address2", "phone_number2", "email2", "position2", "rank2", 1000)
        professor.add_postgraduate_student(postgraduate_student)
        self.assertEqual(postgraduate_student.phd_status, "phd")

    def test_check_assignment(self):
        assignments = {
            "task1": {
                'title': 'test1',
                'description': 'testing...',
                'is_done': False,
                'mark': 0.0
            },
            "task2": {
                'title': 'test2',
                'description': 'testing...',
                'is_done': True,
                'mark': 0.0
            },
            "task3": {
                'title': 'test3',
                'description': 'testing...',
                'is_done': True,
                'mark': 0.0
            },
            "task4": {
                'title': 'test4',
                'description': 'testing...',
                'is_done': True,
                'mark': 0.0
            }
        }
        professor = MathProfessor(3, "name_surname", "address2", "phone_number2", "email2", "position2", "rank2", 1000)
        professor.check_assignment(assignments)
        self.assertEqual(assignments.get("task1").get("mark"), 0.0)
        self.assertEqual(assignments.get("task2").get("mark"), 5.0)
        self.assertEqual(assignments.get("task3").get("mark"), 5.0)
        self.assertEqual(assignments.get("task4").get("mark"), 5.0)

    def test_create_course(self):
        professor = MathProfessor(3, "name_surname", "address2", "phone_number2", "email2", "position2", "rank2", 1000)
        math_course = professor.create_course("title", datetime.now(), datetime.now() + timedelta(hours=600), "description",
                                [], [], 1)
        self.assertEqual(isinstance(math_course, Math), True)

    def
