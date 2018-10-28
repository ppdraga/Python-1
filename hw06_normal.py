# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person():
    def __init__(self, name, surname, middle_name):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
    def representation(self):
        return self.surname + ' ' + self.name[0].upper() + '. ' + self.middle_name[0].upper() + '.'
    def full_representation(self):
        return self.surname + ' ' + self.name + ' ' + self.middle_name

class Pupil(Person):
    def __init__(self, name, surname, middle_name, mother, father):
        Person.__init__(self, name, surname, middle_name)
        self.mother = mother
        self.father = father
    def get_parents(self):
        return [self.father.full_representation(), self.mother.full_representation()]

class SchoolClass:
    def __init__(self, name, pupil_lst, teachersAndSubjects):
        self.name = name
        self.pupil_lst = pupil_lst
        self.teachersAndSubjects = teachersAndSubjects

class School():
    def __init__(self, name, class_lst):
        self.name = name
        self.class_lst = class_lst
    def get_class_lst(self):
        lst = []
        for _ in self.class_lst:
            lst.append(_.name)
        return lst
    def get_pupils(self, class_name):
        lst = []
        for itm in self.class_lst:
            if itm.name == class_name:
                for elem in itm.pupil_lst:
                    lst.append(elem.representation())
                break
        return lst
    def get_parents(self, name_, surname_, middle_name_):
        for class_ in self.class_lst:
            for pupil_ in class_.pupil_lst:
                    if pupil_.name == name_ and pupil_.surname == surname_ and pupil_.middle_name == middle_name_:
                        return pupil_.get_parents()
        return False
    def get_subjects(self, name_, surname_, middle_name_):
        lst = []
        for class_ in self.class_lst:
            for pupil_ in class_.pupil_lst:
                    if pupil_.name == name_ and pupil_.surname == surname_ and pupil_.middle_name == middle_name_:
                        for value in class_.teachersAndSubjects.items():
                            lst.append(value[1])
                        return lst
        return False
    def get_teachers(self, class_name):
        lst = []
        for class_ in self.class_lst:
            if class_.name == class_name:
                for value in class_.teachersAndSubjects.items():
                    lst.append(value[0].full_representation())
                return lst
        return False
        

school1 = School('School # 1', [
    SchoolClass('5a', [
        Pupil('Ivan', 'Inanov', 'Ivanovich', Person('Irina', 'Ivanova', 'Andreevna'), Person('Ivan','Ivanov','Alexandrovich')),
        Pupil('Peter', 'Potapov', 'Ivanovich', Person('Elena', 'Potapova', 'Alexandrovna'), Person('Ivan','Potapov','Petrovich')),
        Pupil('Vasiliy', 'Petrov', 'Ivanovich', Person('Katerina', 'Petrova', 'Ivanovna'), Person('Ivan','Petrov','Alexandrovich'))],
        {Person('Andrey','Andreev','Andreevich') : 'Geometry',
         Person('Margo','Smirnova','Andreevna') : 'English'}),
     SchoolClass('6a', [
        Pupil('Kiril', 'Kirilov', 'Kirilovich', Person('Karina', 'Kirilova', 'Igorevna'), Person('Kiril','Kirilov','Alexandrovich')),
        Pupil('Vitaliy', 'Stogov', 'Ivanovich', Person('Polina', 'Stogova', 'Petrovna'), Person('Ivan','Stogov','Alexandrovich'))],
        {Person('Andrey','Andreev','Andreevich') : 'Geometry',
         Person('Margo','Smirnova','Andreevna') : 'English'})
                                ]
                )
print(school1.get_class_lst())
print(school1.get_pupils('5a'))
print(school1.get_parents('Vitaliy', 'Stogov', 'Ivanovich'))
print(school1.get_subjects('Vitaliy', 'Stogov', 'Ivanovich'))
print(school1.get_teachers('5a'))
print(Person('Ivanov','Inan','Ivanovich').representation())