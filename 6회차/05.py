# 호텔 방 배정 (https://school.programmers.co.kr/learn/courses/30/lessons/64063)

# 문제 설명

# [본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]
# "스노우타운"에서 호텔을 운영하고 있는 "스카피"는 호텔에 투숙하려는 고객들에게 방을 배정하려 합니다. 
# 호텔에는 방이 총 k개 있으며, 각각의 방은 1번부터 k번까지 번호로 구분하고 있습니다. 처음에는 모든 방이 비어 있으며 "스카피"는 다음과 같은 규칙에 따라 고객에게 방을 배정하려고 합니다.
# 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
# 고객은 투숙하기 원하는 방 번호를 제출합니다.
# 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
# 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
# 예를 들어, 방이 총 10개이고, 고객들이 원하는 방 번호가 순서대로 [1, 3, 4, 1, 3, 1] 일 경우 다음과 같이 방을 배정받게 됩니다.

# 원하는 방 번호 	배정된 방 번호
#     1	          1
#     3	          3
#     4	          4
#     1	          2
#     3	          5
#     1	          6

# 전체 방 개수 k와 고객들이 원하는 방 번호가 순서대로 들어있는 배열 room_number가 매개변수로 주어질 때, 각 고객에게 배정되는 방 번호를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# k는 1 이상 1012 이하인 자연수입니다.
# room_number 배열의 크기는 1 이상 200,000 이하입니다.
# room_number 배열 각 원소들의 값은 1 이상 k 이하인 자연수입니다.
# room_number 배열은 모든 고객이 방을 배정받을 수 있는 경우만 입력으로 주어집니다.
# 예를 들어, k = 5, room_number = [5, 5] 와 같은 경우는 방을 배정받지 못하는 고객이 발생하므로 이런 경우는 입력으로 주어지지 않습니다.

# 해설 참고하기 : https://tech.kakao.com/2020/04/01/2019-internship-test/


import sys
sys.setrecursionlimit(10000000) # 설정해주지 않으면 재귀가 많이 일어나면서 런타임에러 등이 나타날 수 있다.

def findEmptyRoom(number, rooms): # 빈방을 찾는 함수
    if number not in rooms:        
        rooms[number] = number + 1
        return number
    
    empty = findEmptyRoom(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty


def solution(k, room_number):
    answer = []
    rooms = dict() # 몇번 방이 비어있는지 체크하는 딕셔너리

    for number in room_number:
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)
    
    return answer



# 다른 풀이
def solution(k, room_number):
    room_dic = {}
    answer = []
    for i in room_number:
        n = i
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        answer.append(n)
        for j in visit:
            room_dic[j] = n+1
    return answer
