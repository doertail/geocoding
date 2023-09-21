# geocoding
230922 서울역과의 특정 장소와의 거리 조사

## Data

보내주신 데이터로 제작,


## why not use map api

1. 지도 api를 사용하지 않아도, 위도와 경도만으로 각 지점과 서울역 간의 직선거리를 구할 수 있음.
2. 거리 외에 걸리는 시간을 구하는 것은 각 지도의 핵심 알고리즘이기에 api로는 어려움


## How to find the distance?

1. [geopy](https://geopy.readthedocs.io/en/stable/) 파이썬 라이브러리를 이용하여, 각 주소를 (위도, 경도)의 데이터로 변환([지오코딩](https://ko.wikipedia.org/wiki/%EC%A7%80%EC%98%A4%EC%BD%94%EB%94%A9))
2. 마찬가지로 서울역의 (위도, 경도)도 구합니다.
3. 두 지점 간의 직선거리를 구하기 위해, 하버사인 공식([Haversine Formula](https://en.wikipedia.org/wiki/Haversine_formula))를 이용해서 거리를 구함. 이 또한 파이썬에 가구현

---

### Note

각 주소가 종종 잘못 입력되어있거나, geopy라이브러리의 함수가 인식하지 못하여 위도와 경도를 구할 때 조금 시간이 걸렸다.


---

### Reference

[주소를 위도 경도로 바꾸기](https://wonhwa1.blogspot.com/2022/10/python-geopy.html)

[위도 경도로 거리 구하기(하버사인)](https://gaussian37.github.io/python-etc-%EC%9C%84%EB%8F%84,%EA%B2%BD%EB%8F%84-%EA%B0%84-%EA%B1%B0%EB%A6%AC/)
