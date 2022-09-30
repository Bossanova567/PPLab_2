from datetime import datetime, timedelta
from staff import Professor, Student
from course import Course, CourseProgress

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
#create two student
student2 = Student(full_name='test_student2',
                   address='test2', phone_number='test2',
                   email='test2@test.test', student_number=2,
                   average_mark=3)
student = Student(full_name='test_student',
                  address='test', phone_number='test',
                  email='test@test.test', student_number=1,
                  average_mark=4)
#create course
course = Course(title='test course', start_date=datetime.now(),
                end_date=datetime.now() + timedelta(minutes=600),
                description="desc test", lectures=[],
                assignments=assignments, limit=1)
#create professor
professor = Professor(name='test_professor', address='test', phone_number='test', email='test@test.test', salary=1000.0)
#create course progress
course_progress = CourseProgress(title='test course', completed_assignments=assignments, course=course)

#add the first student to the course
course.add_student(student=student)
#try to add the second one, though the limit is one student
student2.enroll(course)
#check the assignments
professor.check_assignment(assignments)
#get progress to date (now)
print(course_progress.get_progress_to_date(datetime.now()))
#get a final mark for the course
print(course_progress.get_final_mark())
#fill a note and print it
course_progress.fill_notes("note")
print(course_progress.notes)
#delete a note and try to print it
course_progress.remove_note(datetime.now())
print(course_progress.notes)
#unenroll student
course.remove_student(student.id_)
#try to unenroll him again
course.remove_student(student.id_)
