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
#n = 1
#while n <= 100:
#    print(n, end='\t' if n % 10 != 0 else '\n')
#    n += 1
# 개신기해

#for문

#for j in range (1,10):
#    for i in range(2,10):
#        print(f"{i} * {j} = {i * j}",end='\t')
#    print()

#for 변수 in 반복가능객체:

#0~99

#range(n)    -> 0~(n-1)까지 범위
#range(n,s)  -> n~(s-1)까지 범위
#range(n,s,k)-> n~(s-1)까지 범위 [k씩 증가]
#for _ in range(5):
#    print("hello")

#di = {
#    'a' : 'k',
#    'b' : 'j',
#    'c' : 'c'
#}

#for c in di:
#    print(di[c])
#얘도 신기하다

#li = [i*j for i in range(100) for j in range(50)]

#print(li)

#n = int(input('정수 입력 : '))

#li = [i for i in range(1, n+1)]

#print(sum(li))

exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]

#100점을 받은 학생을 제외 하고 나머지 학생들의 점수를 5점씩 추가 시켜 준다.
#추가시킨 점수는 score 라는 리스트에 저장하고 해당 점수가 100점이 넘지 않도록 프로그래밍

score = [100 if i > 95 else i +5 for i in exam]

print(score)