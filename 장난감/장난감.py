
## ���� (�ڷ���)

## 1.  ������
from stringprep import map_table_b3


a=1000
print(a)

a=-7
print(a) # �� & ���� ���� �����ϰ� �ȴٴ� ��.

a=5 - 2
print(a) #�ٷ� ��굵 �ȴٴ� ��.

b=5%3
print(b) #%�� ������, //�� ���� �ǹ��Ѵ�.

## 1-2 ���ڿ�(�迭)
array=[ 0,3,5]
print(array)

	#if �Լ��� ���� ù ��° ���
array=[i for i in range(20) if i % 2 == 1]
print(array) 

	#if �Լ��� ���� �� ��° ���
array=[]
for i in range(20):
	if i % 2 == 1:
		array.append(i)

print(array)

	#�������� �Ѿ��(1)
n=3
m=4
array=[[0] * m for _ in range(n)]
print(array)


## 2. ���ڿ�

	#Ʃ�� �ڷ���
	#�� �� ����� ���� ������ �� ����.
	#����Ʈ�� ���ȣ�� �̿�������, Ʃ���� �Ұ�ȣ�� �̿��Ѵ�.

a = (1,2,3,4)
print(a) #a[2] = 7 �� ���ڸ� �Է��ϸ� ���� ���峭��. ����

	#���� �ڷ���
	#Dictionary Ű-���� ���� ������ �ֱ�.
	#O(1)�� �ð����� ���� ó���� �� �ִ� ��û�� ����.

Data = dict()
Data['Hansol'] = 'Master'
Data['Dave'] = 'Meber'
Data['John'] = 'Moderator'
print(Data) #Visual Studio������ �ѱ۷� �Է��ϸ� �ȵȴ�.

MemberList = Data.keys()
GradeList = Data.values()

print(MemberList)
print(GradeList)



