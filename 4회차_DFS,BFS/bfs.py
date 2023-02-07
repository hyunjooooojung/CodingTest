bfsGraph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}


def bfs(bfsGraph, start_node):
    visited = [] # 방문한 노드를 담을 배열
    queue = [] # 방문 예정인 노드를 담을 배열

    queue.append(start_node) # 처음에는 시작 노드 담아주고 시작하기.

    while queue: # 더 이상 방문할 노드가 없을 때까지.
        node = queue.pop(0) # 방문할 노드를 앞에서 부터 하나씩 꺼내기.

        if node not in visited: # 방문한 노드가 아니라면
            visited.append(node) # visited 배열에 추가
            queue.extend(bfsGraph[node]) # 해당 노드의 자식 노드로 추가
    
    print("bfs - ", visited)
    return visited
    
    
# 함수 실행
bfs(bfsGraph, 'G')
# bfs -  ['G', 'D', 'C', 'E', 'B', 'F', 'A', 'H', 'I', 'J', 'M', 'K', 'L']


# deque 사용
from collections import deque

def bfs_queue(bfsGraph, node):
    visited = []
    queue=deque()

    queue.appendleft(node)

    while queue:                                # 큐에 남은것이 없을 때까지 반복
        node = queue.pop()
        if node not in visited:                 # 방문한 노드인지를 확인. 노드가 아닐 경우에만 근접 노드를 Queue에 추가
            visited.append(node)
            print(node, visited, queue)
            queue.extendleft(bfsGraph[node])

    return visited       
    
bfs_queue(bfsGraph, "A")
'''
    A ['A'] deque([])
    B ['A', 'B'] deque([])
    H ['A', 'B', 'H'] deque(['C'])
    C ['A', 'B', 'H', 'C'] deque(['M', 'J', 'I', 'B'])
    I ['A', 'B', 'H', 'C', 'I'] deque(['D', 'B', 'M', 'J'])
    J ['A', 'B', 'H', 'C', 'I', 'J'] deque(['H', 'D', 'B', 'M'])
    M ['A', 'B', 'H', 'C', 'I', 'J', 'M'] deque(['K', 'H', 'H', 'D', 'B'])
    D ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D'] deque(['H', 'K', 'H', 'H'])
    K ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K'] deque(['G', 'E', 'C', 'H'])
    E ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K', 'E'] deque(['L', 'J', 'G'])
    G ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K', 'E', 'G'] deque(['F', 'D', 'L', 'J'])
    L ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K', 'E', 'G', 'L'] deque(['D', 'F', 'D'])
    F ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K', 'E', 'G', 'L', 'F'] deque(['K', 'D'])
'''


# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}



def bfs_queue2(graph, start_node):
    queue = [start_node]
    visited = []

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adjacent_node in graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited



print(bfs_queue2(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!