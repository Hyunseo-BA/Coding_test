# 피보나치 함수
# 첫번째 항의 값이 0이고, 두번째 항의 값이 1일때, 다음 항은 이전 두항을 더한 값으로 이루어진 수열
# 0, 1, 1, 2, 3, 5, 8, 13 ...
# 입력을 n으로 받았을 때, n 항 이하까지의 피보나치 수열을 출력하는 함수 작성

n = int(input())

def fibo_rec(n):
    if n == 0 : return 0
    elif n == 1 : return 1
    else : return fibo_rec(n-2) + fibo_rec(n-1)

for i in range(n):
    print(fibo_rec(i), end=' ')

def fibo_my(n):
    result = [0, 1]
    
    for i in range(n-2):
        n3 = result[i]+ result[i+1]
        result.append(n3)

    return result

print(fibo_my(n))