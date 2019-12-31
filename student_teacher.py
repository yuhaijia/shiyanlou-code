#! /usr/bin/env python3

import sys
import collections

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        return 0

class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        common = collections.Counter(self.grade).most_common(4)
        n1 = 0
        n2 = 0
        for item in common:
            if item[0] != 'D':
                n1 += item[1]
            else:
                n2 += item[1]
        return "Pass: {}, Fail: {}".format(n1, n2)

        #Seconde method by using if语句
        #passnum = 0
        #failnum = 0
        #for i in self.grade:
        #    if i == 'A' or i == 'B' or i == 'C':
        #        passnum += 1
        #    elif i == 'D':
        #        failnum += 1
        #return "Pass: {}, Fail: {}".format(passnum, failnum)

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        l = []
        common = collections.Counter(self.grade).most_common(4)
        for i, j in common:
            l.append("{}: {}".format(i, j))
        return ', '.join(l)

person1 = Person('Sachin')
if sys.argv[1] == 'teacher':
    teacher1 = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
    print(teacher1.get_grade())
elif sys.argv[1] == 'student':
    student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
    print(student1.get_grade())
