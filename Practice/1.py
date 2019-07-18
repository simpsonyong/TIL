# 연습1
# class Animal:
#     name = '고양이'

#     def sound(self):
#         print('냐아아옹')

# cat = Animal()

# print(cat.name)
# cat.sound()

# 연습2
# class Student:
#     name = '황재호'
#     kor = input()
#     eng = 90
#     math = 100

#     def getSum(self):
#         sum = self.kor + self.eng + self.math
#         return sum

# hwang = Student()

# print('1')
# print('이름 : %s' % hwang.name)
# print('국어 : %d' % hwang.kor)
# print('영어 : %d' % hwang.eng)
# print('수학 : %d' % hwang.math)
# print('합계 : %d' % hwang.getSum())
# print('평균 : %.1f' % (hwang.getSum()/3))

# 연습3
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print('%s님 반갑습니다!' % self.name)

# person1 = Person('황예린')

# 연습4
# class Member:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def showMember(self):
#         print('이름: %s' % self.name)
#         print('나이: %d' % self.age)

# mem1 = Member('황재호', 30)
# mem1.showMember()

# 문제풀이1
# class Student:
#     b = list(map(int, input().split(', ')))
#     kor = b[0]
#     eng = b[1]
#     math = b[2]

#     def Sum(self):
#         sum = self.kor + self.eng + self.math
#         sum1 = print(f'국어, 영어, 수학의 총점: {sum}')
#         return sum1

# a = Student()
# a.Sum()

# 문제풀이2
# class Korean:
#     country = '대한민국'

#     def printNationality(self):
#         country = self.country
#         print(f'{country}\n{country}')
# a = Korean()
# a.printNationality()

