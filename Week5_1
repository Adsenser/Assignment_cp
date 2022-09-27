import time
a = int(time.time())

#평년기준 1년
py = 31536000
#윤년기준 1년
yy = 31622400
#윤년이면 y를 1이라고 약속
y = 0

#1단계는 윤년, 평년 판별 후 년수 구하기
for county in range (1,1000000,1):
    if (county-2)%4 == 0 and a >31622400: #윤년이다, 두번째 a 조건을 넣어야 아래 조건문에서 뺄셈을 할 때 음수가 나옴을 방지할 수 있다
        if (county-30)%400 ==0: #윤년이다
            a = a - yy
            y = 1
        elif (county-30)%100 ==0: #평년이다
            a = a-py
            y =0
        else: #윤년이다
            a = a - yy
            y = 1
    elif (county-2)%4 != 0 and a>31622400 : #윤년이 아님
        a = a - py
        y = 0
    else:
        break

#31일을 초로 나타낸 경우
d31 = 2678400
#30일을 초로 나타낸 경우
d30 = 2592000
#29일을 초로 나타낸 경우
d29 = 2505600
#28일을 초로 나타낸 경우
d28 = 2419200
#식을 간결하게 하기 위해 미리 변수 선언
b = a-d31-d28

if y==0: #평년일때 7월까지
    if a % d31 > 1:  ##31일  #1월이 아닌경우
        if (a-d31)%d28 >1: #2월도 아닌경우
            for countm in range(3,8,1):
                if countm%2 == 0 and b-d31>0: #짝수달
                    b = b-d30
                    m = countm
                elif countm%2 !=0 and b-d31>0:
                    b = b-d31 #홀수달
                    m = countm
        else:
            m =1 #2로 안한 이유는 마지막에서 +1 시켜줄 것이기 때문
            b = a-d31
    else:
        m = 0 #1로 안한 이유는 마지막에서 +1 시켜줄 것이기 때문
        b = a

else: #윤년인 경우
    if a % d31 > 1:  ##31일  #1월이 아닌경우
        if (a - d31) % d29 > 1:  # 2월도 아닌경우
            for countm in range(3, 8, 1):
                if countm % 2 == 0:  # 짝수달
                    b = b - d30
                    m = countm
                else:
                    b = b - d31  # 홀수달
                    m = countm
        else:
            m = 1 #2로 안한 이유는 마지막에서 +1 시켜줄 것이기 때문
            b = a - d31
    else:
        m = 0 #2로 안한 이유는 마지막에서 +1 시켜줄 것이기 때문
        b = a

if m == 7:
    if b%d31 > 1:
        if (b-d31)%d31 >1:
            for countm in range(8, 13, 1):
                if countm % 2 == 0 and b >d31:  # 짝수달
                    b = b - d30
                    m = countm
                elif countm % 2 != 0 and b >d31:
                    b = b - d31  # 홀수달
                    m = countm
                else:
                    break
        else:
            m =7 #8로 안한 이유는 마지막에서 +1 시켜줄 것이기 때문
            b = b-d31
    else:
        m =6 #2로 안한 이유는 마지막에서 +1 시켜줄 것이기 때문

#시,분, 초 도출 파트
day = 86400
d = b/day
t = (b%day)//3600
minute = (b%day)%3600//60
second = (b%day)%3600%60

#최종프린트

print("[%04d-%02d-%02d]" % (county+1969, m+1, int(d)),end=' ')
print("%02d:%02d:%02d" % (t+9,minute,second))



"""
#2단계 월 구하기 1~7월과 8~12월로 구분
if y==0: #평년일때
    if a % d31 > 1:##31일  #1월이 아닌경우
        if (a-d31)%d28 >1: #2월도 아닌경우
            for countm in range(3,8,1):
                if countm %2 ==0: #짝수 달
                    if (a-d31-d28)//(d31*(countm-2)) >1:
                        m = countm
                        continue
                    else:
                        m = countm
                else:
                    if (a-d31-d28)//(d30*(countm-2)) >1:
                        m = countm
                        continue
                    else:
                        m = countm
                        break
        else:
            m = 2
    else:
        m = 1

else: #윤년일때
    if a % d31 > 1:  ##31일  #1월이 아닌경우
        if (a - d31) % d29 > 1:  # 2월도 아닌경우
            for countm in range(3, 8, 1):
                if countm % 2 == 0:  # 짝수 달
                    if (a - d31 - d29) // (d31 * (countm - 2)) > 1:
                        m = countm
                        continue
                    else:
                        m = countm
                else:
                    if (a - d31 - d29) // (d30 * (countm - 2)) > 1:
                        m = countm
                        continue
                    else:
                        m = countm
                        break
        else:
            m = 2
    else:
        m = 1

#평년 8월 이후부터
if m ==7 and y==0:
    if (a-d31*4-d28-d30*3) % d31 #8월인지 판단
        for countm in range(9, 13, 1):
            if countm % 2 == 0:  # 짝수 달
                if (a - d31 - d28) // (d31 * (countm - 2)) > 1:
                    m = countm
                    continue
                else:
                    m = countm
            else:
                if (a - d31 - d28) // (d30 * (countm - 2)) > 1:
                    m = countm
                    continue
                else:
                    m = countm
                    break
    else:
        m = 8
        
        

print(m)

"""

