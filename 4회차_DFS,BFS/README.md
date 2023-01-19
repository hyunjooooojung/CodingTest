## 1. DFS (Depth-First Search)
- '깊이우선탐색(DFS)'은 가장 깊은 노드까지 내려간 뒤, 더 이상 깊이 갈 곳이 없을 경우 옆으로 이동하여 탐색을 합니다.
- root 노드(혹은 다른 임의의 노드)에서 시작하여 다른 branch로 넘어가기 전에 해당 branch를 전부 탐색하는 방식을 말합니다.

 
### 🤔 어떨 때 사용하는가?
주로 모든 노드를 방문하고자 하는 경우에 사용됩니다.

- 미로 찾기
- 그래프의 위상 정렬
- 모든 경우 다 해보기(전체 탐색)
- 연결 구성 요소 찾기
- 이분 그래프


### 🤔 어떻게 구현?
stack 또는 재귀함수를 사용하여 구현합니다.


### 🔍 예제코드 풀이
1. 시작 정점을 먼저 stack[0]에 넣어줍니다.
2. 그리고 스택에서 가장 위(top)에 있는 원소를 하나 꺼냅니다.
3. 그 원소를 방문표시(visited)하고, 그 원소와 인접한 정점들 중에서 방문하지 않은 정점들을 모두 스택에 넣습니다.
4. 방문의 우선순위에 따라 인접한 정점이 여러 개면 번호(알파벳이)가 작은 순서대로 방문해야 하므로, 순서에 맞게 스택에 넣어줍니다.
5. 계속해서 스택의 가장 위에 있는 원소를 꺼내 방문표시하고, 해당 원소와 인접한 원소 중 방문하지 않은 원소들을 모두 스택에 넣어주는 과정을 반복합니다.


<br>


## 2. BFS (Breath-First Search)
- '너비우선탐색(BFS)'는 root노드에서 인접한 노드를 먼저 탐색하는 방법입니다.
- 시작 정점으로부터 가장 가까운 정점을 먼저 방문하고, 멀리 떨어져 있는 정점은 나중에 방문하는 식으로 탐색하는 방식을 말합니다.

 
### 🤔 어떨 때 사용하는가?
주로 최단 경로 문제에서 사용됩니다.

- 두 정점 u,v 간의 최단 경로 찾기( 경로의 길이는 간선의 수에 따라 정해질 때)
- 문자열 알고리즘 Aho-Corasick 패턴 매칭(순위다중패턴매칭)의 실패함수를 구축할 때
- 그래프에서 정점들이 두 개의 독립적인 서로소 그룹으로 나누어질 수 있는가에 대해 이분성 테스트를 할 때
- copying garbage collection
- cheney's algorithm


### 🤔 어떻게 구현?
queue를 사용하여 구현합니다.


### 🔍 예제코드 풀이
1. 시작 정점을 먼저 queue[0]에 추가해 줍니다.
2. queue에서 제일 앞에 있는 원소를 하나 꺼냅니다.(pop)
3. 그 원소를 방문표시(visited)하고, 그 원소와 인접한 정점들 중 방문완료되지 않았고, queue에 추가되지 않은 인접한 원소들을 queue에 추가해줍니다.
4. queue가 빌 때까지 반복합니다.


<br>


참고자료 : https://nareunhagae.tistory.com/17

<br>


## 3. 프로그래머스 완전탐색 문제풀이

1. 최소직사각형([https://school.programmers.co.kr/learn/courses/30/lessons/86491](https://school.programmers.co.kr/learn/courses/30/lessons/86491))
2. 모의고사([https://school.programmers.co.kr/learn/courses/30/lessons/42840](https://school.programmers.co.kr/learn/courses/30/lessons/42840))
3. 소수찾기([https://school.programmers.co.kr/learn/courses/30/lessons/42839](https://school.programmers.co.kr/learn/courses/30/lessons/42839))
4. 카펫 ([https://school.programmers.co.kr/learn/courses/30/lessons/42842](https://school.programmers.co.kr/learn/courses/30/lessons/42842))
5. 피로도([https://school.programmers.co.kr/learn/courses/30/lessons/87946](https://school.programmers.co.kr/learn/courses/30/lessons/87946))
6. 전력망을 둘로 나누기([https://school.programmers.co.kr/learn/courses/30/lessons/86971](https://school.programmers.co.kr/learn/courses/30/lessons/86971))
7. 모음사전([https://school.programmers.co.kr/learn/courses/30/lessons/84512](https://school.programmers.co.kr/learn/courses/30/lessons/84512))
