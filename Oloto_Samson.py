# -*- coding: utf-8 -*-


#create person class
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_number}"
    
#create student class
class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_number}, Major: {self.major}"


#create instructor class
class Instructor(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_number}, Department: {self.department}"

#create course class
class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
        else:
            print(f"Student {student.name} is already enrolled in {self.course_name}.")

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
        else:
            print(f"Student {student.name} is not enrolled in {self.course_name}.")

    def __str__(self):
        return f"Course: {self.course_name}, ID: {self.course_id}, Enrolled Students: {[student.name for student in self.enrolled_students]}"


#create enrollment class
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

    def assign_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f"Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade}"

#create StudentManagementClass
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.instructors = {}
        self.courses = {}
        self.enrollments = []

    def add_student(self, student):
        self.students[student.id_number] = student

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        else:
            print(f"No student found with ID: {student_id}")

    def update_student(self, student_id, name=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if major:
                student.major = major
        else:
            print(f"No student found with ID: {student_id}")

    def add_instructor(self, instructor):
        self.instructors[instructor.id_number] = instructor

    def remove_instructor(self, instructor_id):
        if instructor_id in self.instructors:
            del self.instructors[instructor_id]
        else:
            print(f"No instructor found with ID: {instructor_id}")

    def update_instructor(self, instructor_id, name=None, department=None):
        if instructor_id in self.instructors:
            instructor = self.instructors[instructor_id]
            if name:
                instructor.name = name
            if department:
                instructor.department = department
        else:
            print(f"No instructor found with ID: {instructor_id}")

    def add_course(self, course):
        self.courses[course.course_id] = course

    def remove_course(self, course_id):
        if course_id in self.courses:
            del self.courses[course_id]
        else:
            print(f"No course found with ID: {course_id}")

    def update_course(self, course_id, course_name=None):
        if course_id in self.courses:
            course = self.courses[course_id]
            if course_name:
                course.course_name = course_name
        else:
            print(f"No course found with ID: {course_id}")

    def enroll_student_in_course(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            course.add_student(student)
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)
        else:
            print(f"Student or course not found. Student ID: {student_id}, Course ID: {course_id}")

    def assign_grade(self, student_id, course_id, grade):
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student_id and enrollment.course.course_id == course_id:
                enrollment.assign_grade(grade)
                break

    def get_students_in_course(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            return course.enrolled_students
        else:
            print(f"No course found with ID: {course_id}")
            return []

    def get_courses_for_student(self, student_id):
        courses = []
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student_id:
                courses.append(enrollment.course)
        return courses
