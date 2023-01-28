#map(실행시킬 명령, 반복가능 객체)

#n1, n2 = map(int, input('숫자 두 개 입력하세요 >>> ').split())

#print(n1, n2)

#if 1:
#    print("helloworld")

#True  : 이외 모든 숫자
#False : 0이나 ''비어있음 을 나타내는 값

age = int(input("나이를 입력하세요 >>> "))

if age >= 20:
    print("성인")
elif age >= 17:
    print("고등학생")
elif age >= 14:
    print("중학생")
else:
    print("어린이")