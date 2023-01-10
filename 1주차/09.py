# 없는 숫자 더하기

# 문제 설명
# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.

# 내가 작성한 코드

def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer


# 차집합을 이용해 작성한 코드

def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    answer = list(set(num)-set(numbers))
    return sum(answer)


# 다른분이 작성한 코드 - lambda 이용
def solution(numbers):
    answer = sum(list(filter(lambda x:x not in numbers, range(0,10))))

    return answer