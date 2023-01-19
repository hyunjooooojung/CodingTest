# 문제 설명

# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.



def solution(brown, yellow):
    total = brown + yellow       # 전체 격자 개수 total
    for i in range(3, brown):    # 가로 or 세로 : i or j / yellow가 1 이상이려면 가로의 길이는 3이상이어야 함.
        if total % i == 0:       # 전체 격자 개수를 i로 나눴을 때 나누어 떨어지면 = 약수이면
            j = total // i       # i * j == total 이니까 j = total // i
            if (i - 2) * (j - 2) == yellow:
                return sorted([i, j], reverse=True)   # 가로 길이가 세로길이보다 같거나 길기 때문에 내림차순 정렬!