import unittest
from datetime import datetime, timedelta

from course import Seminar, CourseProgress, Math, Enrollment
from staff import Student


class TestCourse(unittest.TestCase):

    # class Math tests (test would be the same for any other concrete courses)

    def test_add_student(self):
        course = Math(title='test course', start_date=datetime.now(),
                      end_date=datetime.now() + timedelta(minutes=600),
                      description="desc test", lectures=[],
                      assignments=[], limit=1)
        student = Student(1, "student1_name", "address1", "phone_number1", "email1", "position1", "rank1", 50,
                          student_number=2,
                          average_mark=3)
        course.add_student(student)
        self.assertEqual(student.courses, [course])
        self.assertEqual(course.students, [student])

    def test_remove_student(self):
        course = Math(title='test course', start_date=datetime.now(),
                      end_date=datetime.now() + timedelta(minutes=600),
                      description="desc test", lectures=[],
                      assignments=[], limit=1)
        student = Student(1, "student1_name", "address1", "phone_number1", "email1", "position1", "rank1", 50,
                          student_number=2,
                          average_mark=3)
        course.add_student(student)
        course.remove_student(student)
        self.assertEqual(student.courses, [])
        self.assertEqual(course.students, [])

    # class Seminar tests

    def test_implement_item(self):
        seminar = Seminar("title", datetime.now(), assignments=[{}], status=0, related_course="course")
        result = seminar.implement_item("item")
        self.assertEqual(result, "The item is implemented.")

    def test_add_comment(self):
        seminar = Seminar("title", datetime.now(), assignments=[{}], status=0, related_course="course")
        result = seminar.add_comment("comment")
        self.assertEqual(result, "The comment comment is added.")

    # class Enrollment tests

    def test_enroll(self):
        course = Math(title='test course', start_date=datetime.now(),
                      end_date=datetime.now() + timedelta(minutes=600),
                      description="desc test", lectures=[],
                      assignments=[], limit=1)
        student = Student(1, "student1_name", "address1", "phone_number1", "email1", "position1", "rank1", 50,
                          student_number=2,
                          average_mark=3)
        enrollment = Enrollment(student, course)
        enrollment.enroll()
        self.assertEqual(student.courses, [course])
        self.assertEqual(course.students, [student])

    def test_unenroll(self):
        course = Math(title='test course', start_date=datetime.now(),
                      end_date=datetime.now() + timedelta(minutes=600),
                      description="desc test", lectures=[],
                      assignments=[], limit=1)
        student = Student(1, "student1_name", "address1", "phone_number1", "email1", "position1", "rank1", 50,
                          student_number=2,
                          average_mark=3)
        enrollment = Enrollment(student, course)
        enrollment.enroll()
        enrollment.unenroll(student.personal_info.id_)
        self.assertEqual(student.courses, [])
        self.assertEqual(course.students, [])

        # class CourseProgress tests

        def test_fill_notes(self):
            course = Math(title='test course', start_date=datetime.now(),
                          end_date=datetime.now() + timedelta(minutes=600),
                          description="desc test", lectures=[],
                          assignments=[], limit=1)
            course_progress = CourseProgress("title", [], course)
            course_progress.fill_notes("note")
            self.assertEqual(course_progress.notes[datetime.now()], "note")

        def test_remove_note(self):
            course = Math(title='test course', start_date=datetime.now(),
                          end_date=datetime.now() + timedelta(minutes=600),
                          description="desc test", lectures=[],
                          assignments=[], limit=1)
            course_progress = CourseProgress("title", [], course)
            course_progress.fill_notes("note")
            course_progress.remove_note(datetime.now())
            self.assertEqual(course_progress.notes, {})