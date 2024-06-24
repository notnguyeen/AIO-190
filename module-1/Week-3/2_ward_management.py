from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):  # student will add Grade

        super().__init__(name=name, yob=yob)
        self.__grade = grade

    def describe(self):
        print(
            f" Student - Name: {self._name} | YoB: {self._yob} | Grade: {self.__grade}"
        )


class Doctor(Person):
    def __init__(self, name, yob, specialist):  # student will add Grade

        super().__init__(name=name, yob=yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f" Doctor - Name: {self._name} | YoB: {self._yob} | Specialist: {self.__specialist}"
        )


class Teacher(Person):
    def __init__(self, name, yob, subject):  # student will add Grade

        super().__init__(name=name, yob=yob)
        self.__subject = subject

    def describe(self):
        print(
            f" Teacher - Name: {self._name} | YoB: {self._yob} | Subject: {self.__subject}"
        )


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = list()

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                counter += 1
        return counter

    def sort_yob(self):
        return self.__list_people.sort(key=lambda x: x.get_yob())

    def compute_average(self):
        counter = 0
        total_year = 0
        for p in self.__list_people:
            if isinstance(p, Teacher):
                counter += 1
                total_year += p.get_yob()
        return total_year / counter


Nguyen = Student("Nguyen", 1998, 10)
Phat = Doctor("Phat", 1999, "Crazy")
Hieu = Teacher("Hieu", 1998, "Math")


w1 = Ward("Ward 1")
w1.add_person(Nguyen)
w1.add_person(Phat)
w1.add_person(Hieu)
w1.describe()

# w1.count_doctor()
w1.sort_yob()
w1.describe()
# w1.compute_average()
print(f"\nAverage year of birth (teachers): {w1.compute_average()}")


# student1 = Student(name=" studentZ2023 ", yob=2011, grade="6")
# assert student1._yob == 2011
# student1.describe()

# teacher1 = Teacher(name=" teacherZ2023 ", yob=1991, subject=" History ")
# assert teacher1._yob == 1991
# teacher1.describe()

# doctor1 = Doctor(name=" doctorZ2023 ", yob=1981, specialist=" Endocrinologists ")
# assert doctor1._yob == 1981
# doctor1.describe()


ward1 = Ward("Ward 1")

student1 = Student(name=" studentA ", yob=2010, grade="7")
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")

# assert ward1.count_doctor() == 1

doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.count_doctor()
