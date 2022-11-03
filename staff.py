import itertools
from typing import List, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod


class PersonalInfo:
    """Represents personal info instance

        Attributes:
            address (str): Staff's address.
            phone_number (str): Staff's phone number.
            email (str): Staff's email.
            position (str): Staff's position.
            rank (str): Staff's rank.
            salary (float): Staff's salary.
            name (str): Staff's name.
            id_: Staff's id.
    """
    def __init__(self, address: str, phone_number: str, email: str, position: str, rank: str, salary: float,
    first_name: str, last_name: str, id_: int):
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary
        self.first_name = first_name
        self.last_name = last_name
        self.id_ = id_
        self.name = first_name+last_name





class Staff(ABC, PersonalInfo):
    """Represents staff instance"""

    @abstractmethod
    def ask_sick_leave(self, department: Any):
        """Abstract method"""
        pass

    @abstractmethod
    def send_request(self, department: Any, request: str) -> bool:
        """Abstract method"""
        pass


class Student(Staff):
    """Represents student instance

    Attributes:
        name (str): Student's full name.
        address (str): Student's address.
        phone_number (str): Student's number.
        email (str): Student's email.
        position (str): Student's position.
        rank (str): Student's rank.
        salary (float): Student's scholarship.
        student_number (int): Student's number.
        average_mark (int): Student's average mark
    """

    def __init__(self, id_: int, name: str, address: str, phone_number: str, email: str, position: str, rank: str,
            salary: float,  student_number: int, average_mark: int):
        """Student initializer."""
        self.first_name, self.last_name = name.split("_")
        self.personal_info = PersonalInfo(address, phone_number, email, position, rank, salary, self.first_name, self.last_name, id_)
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

    def send_request(self, department: Any, request: str) -> bool:
        """Sends request to a department. Returns bool value, which is true,
            if operation was successful, and false, if not

            Args:
                department: Department, student belongs to.
                request (str): The request, student wants to send.

            Returns: Bool value, which is true,
                if operation was successful, and false, if not.
        """
        for i, student in enumerate(department.students):
            if student.personal_info.name == self.personal_info.name:
                department.requests.append(request)
                print("The request has been sent successfully.")
                return True
        print(f"The student {self.personal_info.name} does not belong to {department.title} department")
        return False

    def ask_sick_leave(self, department: Any):
        """Sends a request to a department, in which the fact that sender is ill
                    Args:
                        department: Department, sender belongs to.

                    Returns:
                        None
                """
        department.requests.append(f'Student {self.personal_info.name} is ill')
        if department.proceed_requests():
            print(f"Student {self.personal_info.name} is free from studying until he gets over the illness")


class PostgraduateStudent(Staff):
    """Represents postgraduate student instance

        Attributes:
            name_ (str): Student's full name.
            address (str): Student's address.
            phone_number (str): Student's number.
            email (str): Student's email.
            position (str): Student's position.
            rank (str): Student's rank.
            salary (float): Student's scholarship.
            student_number (int): Student's number.
            average_mark (int): Student's average mark
        """

    def __init__(self,id_: int, name: str, address: str, phone_number: str, email: str, position: str, rank: str,
            salary: float, student_number: int, average_mark: int):
        """Postgraduate student initializer."""
        self.first_name, self.last_name = name.split("_")
        self.personal_info = PersonalInfo(address, phone_number, email, position, rank, salary, self.first_name,
                                          self.last_name, id_)
        self.phd_status = "not phd yet"
        self.student_number = student_number
        self.average_mark = average_mark
        self.course_progress: List[Any] = []
        self.courses: List[Any] = []

    def send_request(self, department: Any, request: str) -> bool:
        """Sends request to a department. Returns bool value, which is true,
                    if operation was successful, and false, if not

                    Args:
                        department: Department, student belongs to.
                        request (str): The request, student wants to send.

                    Returns: Bool value, which is true,
                    if operation was successful, and false, if not.
                """
        for i, student in enumerate(department.students):
            if student.name_ == self.name_:
                department.requests.append(request)
                print("The request has been sent successfully.")
                return True
        print(f"The postgraduate student {self.name_} does not belong to {department.title} department")
        return False

    def ask_sick_leave(self, department: Any):
        """Sends a request to a department, in which the fact that sender is ill
            Args:
                department: Department, sender belongs to.

            Returns:
                None
        """
        department.requests.append(f'Student {self.personal_info.name} is ill')
        if department.proceed_requests():
            print(f"Student {self.personal_info.name} is free from studying until he gets over the illness")



class Professor(Staff):
    """Represents professor instance

    Attributes:
        name_ (str): Professor's name.
        address (str): Professor's address.
        phone_number (str): Professor's phone number.
        email (str): Professor's email.
        position (str): Professor's position.
        rank (str): Professor's rank.
        salary (float): Professor's salary.

    """

    id_iter = itertools.count()

    def __init__(self, id_: int, name: str, address: str, phone_number: str, email: str, position: str, rank: str,
            salary: float):
        """Professor initializer."""
        self.first_name, self.last_name = name.split("_")
        self.personal_info = PersonalInfo(address, phone_number, email, position, rank, salary, self.first_name,
                                          self.last_name, id_)
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

    def send_request(self, department: Any, request) -> bool:
        """Sends request to a department. Returns bool value, which is true,
                    if operation was successful, and false, if not

                    Args:
                        department: Department, professor belongs to.
                        request (str): The request, professor wants to send.

                    Returns: Bool value, which is true,
                    if operation was successful, and false, if not.
                """
        for i, professor in enumerate(department.professors):
            if professor.personal_info.name == self.personal_info.name:
                department.requests.append(request)
                print("The request has been sent successfully.")
                return True
        print(f"The professor {self.personal_info.name} does not belong to {department.title} department")
        return False

    def ask_sick_leave(self, department: Any):
        """Sends a request to a department, in which the fact that sender is ill
                    Args:
                        department: Department, sender belongs to.

                    Returns:
                        None
                """
        department.requests.append(f'Professor {self.personal_info.name} is ill')
        if department.proceed_requests():
            print(f"Professor {self.personal_info.name} is free from teaching until he gets over the illness")

    def add_postgraduate_student(self, student: PostgraduateStudent) -> PostgraduateStudent:
        """Makes a postgraduate student

            Args:
                student (PostgraduateStudent): student, which should be Postgraduate.

            Returns:
                PostgraduateStudent
        """
        if isinstance(student, PostgraduateStudent):
            if student.phd_status == "not phd yet":
                student.phd_status = "phd"
                print(f"Student {student.personal_info.name} now has phd")
            else:
                print(f"Student {student.personal_info.name} already has phd")
        else:
            print(f"{student.personal_info.name} is not postgraduate student")
        return student

    def request_support(self) -> None:
        """Requests a support for a professor

            Args:
                None.

            Returns:
                None.
        """
        print(f"Professor {self.personal_info.name} has requested support")


class Department:
    """Represents department instance

        Attributes:
            title (str): Department's title.
            students (List[Student]): List of students, that belong to the department.
            professors (List[Professor]): List of professors, that belong to the department.
            courses (List[str]): List of courses, that belong to the department.
            requests (List[str]): List of requests, that has been sent to the department.
    """
    def __init__(self, title: str, students: List[Student], professors: List[Professor],
                 courses: List[str]):
        """Department initializer"""
        self.title = title
        self.students = students
        self.professors = professors
        self.courses = courses
        self.requests = requests = []

    def proceed_requests(self) -> Any:
        """Proceeds requests, which has been to the department

            Args:
                None.

            Returns:
                Bool value.
        """
        return True




