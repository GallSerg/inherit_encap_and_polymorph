class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.student_grades:
                lecturer.student_grades[course] += [grade]
            else:
                lecturer.student_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __gt__(self, other):
        return sum(*self.grades.values()) / len(*self.grades.values()) > \
            sum(*other.grades.values()) / len(*other.grades.values())

    def __ge__(self, other):
        return sum(*self.grades.values()) / len(*self.grades.values()) >= \
            sum(*other.grades.values()) / len(*other.grades.values())

    def __lt__(self, other):
        return sum(*self.grades.values()) / len(*self.grades.values()) < \
            sum(*other.grades.values()) / len(*other.grades.values())

    def __le__(self, other):
        return sum(*self.grades.values()) / len(*self.grades.values()) <= \
            sum(*other.grades.values()) / len(*other.grades.values())

    def __eq__(self, other):
        return sum(*self.grades.values()) / len(*self.grades.values()) == \
            sum(*other.grades.values()) / len(*other.grades.values())

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {sum(*self.grades.values()) / len(*self.grades.values())}
Курсы в процессе изучения: {' ,'.join(self.courses_in_progress)}
Завершенные курсы: {' ,'.join(self.finished_courses)}'''


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.student_grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {sum(*self.student_grades.values()) / len(*self.student_grades.values())}'

    def __gt__(self, other):
        return sum(*self.student_grades.values()) / len(*self.student_grades.values()) > \
            sum(*other.student_grades.values()) / len(*other.student_grades.values())

    def __ge__(self, other):
        return sum(*self.student_grades.values()) / len(*self.student_grades.values()) >= \
            sum(*other.student_grades.values()) / len(*other.student_grades.values())

    def __lt__(self, other):
        return sum(*self.student_grades.values()) / len(*self.student_grades.values()) < \
            sum(*other.student_grades.values()) / len(*other.student_grades.values())

    def __le__(self, other):
        return sum(*self.student_grades.values()) / len(*self.student_grades.values()) <= \
            sum(*other.student_grades.values()) / len(*other.student_grades.values())

    def __eq__(self, other):
        return sum(*self.student_grades.values()) / len(*self.student_grades.values()) == \
            sum(*other.student_grades.values()) / len(*other.student_grades.values())


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avg_student_mark_on_course(student_list, ):
    pass


def avg_lecturer_mark_on_course():
    pass


best_student = Student('Peter', 'Parker', 'male')
best_student.courses_in_progress += ['Journalism']
best_student.finished_courses += ['Photography']
bad_student = Student("Mary Jane", "Watson", 'female')
bad_student.finished_courses += ['Journalism']
bad_student.courses_in_progress += ['Photography']

bad_reviewer = Reviewer('J. Jonah', 'Jameson')
bad_reviewer.courses_attached += ['Journalism']
cool_reviewer = Reviewer('Eddie', 'Brock')
cool_reviewer.courses_attached += ['Photography']

bad_lecturer = Lecturer('Norman', 'Osborn')
bad_lecturer.courses_attached += ['Photography']
cool_lecturer = Lecturer('Harry', 'Osborn')
cool_lecturer.courses_attached += ['Photography']

cool_reviewer.rate_student(best_student, 'Journalism', 10)
cool_reviewer.rate_student(bad_student, 'Journalism', 8)
bad_reviewer.rate_student(best_student, 'Journalism', 6)
bad_reviewer.rate_student(bad_student, 'Journalism', 1)
cool_reviewer.rate_student(best_student, 'Photography', 7)
cool_reviewer.rate_student(bad_student, 'Photography', 9)
bad_reviewer.rate_student(best_student, 'Photography', 2)
bad_reviewer.rate_student(bad_student, 'Photography', 4)

best_student.rate_lecturer(cool_lecturer, 'Journalism', 9)
best_student.rate_lecturer(bad_lecturer, 'Journalism', 5)
best_student.rate_lecturer(cool_lecturer, 'Journalism', 8)
best_student.rate_lecturer(bad_lecturer, 'Journalism', 4)
bad_student.rate_lecturer(cool_lecturer, 'Photography', 6)
bad_student.rate_lecturer(bad_lecturer, 'Photography', 2)
bad_student.rate_lecturer(cool_lecturer, 'Photography', 5)
bad_student.rate_lecturer(bad_lecturer, 'Photography', 1)

print(best_student.__str__(), '\n')
print(bad_student.__str__(), '\n')
print(cool_lecturer.__str__(), '\n')
print(bad_lecturer.__str__(), '\n')
print(cool_reviewer.__str__(), '\n')
print(bad_reviewer.__str__(), '\n')
print(best_student > bad_student, best_student < bad_student, best_student >= bad_student,
      best_student <= bad_student, best_student == bad_student)
print(cool_lecturer > bad_lecturer, cool_lecturer < bad_lecturer, cool_lecturer >= bad_lecturer,
      cool_lecturer <= bad_lecturer, cool_lecturer == bad_lecturer)
