#while문

#True
#False - 0, '', None, [] ...
# n을 입력하여 해당 수 만큼 반복하는 반복문을 작성
#n = int(input('숫자를 입력하십시오 >>> '))

#while n:
#    print("아아아아")
#    n -= 1

#li = []

#while True:
#    n = int(input('정수입력 : '))
#    if not n: break
#    li.append(n)

#print(li)

#1~100 사이의 모든 정수 중에서 7의 배수만 출력하는 프로그램을 구현

#n = 0
#while n <= 100:
#    n += 1
#    if n % 7 == 0:
#        print(n)

#1부터 100사이의 모든 정수를 한줄에 10개씩 출력하는 프로그램을 구현하세요.
n = 1
while n <= 100:
    print(n, end='\t' if n % 10 != 0 else '\n')
    n += 1
# 개신기해
