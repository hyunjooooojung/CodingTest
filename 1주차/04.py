# 자연수 뒤집어 배열로 만들기

# 문제 설명

# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.


# 처음 작성한 코드
def solution(n):
    answer = list(str(n))
    answer.reverse()
    return answer


# 수정한 코드1
def solution(n):
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer


# 수정한 코드2
def solution(n):
    answer = []
    answer_r = reversed(str(n))
    for i in answer_r:
        answer.append(int(i))
    return answer