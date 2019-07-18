class Student(object):
    def __init__(self, name, year, class_num, student_id):

        # 파이썬 키워드인 class는 인수이름으로 사용 불가
        self.name = name
        self.year = year
        self.class_num = class_num
        self.student_id = student_id

    def introduce_myself(self):
        return '{}, {}학년 {}반 {}번'.format(
            self.name, self.year, self.class_num,
            self.student_id)

student = Student('아아아', 2, 3, 35)
print(student.introduce_myself())
