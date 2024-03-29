# distancesFromHere
특정 장소로부터 특정 장소까지를 거리를 계산해줌
----

# 프로젝트 소개
특정 장소로부터 여러 장소까지의 직선 가리가 필요할 때 사용할 수 있는 프로그램입니다.

## 거리를 구한 방법

1. [geopy](https://geopy.readthedocs.io/en/stable/) 라이브러리를 이용하여, 각 주소를 (위도, 경도)의 데이터로 변환한다.
2. 마찬가지로 기준 위치의 (위도, 경도)도 구합니다.
3. 두 지점 간의 직선거리를 구하기 위해, 하버사인 공식([Haversine Formula](https://en.wikipedia.org/wiki/Haversine_formula))를 이용해서 거리를 구함. 

---

## why not use map api

1. 지도 api를 사용하지 않아도, 위도와 경도만으로 각 지점과 서울역 간의 직선거리를 구할 수 있음.
2. 거리 외에 걸리는 시간을 구하는 것은 각 지도의 핵심 알고리즘이기에 api로는 어려움

---

### Reference

[주소를 위도 경도로 바꾸기](https://wonhwa1.blogspot.com/2022/10/python-geopy.html)

[위도 경도로 거리 구하기(하버사인)](https://gaussian37.github.io/python-etc-%EC%9C%84%EB%8F%84,%EA%B2%BD%EB%8F%84-%EA%B0%84-%EA%B1%B0%EB%A6%AC/)
