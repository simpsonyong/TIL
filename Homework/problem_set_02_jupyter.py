# 1. 이상한 덧셈
# 숫자로 구성된 리스트에서 양의 정수의 합을 구하는 함수, 
# positive_sum 을 만들어 보아요

# 예시)

# positive_sum([1, -10, 2]) # 3
# positive_sum([-1, -2, -3, -4]) # 0

# def positive_sum(x):
#     import json
#     lst = json.loads(x)
#     result = sum([i for i in lst if i > 0])
#     return result
# print(positive_sum(input()))

# 2. 문자열 탐색
# 문자열 요소로만 이루어진 리스트를 넣었을 때, 
# 문자열의 길이가 2 이상이고 주어진 문자열의 첫 번째와 
# 마지막 문자가 같은 문자열의 수를 세는 함수 start_end 
# 를 작성하세요

# 예시)

# keywords = ['level', 'asdwe', 's', 'abadsfa', 'q1q']
# start_end(keywords) # 3

# def start_end(x):
#     a = [i for i in x if i[0] == i[-1] and len(i) > 1]
#     return len(a)
# keywords = ['level', 'asdwe', 's', 'abadsfa', 'q1q']
# print(start_end(keywords))

# 3. Collatz
# Collatz 추측: 어떤 자연수 n 이던지, 다음과 같은 작업을 반복하면 1로 만들수 있다.

# n이 짝수라면 2로 나눈다.
# n이 홀수라면 3을 곱하고 1을 더한다.
# 결과로 나온 수에 1 / 2 의 작업을 1이 될때까지 반복한다.
# 예를 들어 n 이 6이면, 6 => 3 => 10 => 5 => 16 => 8 => 4 => 2 => 1 이 되며 
# 8번(=> 갯수!)만에 1이 됩니다. 자연수 n이 들어왔을 때, 몇 번의 작업만에 1이 되는 지를
# return 하는 함수 collatz() 를 완성하세요
# 단! 500 번을 넘어가도 1이 되지 않는다면, -1을 return 할게요!
# 예시)
# collatz(6) # 8
# collatz(16) # 4
# collatz(626331) # -1

def collatz(x, count=0):
    if x == 1:
        return count
    elif count > 500:
        return -1

    else:
        if x % 2 == 0:
            x /= 2
        else:
            x = x*3 + 1
        count += 1
    return collatz(x, count)
print(collatz(int(input())))
