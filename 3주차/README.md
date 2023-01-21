<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Programmers&fontSize=90" />
</div>

## 1. 문자열 내 p와 y의 개수([https://school.programmers.co.kr/learn/courses/30/lessons/12916](https://school.programmers.co.kr/learn/courses/30/lessons/12916))
   1. 문자열의 알파벳을 소문자 or 대문자로 모두 통일 후 문자의 개수 count()

<br>

## 2. 핸드폰 번호 가리기([https://school.programmers.co.kr/learn/courses/30/lessons/12948](https://school.programmers.co.kr/learn/courses/30/lessons/12948))
   1. phone_number에서 끝에 숫자 4개만 뽑아내고 앞에 7자리는 *로 채우기

<br>

## 3. 제일 작은 수 제거하기 ([https://school.programmers.co.kr/learn/courses/30/lessons/12935](https://school.programmers.co.kr/learn/courses/30/lessons/12935))
   1. 배열의 길이가 1일때와 1보다 클 때로 나누기
   2. 배열의 원소 중 최솟값 찾기

<br>

## 4. 콜라츠 추측([https://school.programmers.co.kr/learn/courses/30/lessons/12943](https://school.programmers.co.kr/learn/courses/30/lessons/12943))
   1. 

<br>

## 5. 수박수박수박수박수박수?([https://school.programmers.co.kr/learn/courses/30/lessons/12922](https://school.programmers.co.kr/learn/courses/30/lessons/12922))
   1. n이 짝수인 경우 : n//2 만큼 "수박" 반복
   2. n이 홀수인 경우 : n//2 만큼 "수박" 반복 후 "수" 추가

<br>

## 6. 가운데 글자 가져오기([https://school.programmers.co.kr/learn/courses/30/lessons/12903](https://school.programmers.co.kr/learn/courses/30/lessons/12903))
   1. 문자열 s의 길이가 홀수일 때 : 문자열 s에서 문자열 s의 길이//2 를 인덱스로 갖는 요소 반환
   2. 문자열 s의 길이가 짝수일 때 : 문자열 s에서 (문자열 s의 길이//2 - 1)를 인덱스로 갖는 요소와 문자열 s에서 문자열 s의 길이//2 를 인덱스로 갖는 요소 반환

<br>

## 7. 올바른 괄호 - 스택/큐([https://school.programmers.co.kr/learn/courses/30/lessons/12909](https://school.programmers.co.kr/learn/courses/30/lessons/12909))
   1. "(" 를 저장할 괄호 스택 리스트를 선언.
   2. 문자열 s에 있는 괄호들을 하나씩 반복.
   3. 현재 괄호가 "("라면 stack에 현재괄호를 넣어준다.
   4. 현재 괄호가 ")"라면  

<br>

## 8. H-Index ([https://school.programmers.co.kr/learn/courses/30/lessons/42747](https://school.programmers.co.kr/learn/courses/30/lessons/42747))
   1. if citations[i] >= l-i는 주어진 h번 이상 인용된 논문이 h편 이상이라는 조건을 그대로 풀어쓴 것.
   2. citations[i]는 i번 논문이 인용된 횟수이고 l-i는 인용된 논문의 개수를 최댓값부터 하나씩 줄여나간 것이다. (최댓값을 찾아야 하므로 가장 큰 값부터 시작)
   3. 그리고 리스트는 오름차순 정렬된 상태이므로 i번째 이후는 모두 i번째보다 큰 값을 가질 것이다.

<br>

## 9. 폰켓몬 ([https://school.programmers.co.kr/learn/courses/30/lessons/1845](https://school.programmers.co.kr/learn/courses/30/lessons/1845))
   1. mon = list(set(nums))  : 중복 폰켓몬 제거
   2. i = len(nums) // 2     : 데려갈 수 있는 폰켓몬 수
   3. 중복을 제거한 폰켓몬의 수가 데려갈 수 있는 폰켓몬의 수보다 작으면 len(mon)

<br>

## 10. 다트게임 ([https://school.programmers.co.kr/learn/courses/30/lessons/17682](https://school.programmers.co.kr/learn/courses/30/lessons/17682))
   1. dartResult 문자열 돌기
   2. 숫자(0~10) 있는지 확인(** 10인경우 예외처리!! **)
   3. S, D, T 체크(1제곱, 2제곱, 3제곱)
   4. [옵션]*, # 중 하나 체크