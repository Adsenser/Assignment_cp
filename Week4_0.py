number = int(input("숫자를 입력하세요:"))
a = int(0)
b = int(0)

for n in range(2, number, 1):
    if number%n != 0:
        a = 1
        b = 0
    else:
        a = 0
        b = 1
        break

if a == 1:
    print(number,"는 소수입니다")

if b == 1:
    print(number,"는 소수가 아닙니다")
