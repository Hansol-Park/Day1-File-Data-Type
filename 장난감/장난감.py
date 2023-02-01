
## 시작 (자료형)

## 1.  정수형
from stringprep import map_table_b3


a=1000
print(a)

a=-7
print(a) # 양 & 음의 정수 간단하게 된다는 점.

a=5 - 2
print(a) #바로 계산도 된다는 점.

b=5%3
print(b) #%는 나머지, //는 몫을 의미한다.

## 1-2 문자열(배열)
array=[ 0,3,5]
print(array)

	#if 함수를 쓰는 첫 번째 방식
array=[i for i in range(20) if i % 2 == 1]
print(array) 

	#if 함수를 쓰는 두 번째 방식
array=[]
for i in range(20):
	if i % 2 == 1:
		array.append(i)

print(array)

	#공간으로 넘어가기(1)
n=3
m=4
array=[[0] * m for _ in range(n)]
print(array)


## 2. 문자열

	#튜플 자료형
	#한 번 선언된 값을 변경할 수 없다.
	#리스트는 대괄호를 이용하지만, 튜플은 소괄호를 이용한다.

a = (1,2,3,4)
print(a) #a[2] = 7 등 숫자를 입력하면 값이 고장난다. 유의

	#사전 자료형
	#Dictionary 키-쌍의 값을 가지고 있기.
	#O(1)의 시간으로 값을 처리할 수 있는 엄청난 장점.

Data = dict()
Data['Hansol'] = 'Master'
Data['Dave'] = 'Meber'
Data['John'] = 'Moderator'
print(Data) #Visual Studio에서는 한글로 입력하면 안된다.

MemberList = Data.keys()
GradeList = Data.values()

print(MemberList)
print(GradeList)



