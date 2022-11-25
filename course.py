from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Any
import itertools


class Seminar:
    """Represent Seminar instance.

        Attributes:
            title (str): Seminar's title.
            deadline (datetime): Date, before which tasks must be done.
            assignments (List[dict]): Tasks, which must be done.
            status (Any): Seminar's status.
            related_course (str): Title of a course, seminar belongs to.
    """

    def __init__(self, title: str, deadline: datetime, assignments: List[dict],
                 status: Any, related_course: str):
        """Seminar initializer"""
        self.title = title
        self.deadline = deadline
        self.assignments = assignments
        self.status = status
        self.related_course = related_course

    def implement_item(self, item_name: str) -> str:
        """Implements an item.

            Args:
                item_name (str): Item, which should be implemented.

            Returns:
                The message, that particular item was implemented.
        """
        return f"The {item_name} is implemented."

    def add_comment(self, str: str):
        """Adds a comment.

                Args:
                    str (str): Commentary, which should be added.

                Returns:
                    None.
                """
        print(f"The comment {str} is added.")
        return f"The comment {str} is added."


class Course(ABC):
    @abstractmethod
    def add_student(self, student: Any) -> None:
        """ Abstract method """
        pass

    @abstractmethod
    def remove_student(self, student: Any) -> None:
        """ Abstract method """
        pass



class CourseProgress:
    """CourseProgress representation.

        Attributes:
            title (str): Course's name.
            received_marks (dict): Dictionary of the marks, student has received.
            visited_lectures (int): Number of lectures, student has visited.
            completed_assignments (dict): Assignments, student has completed (or not).
            notes (dict): Notes about CourseProgress

        """

    def __init__(self, title: str, completed_assignments: dict, course: Course) -> None:
        """CourseProgress initializer."""
        self.title = title
        self.received_marks = {}
        self.visited_lectures = 0
        self.completed_assignments = completed_assignments
        self.notes = {}
        self.course = course

    def get_progress_to_date(self, date: datetime) -> str:
        """Returns a grade before date in arguments.

                Arguments:
                    date (datetime): should be in default format.

                Returns:
                    The relation between the sum of grades and their quantity.

                """
        grades = 0.0
        i = 0.0
        for task_date, task in self.completed_assignments.items():
            if self.course.start_date <= date:
                grades += task["mark"]
                i += 1.0
        if i == 0.0:
            i = 1.0
        return grades / i

    def get_final_mark(self) -> float:
        """Returns a final grade.

                Arguments:
                    None.

                Returns:
                    The relation between the sum of grades and their quantity.

                    """
        final_mark = 0.0
        i = 0.0
        for mark, task in self.completed_assignments.items():
            final_mark += task["mark"]
            i += 1.0
        final_mark /= i
        return final_mark

    def fill_notes(self, note: str) -> None:
        """Leave a note about course.

               Args:
                   note (str): Note that is attached

               Returns:
                   None.

               """
        self.notes[datetime.now()] = note

    def remove_note(self, date: datetime) -> None:
        """Delete a note about course for the date.

               Args:
                    date (str): Date of the note, which should be deleted

               Returns:
                    None.

                       """
        del self.notes[date]


class Enrollment:
    def __init__(self, student: Any, course: Course):
        self.student = student
        self.course = course

    def enroll(self) -> None:
        """Enrolls a student in a course

            Args:
                student (Student): Student, who needs to be enrolled.

            Returns:
                None.

        """
        try:
            for i in self.student.courses:
                if i.title == self.course.title:
                    raise ValueError("The student has already enrolled in this course")
            if len(self.course.students) < self.course.limit:
                course_progress = CourseProgress(title=self.course.title, completed_assignments=self.course.assignments,
                                                 course=self.course)
                self.student.courses.append(self.course)
                self.student.course_progress.append(course_progress)
                self.course.students.append(self.student)
                print(f"Student {self.student.personal_info.name} has enrolled into {self.course.title}")
            else:
                print(
                    f"Student {self.student.personal_info.name} can't enroll in this course, because the limit of "
                    f"students has been reached")
        except ValueError:
            print(f"Student {self.student.personal_info.name} has already enrolled in this course")

    def unenroll(self, id: int) -> None:
        """Unenrolls a student from a course

            Args:
                id (int): Id of a student, who needs to be unenrolled.

            Returns:
                 None.

        """
        for i, student in enumerate(self.course.students):
            if student.personal_info.id_ == id:
                self.course.students.pop(i)
                for j in self.student.courses:
                    if j.title == self.course.title:
                        # student.unenroll(title=self.course.title)
                        self.student.courses.pop(i)
                        print(f"Student {self.student.personal_info.name} has unenrolled from {self.course.title}")
                        break
                break


class Math(Course):
    """Math course representation.

        Attributes:
            title (str): Course's name.
            start_date (datetime): Start date.
            end_date (datetime): End date.
            description (str): Course's description.
            lectures (List[str]): Course's lectures.
            assignments (List[str]): Course's assignments.
            limit (int): Course's limit for the number of students.
            students (List[Any]): Course's list for enrolled students.
            control_works_date (datetime): Date of the control works.

        """

    def __init__(self, title: str, start_date: datetime, end_date: datetime, description: str,
                 lectures: List[str], assignments: List[str], limit: int):
        """Math course initializer."""
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assignments = assignments
        self.limit = limit
        self.students: List[Any] = []
        self.seminars: List[int] = []
        self.control_works_date = None

    def add_student(self, student: Any) -> None:
        """Enrolls a student into a course

            Arguments:
                student (Student): Student, which should be enrolled

            Returns:
                None
                """
        self.enrollment = Enrollment(student, self)
        self.enrollment.enroll()

    def remove_student(self, student: Any) -> None:
        """Unenrolls a student from a course

            Arguments:
                student (Student): Student, which should be unenrolled

            Returns:
                  None
        """
        self.enrollment = Enrollment(student, self)
        self.enrollment.unenroll(student.personal_info.id_)

class Programming(Course):
    """Programming course representation.

        Attributes:
            title (str): Course's name.
            start_date (datetime): Start date.
            end_date (datetime): End date.
            description (str): Course's description.
            lectures (List[str]): Course's lectures.
            assignments (List[str]): Course's assignments.
            limit (int): Course's limit for the number of students.
            students (List[Any]): Course's list for enrolled students.
            extra_tasks (List[dict]): Extra tasks for students, who want higher marks.

        """

    def __init__(self, title: str, start_date: datetime, end_date: datetime, description: str,
                 lectures: List[str], assignments: List[str], limit: int):
        """Programming course initializer."""
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assignments = assignments
        self.limit = limit
        self.students: List[Any] = []
        self.seminars: List[int] = []
        self.extra_tasks = {}

    def add_student(self, student: Any) -> None:
        """Enrolls a student into a course

            Arguments:
                student (Student): Student, which should be enrolled

            Returns:
                None
                """
        self.enrollment = Enrollment(student, self)
        self.enrollment.enroll()

    def remove_student(self, student: Any) -> None:
        """Unenrolls a student from a course

            Arguments:
                student (Student): Student, which should be unenrolled

            Returns:
                  None
        """
        self.enrollment = Enrollment(student, self)
        self.enrollment.unenroll(student.personal_info.id_)

class Algorithms(Course):
    """Algorithms course representation.

        Attributes:
            title (str): Course's name.
            start_date (datetime): Start date.
            end_date (datetime): End date.
            description (str): Course's description.
            lectures (List[str]): Course's lectures.
            assignments (List[str]): Course's assignments.
            limit (int): Course's limit for the number of students.
            students (List[Any]): Course's list for enrolled students.
            errors (int): Number of errors, which were found in your assignments.

        """

    def __init__(self, title: str, start_date: datetime, end_date: datetime, description: str,
                 lectures: List[str], assignments: List[str], limit: int):
        """Algorithms course initializer."""
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assignments = assignments
        self.limit = limit
        self.students: List[Any] = []
        self.seminars: List[int] = []
        self.errors = 0

    def add_student(self, student: Any) -> None:
        """Enrolls a student into a course

            Arguments:
                student (Student): Student, which should be enrolled

            Returns:
                None
                """
        self.enrollment = Enrollment(student, self)
        self.enrollment.enroll()

    def remove_student(self, student: Any) -> None:
        """Unenrolls a student from a course

            Arguments:
                student (Student): Student, which should be unenrolled

            Returns:
                  None
        """
        self.enrollment = Enrollment(student, self)
        self.enrollment.unenroll(student.personal_info.id_)