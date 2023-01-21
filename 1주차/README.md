<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Programmers&fontSize=90" />
</div>

## 1. 평균 구하기 ([https://school.programmers.co.kr/learn/courses/30/lessons/12944](https://school.programmers.co.kr/learn/courses/30/lessons/12944))
    1. arr의 합계를 arr의 길이만큼 나누면 평균값.

<br>

## 2. 짝수와 홀수 ([https://school.programmers.co.kr/learn/courses/30/lessons/12937](https://school.programmers.co.kr/learn/courses/30/lessons/12937))
    1. num을 2로 나눴을 때 나머지가 0이면 짝수 "Even",  그렇지 않으면 홀수 "Odd"

<br>

## 3. 자릿수 더하기 ([https://school.programmers.co.kr/learn/courses/30/lessons/12931](https://school.programmers.co.kr/learn/courses/30/lessons/12931))
    1. 자연수 n을 string으로 변환해준 배열 n_list 
    2. n_list의 요소를 돌면서 i를 다시 정수로 변환해서 answer에 추가

<br>

## 4. 자연수 뒤집어 배열로 만들기 ([https://school.programmers.co.kr/learn/courses/30/lessons/12932](https://school.programmers.co.kr/learn/courses/30/lessons/12932))
    1. 처음에는 n을 문자열로 변환해준 후 reverse()만 해주면 된다고 생각했는데 오답이었다.
    2. map 함수를 통해 입력받은 자연수(n)를 배열로 바꿔준 후 각각 다시 정수형으로 변환해서 배열로 저장해야한다.
    3. .reverse()를 통해서 배열의 순서를 뒤집어준다.

<br>


## 5. 숫자 문자열과 영단어 - 2021 카카오 채용연계형 인턴십([https://school.programmers.co.kr/learn/courses/30/lessons/81301](https://school.programmers.co.kr/learn/courses/30/lessons/81301))
    1. 숫자와 영단어를 짝지어서 배열에 담아준다.(num_s)
    2. num_s의 요소를 돌면서 숫자와 영단어를 replace 시켜준다. (숫자는 int형이므로 String타입으로 변환해야함)

<br>

## 6. 체육복 탐욕법(Greedy) ([https://school.programmers.co.kr/learn/courses/30/lessons/42862](https://school.programmers.co.kr/learn/courses/30/lessons/42862)) 
    1. 

<br>

## 7. 비밀지도 - 2018 KAKAO BLIND RECRUITMENT([https://school.programmers.co.kr/learn/courses/30/lessons/17681](https://school.programmers.co.kr/learn/courses/30/lessons/17681)) 
    1. 

<br>

## 8. 약수의개수와덧셈-월간코드챌린지시즌2([https://school.programmers.co.kr/learn/courses/30/lessons/77884](https://school.programmers.co.kr/learn/courses/30/lessons/77884))
    1. left 부터 right까지 1씩 늘어나면서 for문 반복
    2. count: 약수의 개수를 담는 변수
    3. 1부터 i안에서 반복문을 돌며 약수를 찾는다.
    4. i가 j로 나누어 떨어지면 약수이다.
    5. 약수의 개수가 짝수인지 홀수인지 판별

<br>

## 9. 없는숫자더하기-월간코드챌린지시즌3([https://school.programmers.co.kr/learn/courses/30/lessons/86051](https://school.programmers.co.kr/learn/courses/30/lessons/86051))
    1. 어렵다^_^

<br>

## 10. 완주하지 못한 선수 – 해시([https://school.programmers.co.kr/learn/courses/30/lessons/42576](https://school.programmers.co.kr/learn/courses/30/lessons/42576))
    1. 처음에는 participant를 집합으로 바꾼 결과에서 completion을 집합으로 바꾼 결과를 차집합하도록 코드를 작성했는데 동명이인이 고려되지 않아서 답이 아니었다.
    2. Counter라는 라이브러리를 사용해서 동명이인 여부를 찾아내야한다.
      - participant의 Counter를 구한다
      - completion의 Counter를 구한다
      - 둘의 차를 구하면 정답만 남아있는 counter를 반환한다
      - counter의 key값을 반환한다
    3. 해시를 이용하는 방법도 있다.