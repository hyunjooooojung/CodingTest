# 약수의 개수와 덧셈.

# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다. 
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ left ≤ right ≤ 1,000


def solution(left, right):
    answer = 0
    for i in range(left, right+1): #left 부터 right까지 1씩 늘어나면서 도는 for문
        count = 0                  #약수의 개수를 담는 변수
        for j in range(1, i+1):    #1부터 i까지 늘어나면서 약수 찾음
            if i % j == 0:         #나누어 떨어지면 약수
                count += 1         #약수의 개수 카운트
                
        if count % 2 == 0:         #약수의 개수가 짝수이면
            answer += i            #answer에 더하고
        else:
            answer -= i            #홀수이면 answer에 뺄셈
    return answer