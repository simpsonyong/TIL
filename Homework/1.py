# class Student:
#     def Callme(self, name):
#         self.name = name
#         print(f'이름: {self.name}')


# class GraduateStudent(Student):
#     def __init__(self, name, major):
#         self.name = name
#         self.major = major
#         print(f'이름: {self.name}, 전공: {self.major}')

# Ha = Student()
# Ha.Callme('홍길동')
# Ha = GraduateStudent('이순신', '컴퓨터')

# class Circle:
#     def calculation(self, radius):
#         self.radius = radius
#         self.area = round((radius**2)*(3.14), 2)
#         print(f'원의 면적: {self.area}')

# obj = Circle()
# obj.calculation(int(2))

# class Rectangle:
#     def calculation(self, width, height):
#         self.width = width
#         self.height = height
#         self.area = width * height
#         print(f'사각형의 면적: {self.area}')

# obj = Rectangle()
# obj.calculation(2, 10)

# class Shape:
#     def area(self, length):
#         self.length = length
#         self.area = length * length
#         return print(f'정사각형의 면적: {self.area}')


# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

# a = Square(3)
# a.area(3)

class Person:
    def getGender(self):
        return 'Unknown'


class Male(Person):
    def getGender(self):
            super().getGender()
            return 'Male'


class Female(Person):
        def getGender(self):
            super().getGender()
            return 'Female'
a = Male()
b = Female()
print(a.getGender())
print(b.getGender())
