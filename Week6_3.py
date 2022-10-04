import random

p = int(input("게임 참자가 수를 입력하시오"))
m = float(input("실수할 확률을 입력하시오_범위는 0~1 사이 실수"))
g = 1
jj =0

direction = 1
person = 65

while p > 0:
    mistake = random.random()
    if mistake < m:
        print(chr(person),"실수함 -> 술래")
        break

    else:
        if 64<person <=65+p-1: #정상 범위일때 
            if g % 3 == 0:

                skill = random.random()
                if skill < (1 / 3):
                    if direction == +1:
                        print(chr(person), ": 고")
                        person += 1
                    else:
                        print(chr(person), ": 고")
                        person -= 1
                elif (1 / 3) <= skill < (2 / 3):
                    if direction == +1:
                        print(chr(person), ": 백")
                        person -= 1
                        direction = -1
                    else:
                        print(chr(person), ": 백")
                        person += 1
                        direction = +1
                else:
                    
                    if direction == 1: #양의 방향으로 갈때
                        print(chr(person), ": 점프")
                        #마지막에서 2칸에 위치할 때부터 문제가 되므로 jj라는 변수 통해 현재 어디 위치인지 각각 나누기
                        if (65+p)-person ==2:
                            jj = -2
                        elif (65+p)-person == 1:
                            jj = -1
                        else:
                            jj = 0
                        
                        
                        person += 2
                    else: #음의 방향으로 갈때
                        print(chr(person), ": 점프")
                        if person-2 ==63:
                            jj = +1
                        elif person-2 == 64:
                            jj = +2
                        else:
                            jj = 0
                        
                        person -= 2


                g += 1
            else:
                print(chr(person), ": ", g)
                person += direction
                g += 1
                
#정상 범위가 아닐때 조정해 주는 파트                
                
        
        elif person > 65+p-1 and jj==0:#jj==0이 있어야 점프 상황일때만 따로 처리 가능
            person = 65
            continue
            
           
        elif person <65 and jj ==0:
            person = 65+p-1
            continue
        
        elif jj!= 0: # 점프 하기 전 어느 위치에 있었느냐에 따라<jj이용> 점프 이후 값 분류
            if jj == -2:
                person = 65
                jj =0 
            elif jj == -1:
                person = 66
                jj = 0
            elif jj == +2:
                person = 65+p-1
                jj =0
            elif jj == +1:
                person = 65+p-2
                jj=0


