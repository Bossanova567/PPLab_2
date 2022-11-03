from datetime import datetime, timedelta
from staff import Professor, Student, PostgraduateStudent, Department
from course import Course, CourseProgress, Seminar

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
# create two student

student1 = Student(1, "student1_name", "address1", "phone_number1", "email1", "position1", "rank1", 50, student_number=2,
                   average_mark=3)
student2 = Student(1, "student2_name", "address2", "phone_number2", "email2", "position2", "rank2", 60, student_number=4,
                   average_mark=4)
# create course
course = Course(title='test course', start_date=datetime.now(),
                end_date=datetime.now() + timedelta(minutes=600),
                description="desc test", lectures=[],
                assignments=assignments, limit=1)
# create professor
professor = Professor(3, "name_surname", "address2", "phone_number2", "email2", "position2", "rank2", 1000)
# create course progress
course_progress = CourseProgress(title='test course', completed_assignments=assignments, course=course)

student3 = PostgraduateStudent(4, "student3_name", "address2", "phone_number2", "email2", "position2", "rank2", 60,
                               student_number=4, average_mark=4)
department = Department("department", [student1, student3], [professor], [course])
seminar = Seminar("seminar", datetime.now(), assignments, True, course.title)

course.add_student(student1)
course.add_student(student1)
course.add_student(student2)
course.remove_student(student1)

print(student3.phd_status)
professor.add_postgraduate_student(student3)
professor.add_postgraduate_student(student2)
print(student3.phd_status)

student1.ask_sick_leave(department)
student3.ask_sick_leave(department)
professor.ask_sick_leave(department)

professor.send_request(department, "request")
student1.send_request(department, "request")
student2.send_request(department, "request")

professor.request_support()

seminar.add_comment("comment")
print(seminar.implement_item("item"))