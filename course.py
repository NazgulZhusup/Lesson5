# Создайте класс Course с атрибутами name и students, где students - это список студентов, записанных на курс.
# Создайте класс Student с атрибутами name и student_id. Каждый студент может записаться на несколько курсов.
# Реализуйте методы в классе Course для добавления и удаления студентов.
# В классе Student реализуйте метод для вывода всех курсов, на которые записан студент.
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []  # Исправлено на students для ясности

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.add_course(self)  # Добавляем курс в список курсов студента

    def delete_student(self, student):
        if student in self.students:
            self.students.remove(student)
            student.courses.remove(self)  # Удаляем курс из списка курсов студента

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id  # Исправлено: использование правильного имени переменной
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def get_all_courses(self):
        # Исправлено: метод не должен принимать параметры, он выводит курсы
        for course in self.courses:
            print(course.name)

# Пример использования:
course1 = Course("Math")
course2 = Course("Science")
student1 = Student("John Doe", "123")
student2 = Student("Jane Doe", "456")

course1.add_student(student1)
course1.add_student(student2)
course2.add_student(student1)

print(f"Students in {course1.name}: {[student.name for student in course1.students]}")
print(f"Students in {course2.name}: {[student.name for student in course2.students]}")
print(f"Courses for {student1.name}:")
student1.get_all_courses()
