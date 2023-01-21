<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Programmers&fontSize=90" />
</div>

## 1. 두 정수 사이의 합 ([https://school.programmers.co.kr/learn/courses/30/lessons/12912**)](https://school.programmers.co.kr/learn/courses/30/lessons/12912)
    1. 입력받은 두 정수 a,b의 크기를 범위를 나눠 비교해서 range()로 반복문.
    2. 반복문을 돌아 나온 i를 answer 변수에 더하기

<br>

## 2. 문자열을 정수로 바꾸기([https://school.programmers.co.kr/learn/courses/30/lessons/12925](https://school.programmers.co.kr/learn/courses/30/lessons/12925))
    1. 정수 n을 string으로 변환 후 내림차순 정렬
    2. 내림차순 정렬된 배열을 join연산

<br>

## 3. 정수 내림차순으로 배치하기([https://school.programmers.co.kr/learn/courses/30/lessons/12933](https://school.programmers.co.kr/learn/courses/30/lessons/12933))
    1. 정수 n을 string으로 변환 후 내림차순 정렬
    2. 내림차순 정렬된 배열을 join연산

<br>

## 4. 나머지가 1이 되는 수 찾기 - 월간 코드 챌린지 시즌3([https://school.programmers.co.kr/learn/courses/30/lessons/87389](https://school.programmers.co.kr/learn/courses/30/lessons/87389))
    1. 2부터 n사이를 range로 반복문을 돌린다.
    2. n을 i로 나눴을 때 나머지가 1인 경우의 i를 반환

<br>

## 5. 음양 더하기 - 월간 코드 챌린지 시즌2([https://school.programmers.co.kr/learn/courses/30/lessons/76501](https://school.programmers.co.kr/learn/courses/30/lessons/76501))
    1. absolutes의 길이만큼 range 반복문.
    2. signs[i]가 참이면 absolutes[i] 의 실제 정수가 양수이므로 absolutes[i]를 answer에 추가
    3. 그렇지 않으면 실제 정수가 음수이므로 absolutes[i]만큼 answer에서 뺄셈

<br>

## 6. 예산 - Summer/Winter Coding(~2018)([https://school.programmers.co.kr/learn/courses/30/lessons/12982](https://school.programmers.co.kr/learn/courses/30/lessons/12982))
    1. answer : 지원할 수 있는 부서의 개수
    2. 부서별로 신청한 금액이 들어있는 배열 d를 정렬
    3. d의 길이만큼 range 반복
    4. 총 예산 budget 보다 d[i]의 금액이 작으면 budget에서 d[i]만큼 뺄셈
    5. 반복문을 돌 때마다 answer은 1씩 증가

<br>

## 7. K번째수 - 정렬([https://school.programmers.co.kr/learn/courses/30/lessons/42748](https://school.programmers.co.kr/learn/courses/30/lessons/42748))
    1. array[i-1:j]만큼 자른 배열을 new_arr에 선언.
    2. new_arr 정렬
    3. new_arr[k-1]인 요소를 answer에 추가
 

<br>

## 8. 같은 숫자는 싫어 - 스택/큐([https://school.programmers.co.kr/learn/courses/30/lessons/12906](https://school.programmers.co.kr/learn/courses/30/lessons/12906))
    1. 원소들을 하나씩 꺼내서 비교하는 방법으로 코드를 짜야 한다!
    2. 결과값을 담을 배열 answer를 만들어준다.
    3. arr의 길이만큼 range반복
    4. i가 0이면 arr[i]를 answer에 추가
    5. arr[i]와 arr[i-1]이 같지 않으면 arr[i]를 answer에 추가

<br>

## 9. 실패율 - 2019 KAKAO BLIND RECRUITMENT([https://school.programmers.co.kr/learn/courses/30/lessons/42889](https://school.programmers.co.kr/learn/courses/30/lessons/42889)) 
    1. 너무 어렵다 ^_^

<br>

## 10. 소수 만들기 - Summer/Winter Coding(~2018)(**[https://school.programmers.co.kr/learn/courses/30/lessons/12977](https://school.programmers.co.kr/learn/courses/30/lessons/12977))
    1. 소수인지 판별하는 is_prime_number 함수 생성
    2. itertools의 combinations 를 활용해야한다!
    3. 3개의 숫자를 조합해서 배열 l에 할당.
    4. l을 돌면서 arr의 합이 소수인지 판별하고 맞으면 answer 1씩 증가

<br>


