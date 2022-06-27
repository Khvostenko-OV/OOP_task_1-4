class Student:
    def __init__(self, name='', surname='', gender=1):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course_name):
        self.courses_in_progress.append(course_name)

    def finish_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
        self.finished_courses.append(course_name)

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (
                course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        c = 0
        g = 0
        for course in self.grades:
            c += len(self.grades[course])
            g += sum(self.grades[course])
        if c > 0:
            return g / c
        else:
            return 0

    def __str__(self):
        c_i_p = ''
        for i in self.courses_in_progress:
            c_i_p += i + ','
        f_c = ''
        for i in self.finished_courses:
            f_c += i + ','
        return 'Имя:' + self.name + '\nФамилия:' + self.surname + '\nСредняя оценка за задания: ' + str(
            self._average_grade()) + '\nКурсы в процессе изучения: ' + c_i_p[:-1] + '\nЗавершенные курсы: ' + f_c[:-1]

    def __lt__(self, other):
      return self._average_grade() < other._average_grade()

    def __eq__(self, other):
      return self._average_grade() == other._average_grade()

class Mentor:

    def __init__(self, name = '', surname = ''):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, n = '', s = ''):
        super().__init__(n, s)
        self.grades = {}

    def _average_grade(self):
        c = 0
        g = 0
        for course in self.grades:
            c += len(self.grades[course])
            g += sum(self.grades[course])
        if c > 0:
            return g / c
        else:
            return 0

    def __str__(self):
        return 'Имя:' + self.name + '\nФамилия:' + self.surname + '\nСредняя оценка за лекции: ' + str(
            self._average_grade())

    def __lt__(self, other):
      return self._average_grade() < other._average_grade()

    def __eq__(self, other):
      return self._average_grade() == other._average_grade()



class Rewiewer(Mentor):

    def rate(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя:' + self.name + '\nФамилия:' + self.surname

def course_average_rate (persons, course):
    rate = 0
    c = 0
    for homo in persons:
        if (isinstance(homo, Student) or isinstance(homo, Lecturer)) and course in homo.grades:
            rate += sum(homo.grades[course])
            c += len(homo.grades[course])
    if c > 0:
        return rate / c
    else:
        return 0

stud1 = Student('Ivan', 'Petrov')
stud2 = Student('Inna', 'Fine', 0)
lect1 = Lecturer('Albert', 'Einstein')
lect2 = Lecturer('Isaac', 'Newton')
rew1 = Rewiewer('First', 'Arbiter')
rew2 = Rewiewer('Second', 'Arbiter')

stud1.add_course('A')
stud1.add_course('B')
stud1.add_course('C')
stud2.add_course('A')
stud2.add_course('B')
stud2.add_course('C')

rew1.courses_attached = ['A', 'B']
rew2.courses_attached = ['B', 'C']
lect1.courses_attached = ['A', 'B']
lect2.courses_attached = ['B', 'C']

rew1.rate(stud1, 'A', 8)
rew1.rate(stud1, 'B', 9)
rew1.rate(stud1, 'C', 10)
rew1.rate(stud2, 'A', 10)
rew1.rate(stud2, 'B', 9)
rew1.rate(stud2, 'C', 10)

rew2.rate(stud1, 'A', 5)
rew2.rate(stud1, 'B', 6)
rew2.rate(stud1, 'C', 7)
rew2.rate(stud2, 'A', 1)
rew2.rate(stud2, 'B', 2)
rew2.rate(stud2, 'C', 3)

stud1.finish_course('A')
stud1.finish_course('B')

stud1.rate(lect1, 'A', 8)
stud1.rate(lect1, 'B', 10)
stud1.rate(lect2, 'B', 7)
stud1.rate(lect2, 'C', 8)

stud2.rate(lect1, 'A', 5)
stud2.rate(lect1, 'B', 4)
stud2.rate(lect2, 'B', 6)
stud2.rate(lect2, 'C', 7)

print(rew1)
print(rew2)

if stud1 > stud2:
    print(stud1)
else:
    print(stud2)

if lect1 > lect2:
    print(lect1)
else:
    print(lect2)

print(course_average_rate([stud1, stud2], 'A'))
print(course_average_rate([stud1, stud2], 'B'))
print(course_average_rate([stud1, stud2], 'C'))

print(course_average_rate([lect1, lect2], 'A'))
print(course_average_rate([lect1, lect2], 'B'))
print(course_average_rate([lect1, lect2], 'C'))

print(stud2)
print(lect1)