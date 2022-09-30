from datetime import datetime
from typing import List, Any
from staff import Student


class Course:
    """Course representation.

    Attributes:
        title (str): Course's name.
        start_date (datetime): Start date.
        end_date (datetime): End date.
        description (str): Course's description
        lectures (List[str]): Course's lectures
        assignments (List[str]): Course's assignments
        limit (int): Course's limit for the number of students
        students (List[Any]): Course's list for enrolled students

    """

    def __init__(self, title: str, start_date: datetime, end_date: datetime, description: str,
                 lectures: List[str], assignments: List[str], limit: int):
        """Course initializer."""
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assignments = assignments
        self.limit = limit
        self.students: List[Any] = []

    def add_student(self, student: Student) -> None:
        """Enrolls a student in a course

        Args:
            student (Student): Student, who needs to be enrolled.

        Returns:
              None.

        """
        try:
            student.enroll(course=self)
        except ValueError:
            print(f"Student {student.fullname} has already enrolled in this course")
        course_progress = CourseProgress(title=self.title, completed_assignments=self.assignments, course=self)
        if len(self.students) < self.limit:
            student.course_progress.append(course_progress)
            self.students.append(student)
        else:
            print(
                f"Student {student.fullname} can't enroll in this course, because the limit of students has been reached")

    def remove_student(self, id: int) -> None:
        """Unenrolls a student from a course

                Args:
                    id (int): Id of a student, who needs to be unenrolled.

                Returns:
                      None.

                """
        for i, student in enumerate(self.students):
            if student.id_ == id:
                self.students.pop(i)
                student.unenroll(title=self.title)
                break


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
