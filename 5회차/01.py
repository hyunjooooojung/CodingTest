# 타겟 넘버(https://school.programmers.co.kr/learn/courses/30/lessons/43165)

# 문제 설명
# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.


def dfs(n, sum, numbers, target):
    global answer
    if n == len(numbers):   # 더이상 탐색할 값이 없을 떄
        if sum == target:   # 합이 target과 같으면 answer +1
            answer += 1
        return answer
    
    # 탐색할 값이 남아있으면 dfs 호출
    dfs(n+1, sum + numbers[n], numbers, target)
    dfs(n+1, sum - numbers[n], numbers, target)
    
def solution(numbers, target):
    global answer
    answer = 0
        
    dfs(0, 0, numbers, target)

    return answer



print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))


