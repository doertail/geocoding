# -*- coding: utf-8 -*-
# pip install haversine
from haversine import haversine

# pip install geopy
from geopy.geocoders import Nominatim
''' 도로명 주소 위도 경도로 바꾸기'''
geo_local = Nominatim(user_agent='South Korea')

# 주소에 대한 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        return [geo.latitude, geo.longitude]

    except:
        return [0,0]

### 주소 데이터 입력 받기

# 여러 줄의 주소 데이터를 입력합니다.
dataOfAddress = []
print('기준 주소로부터 거리를 구하고싶은 주소를 입력해주세요')
print('그만 입력하려면 -1을 입력해주세요.')
while True:
        data = input()
        if data == '-1':
          break
        candidate = geocoding(data)
        if(candidate[0] == 0 and candidate[1] == 0):
          print('다시 입력해주세요')
          continue
        dataOfAddress.append(candidate)
print('주소 입력 완료!')
## 하버사인으로 기준 위치와의 거리 구하기

print('기준 주소를 입력해주세요!')
while True:
  where = input()
  fromHere = geocoding(where)
  if(fromHere[0] == 0 and fromHere[1] == 0):
    print('도로명 주소로 다시 입력해주세요!')
  else:
    break
print('주소 입력 완료!')
# print(fromHere)

print(f'{where}로부터의 거리 출력:')
for i in dataOfAddress:
    print(haversine(fromHere, i))