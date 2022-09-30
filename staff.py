import itertools
from typing import List, Any
from dataclasses import dataclass


class Student:
    """Represents student instance

    Attributes:
        full_name (str): Student's full name.
        address (str): Student's address.
        phone_number (str): Student's number.
        email (str): Student's email.
    """

    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, phone_number: str, email: str,
                 student_number: int, average_mark: int):
        """Student initializer."""
        self.id_ = next(self.id_iter)
        self.fullname = full_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.student_number = student_number
        self.average_mark = average_mark
        self.course_progress: List[Any] = []
        self.courses: List[Any] = []

    def taken_courses(self) -> List[Any]:
        """Return a list of courses, student has enrolled

                Args:
                    None.

                Returns:
                    self.courses: Courses, in which student has enrolled.
                """
        if self.courses:
            return self.courses
        else:
            print("Student has not enrolled in any course yet")

    def enroll(self, course: Any) -> None:
        """Stands for enrolling current student into course

                Args:
                    course (Any): Course to be enrolled.

                Returns:
                    None.
                """
        for i in self.courses:
            if i.title == course.title:
                raise ValueError("The student has already enrolled in this course")
        if len(course.students) < course.limit:
            self.courses.append(course)
            print(f"Student {self.fullname} has enrolled into {course.title}")
        else:
            print(
                f"Student {self.fullname} can't enroll in this course, because the limit of students has been reached")

    def unenroll(self, title: str) -> None:
        """Stands for unenrolling current student into course

                Args:
                    title (str): Title of a course to be unenrolled.

                Returns:
                    None.
                """
        for i, course in enumerate(self.courses):
            if course.title == title:
                self.courses.pop(i)
                print(f"Student {self.fullname} has unenrolled from {course.title}")
                break


class Professor:
    """Represents professor instance

    Attributes:
        name (str): Professor's name.
        address (str): Professor's address.
        phone_number (str): Professor's phone number.
        email (str): Professor's email.
        salary (float): Professor's salary.

    """

    id_iter = itertools.count()

    def __init__(self, name: str, address: str, phone_number: str,
                 email: str, salary: float):
        """Professor initializer."""
        self.id_ = next(self.id_iter)
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.assignment = {}

    @staticmethod
    def check_assignment(assignment: dict) -> None:
        """Сhecking the assignments

                Args:
                    assignment (dict): The task to be checked

                Returns:
                    None.
                """
        for mark, task in assignment.items():
            if task["is_done"]:
                task["mark"] = 5.0

@dataclass
class PersonalInfo:

    id_iter = itertools.count()

    def __init__(self, full_name_: str, address: str,
                 phone_number: str, email: str, position: int, rank: str, salary: float):
        self.id_ = next(self.id_iter)
        self.first_name, self.last_name = full_name_.split()
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary
        self.full_name = full_name_
    '''
    @property
    def full_name(self):
        return self._full_name
        '''
'''
    @full_name.setter
    def full_name(self, value: str) -> None:
        first_name, last_name = value.split()
        self.first_name = first_name
        self.last_name = last_name
        self._full_name = value
'''
