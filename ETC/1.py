# 이 때 첫 번째 학생은 (90, 80), 두 번째 학생은 (85, 75), 세 번째 학생은 (90, 100)의 점수를
#  갖습니다.
 

# 다음과 같이 결과를 만들기 위한 프로그램을 작성하십시오.
# 1번 학생의 총점은 170점이고, 평균은 85.0입니다.

# 2번 학생의 총점은 160점이고, 평균은 80.0입니다.

# 3번 학생의 총점은 190점이고, 평균은 95.0입니다.


lst_student = [(90, 80), (85, 75), (90, 100)]

def score(x):
    count = 1
    for i in x:
        total = 0
        total += sum(i)
        average = total / 2
        print('{0}번 학생의 총점은 {1}점이고, 평균은 {2:.1f}입니다.'.format(count, total, average))
        count += 1

score(lst_student)
