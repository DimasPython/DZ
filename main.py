class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Имя: {self.first_name} {self.last_name}, Возраст: {self.age}, Пол: {self.gender}")


class Teacher(Person):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.subject = ""

    def display_info(self):
        super().display_info()
        print(f"Преподаваемый предмет: {self.subject}")


class Student(Person):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.level = ""

    def display_info(self):
        super().display_info()
        print(f"Успеваймость: {self.level}")


class Academy:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def display_teachers(self):
        print("Преподаватели:")
        for teacher in self.teachers:
            teacher.display_info()

    def display_students(self):
        print("Студенты:")
        for student in self.students:
            student.display_info()


academy = Academy()

while True:
    print("1. Добавить преподавателя")
    print("2. Добавить студента")
    print("3. Показать преподавателей")
    print("4. Показать студентов")
    print("5. Выход")

    choice = input("Выберите опцию: ")

    if choice == "1":
        first_name = input("Введите имя преподавателя: ")
        last_name = input("Введите фамилию преподавателя: ")
        age = int(input("Введите возраст преподавателя: "))
        gender = input("Введите пол преподавателя: ")
        subject = input("Введите преподаваемый предмет: ")
        teacher = Teacher(first_name, last_name, age, gender)
        teacher.subject = subject
        academy.add_teacher(teacher)
        print("Преподаватель добавлен")

    elif choice == "2":
        first_name = input("Введите имя студента: ")
        last_name = input("Введите фамилию студента: ")
        age = int(input("Введите возраст студента: "))
        gender = input("Введите пол студента: ")
        level = input("Введите уровень студента: ")
        student = Student(first_name, last_name, age, gender)
        student.level = level
        academy.add_student(student)
        print("Студент добавлен.")

    elif choice == "3":
        academy.display_teachers()

    elif choice == "4":
        academy.display_students()

    elif choice == "5":
        print("Выход")
        break

    else:
        print("Неправильный выбор")


