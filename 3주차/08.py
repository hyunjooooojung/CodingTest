# H-Index

# 문제 설명

# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 
# 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.


def solution(citations):
    citations.sort(reverse=True)  # 논문 인용 횟수 배열 citations 내림차순 정렬
    
    for i, citation in enumerate(citations): # 
        if i >= citation:
            return i
    return len(citations)

print(solution([3, 0, 6, 1, 5])) # 3



# 다른 사람의 풀이
def solution(citations):
    citations.sort()
    l = len(citations)
    
    for i in range(l):
        if citations[i] >= l-i: # 배열을 순회하며 남은 문서 수 보다 인용횟수가 크거나 같은지 비교한다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            return l-i
    return 0

# if citations[i] >= l-i는 주어진 h번 이상 인용된 논문이 h편 이상이라는 조건을 그대로 풀어쓴 것.
# citations[i]는 i번 논문이 인용된 횟수이고 l-i는 인용된 논문의 개수를 최댓값부터 하나씩 줄여나간 것이다. (최댓값을 찾아야 하므로 가장 큰 값부터 시작)
# 그리고 리스트는 오름차순 정렬된 상태이므로 i번째 이후는 모두 i번째보다 큰 값을 가질 것이다.