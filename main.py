class Student:
    """
    Class defines students.
    Class has function for rating lecturers.
    Uses own print.
    Class objects can be compared between each other.
    """
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        check = False
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.student_grades:
                lecturer.student_grades[course] += [grade]
            else:
                lecturer.student_grades[course] = [grade]
            check = True
        return 'Grade is added' if check else 'Error of adding grade'

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
    """
    Class defines mentors.
    Class is a parent for others and has only init method.
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """
    Class defines lecturers.
    Child class from class Mentor.
    Purpose of class is additional function of getting rate from students.
    Uses own print.
    Class objects can be compared between each other.
    """
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
    """
    Class defines reviewers.
    Child class from class Mentor.
    Purpose of class is additional function of rating student.
    Uses own print
    """
    def rate_student(self, student, course, grade):
        check = False
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
                check = True
        return 'Grade is added' if check else 'Error of adding grade'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avg_student_mark_on_course(student_list, course):
    """
    Calculate avg mark on course and student's list

    Input:
    :param student_list:
    :param course:
    Output:
    :return students avg mark on course or message 'No marks':
    """
    marks_sum = 0
    marks_count = 0
    for student in student_list:
        for lecture, marks in student.grades.items():
            if lecture == course:
                marks_sum += sum(marks)
                marks_count += len(marks)
    return round(marks_sum/marks_count, 2) if marks_count != 0 else 'Оценок нет'


def avg_lecturer_mark_on_course(lecturer_list, course):
    """
    Calculate avg mark on course and lecturer's list

    Input:
    :param lecturer_list:
    :param course:
    Output:
    :return lecturers avg mark on course or message 'No marks':
    """
    marks_sum = 0
    marks_count = 0
    for lecturer in lecturer_list:
        for lecture, marks in lecturer.student_grades.items():
            if lecture == course:
                marks_sum += sum(marks)
                marks_count += len(marks)
    return round(marks_sum/marks_count, 2) if marks_count != 0 else 'Оценок нет'


# Creating students
best_student = Student('Peter', 'Parker', 'male')
best_student.courses_in_progress += ['Journalism']
best_student.finished_courses += ['Photography']
bad_student = Student("Mary Jane", "Watson", 'female')
bad_student.finished_courses += ['Journalism']
bad_student.courses_in_progress += ['Photography']

# Creating reviewers
bad_reviewer = Reviewer('J. Jonah', 'Jameson')
bad_reviewer.courses_attached += ['Journalism']
cool_reviewer = Reviewer('Eddie', 'Brock')
cool_reviewer.courses_attached += ['Photography']

# Creating lecturers
bad_lecturer = Lecturer('Norman', 'Osborn')
bad_lecturer.courses_attached += ['Journalism']
cool_lecturer = Lecturer('Harry', 'Osborn')
cool_lecturer.courses_attached += ['Photography']

# Filling students grades (with checking that program fill only courses in progress)
cool_reviewer.rate_student(best_student, 'Journalism', 10)
cool_reviewer.rate_student(bad_student, 'Journalism', 8)
bad_reviewer.rate_student(best_student, 'Journalism', 6)
bad_reviewer.rate_student(bad_student, 'Journalism', 1)
cool_reviewer.rate_student(best_student, 'Photography', 7)
cool_reviewer.rate_student(bad_student, 'Photography', 9)
bad_reviewer.rate_student(best_student, 'Photography', 2)
bad_reviewer.rate_student(bad_student, 'Photography', 4)

# Filling lecturers grades (with checking that program fill only attached courses)
best_student.rate_lecturer(cool_lecturer, 'Journalism', 9)
best_student.rate_lecturer(bad_lecturer, 'Journalism', 5)
best_student.rate_lecturer(cool_lecturer, 'Journalism', 8)
best_student.rate_lecturer(bad_lecturer, 'Journalism', 4)
bad_student.rate_lecturer(cool_lecturer, 'Photography', 6)
bad_student.rate_lecturer(bad_lecturer, 'Photography', 2)
bad_student.rate_lecturer(cool_lecturer, 'Photography', 5)
bad_student.rate_lecturer(bad_lecturer, 'Photography', 1)

# Checking correct __str__ printing
print('Students, lecturers and reviewers:')
print(best_student, '\n')
print(bad_student, '\n')
print(cool_lecturer, '\n')
print(bad_lecturer, '\n')
print(cool_reviewer, '\n')
print(bad_reviewer, '\n')

# Checking students and lecturers compares operations
print('Check compares:')
print('Students compare: ', best_student > bad_student, best_student < bad_student, best_student >= bad_student,
      best_student <= bad_student, best_student == bad_student)
print('Lecturers compare: ', cool_lecturer > bad_lecturer, cool_lecturer < bad_lecturer, cool_lecturer >= bad_lecturer,
      cool_lecturer <= bad_lecturer, cool_lecturer == bad_lecturer)
print()

# Print lectures courses with grades
print('Lecturer grades:')
print(cool_lecturer.name, cool_lecturer.surname, ': ', cool_lecturer.student_grades)
print(bad_lecturer.name, bad_lecturer.surname, ': ', bad_lecturer.student_grades)
print()

# Checking nonclass functions calculating avg marks of students and lecturers
print('Use additional nonclass functions:')
print("Student's AVG mark on Photography:", avg_student_mark_on_course([best_student, bad_student], 'Photography'))
print("Lecturer's AVG mark on Journalism:", avg_lecturer_mark_on_course([cool_lecturer, bad_lecturer], 'Journalism'))
