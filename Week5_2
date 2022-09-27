import math, cmath

a = float(input("a를 입력하시오:"))
b = float(input("b를 입력하시오:"))
c = float(input("c를 입력하시오:"))

if a == 0 and b != 0 and c !=0:
    sol = -c/b
    print(sol)
    
elif a==0 and b==0 and c !=0:
    print("근이 없다")
    
elif a==0 and b==0 and c==0:
    print("근이 무수히 많다")
    
else:
    if (b**2)-(4*a*c) < 0:
        sol3 = -b+cmath.sqrt(b**2-4*a*c)/2*a
        sol4 = (-b-cmath.sqrt(b**2-4*a*c))/2*a
        print(sol3,sol4)
        
    elif (b**2)-(4*a*c) == 0:
        sol0 = (-b)/2*a
        print(sol0)
    else:
        sol1 = -b+math.sqrt(b**2-4*a*c)/2*a
        sol2 = (-b-math.sqrt(b**2-4*a*c))/2*a
        print(sol1,sol2)
        
        
    
  
    
