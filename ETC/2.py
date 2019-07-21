
# 리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
# 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# 입력
# 입력없음
# ex_012_input.txt
# 출력
# Pythn s pwrfl... nd fst; plys wll wth thrs; rns vrywhr; s frndly & sy t lrn; s Opn.

#   a = [1, 2, 3, 4]
#   result = []
#   for num in a:
#       result.append(num * 3)
#   print(result)
#   ​
#   result = [num * 3 for num in a]
#   print(result)
#   ​
#   result = [num * 3 for num in a if num % 2 == 0]
#   print(result)
#   ​
#   # 연습문제 풀이
#   print("[문제5] 리스트 내포1")
#   """
#   리스트 중에서 홀수에만 2를 곱하여 저장하는 다음과 같은 코드가 있다.
#   numbers = [1, 2, 3, 4, 5]
#   result = []
#   for n in numbers:
#       if n % 2 == 1:
#           result.append(n*2)
#   위 코드를 리스트 내포로 표현하시오.
#   """
#   numbers = [1, 2, 3, 4, 5]
#   result = [num * 2 for num in numbers if num % 2 == 1]
#   print(result)
#   ​
#   print("[문제6] 리스트 내포2")
#   """
#   리스트 내포를 이용하여 다음 문장에서 모음('aeiou')을 제거하시오.
#   Life is too short, you need python
#   """
#   moeum = "aeiou"
#   sentence = "Life is too short, you need python"
#   result = [char for char in sentence if char not in moeum]
#   print(''.join(result))

string = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
moeum = 'aeiou'
result = [char for char in string if char not in moeum]
print(''.join(result))
