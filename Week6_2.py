a,b = map(int,input().split(" "))

for n in range(a,b+1):
    if n>=10:
        if n>=100:
            if n != 103:
                if n !=  113:
                    if n != 123:
                        if n != 133:
                            if n != 143:
                                if n != 153:
                                    if n != 163:
                                        if n != 173:
                                            if n != 183:
                                                if n != 193:
                                                    print(n)
        else:
            if n != 13:
                if n != 23:
                    if n != 33:
                        if n != 43:
                            if n != 53:
                                if n != 63:
                                    if n != 73:
                                        if n != 83:
                                            if n != 93:
                                                print(n)
        
    else:
        if n !=3:
            print(n)
