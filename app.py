# # sayilar = [1, 2, 3, 4]
# # toplam = 0
# # for a in sayilar:
# #     toplam += a
# # print(toplam)
# #
#
# class Person():
#     def __init__(self, fname, lname):
#         self.firstName = fname
#         self.lastName = lname
#         print('Person created')
#
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
#         print('Student created')
#
# p1 = Person('Celal','Yurt')
# s1 = Student('Kaan', 'Yurt')
#
#
# class Teacher(Person):
#     def __init__(self, fname, lname, branch):
#         super().__init__(fname, lname)
#         self.branch = branch
# t1 = Teacher('osman', 'mem', 'math')
#
# print(p1.firstName + ' ' +p1.lastName)
# print(s1.firstName + ' ' + s1.lastName)
# print(t1.firstName + ' ' + t1.lastName + '' + t1.branch)

# class Question():
#     def __init__(self,text, choices, answer):
#         self.text = text
#         self.answer = answer
#         self.choices= choices
#
#     def checkAnswer(self, answer):
#         return self.answer == answer
#
# q1 = Question('en iyi programlama dili?', ['java','python'],'python')
#
# print(q1.checkAnswer('python'))

# a = input('a: ')
# b = a.split()
# c = len(b)
# print(c)



