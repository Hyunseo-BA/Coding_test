# Q1 : 문자열 바꾸기
# a:b:c:d -> a#b#c#d
# split 과 join 함수 사용하여 문자열 고치기

# data='a:b:c:d'

# a = data.split(sep=":")

# result='#'.join(a)
# print(result)

# Q2 : 딕셔너리 값 추출
# 딕셔너리 a에서 'C'라는 키에 해당하는 밸류를 출력
# a = {'A':90, 'B':80}
# print(a.get('C', 70))

# Q3 : 리스트 더하기
# 리스트 a에 extend 함수를 사용하면 뭐가 다른지?
# a=[1,2,3]
# a.extend([4,5])
# a

# Q4 : 리스트 총합 구하기
# A 학급 학생점수를 나타낸 리스트에서 50점 이상인 점수의 총합

# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# result = 0
# for i in A:
#     if i >= 50:
#         result += i
# print(result)

# Q5 : 피보나치 함수
# 첫번째 항의 값이 0이고, 두번째 항의 값이 1일때, 다음 항은 이전 두항을 더한 값으로 이루어진 수열
# 0, 1, 1, 2, 3, 5, 8, 13 ...
# 입력을 n으로 받았을 때, n 항 이하까지의 피보나치 수열을 출력하는 함수 작성

# n = int(input())

# def fibo_rec(n):
#     if n == 0 : return 0
#     elif n == 1 : return 1
#     else : return fibo_rec(n-2) + fibo_rec(n-1)

# for i in range(n):
#     print(fibo_rec(i), end=' ')

# def fibo_my(n):
#     result = [0, 1]
    
#     for i in range(n-2):
#         n3 = result[i]+ result[i+1]
#         result.append(n3)

#     return result

# print(fibo_my(n))

# Q6. 숫자 총합 구하기
# 사용자로부터 정해진 숫자를 입력받아 그 총합을 구하는 프로그램
# 숫자는 콤마로 구분

# numbers = list(map(int, input().split(sep=',')))

# result = 0
# for i in numbers:
#     result += i

# print(result)

# Q7. 한 줄 구구단
# 구구단을 출력할 숫자를 입력하세요(2~9) : 2
# 2 4 6 ... 18

# n = int(input('구구단을 출력할 숫자를 입력하세요(2~9) : '))
# for i in range(1,10):
#     print(n * i, end=' ')

# Q8. 사칙연산 계산기
class Calculator:
    def __init__(self, number_list):
        self.number_list = number_list

    def add(self):
        result =0
        for i in self.number_list:
            result += i
        return result

    def avg(self):
        result =0
        for i in self.number_list:
            result += i
        return result/len(self.number_list)

cal1 = Calculator([1,2,3,4])
print(cal1.add(), cal1.avg())