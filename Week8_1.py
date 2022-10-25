line = 5
blank_plus = 0
blank_plus_1 = 4

for line_count_1 in range(line,1,-1):
    for blank_1 in range(blank_plus_1,0,-1):
        print(" ",end="")
    for star_1 in range(1,6-line_count_1+1,1):
        print("\u2605",end="")
    blank_plus_1 -=1
    print()
for line_count in range(1,line+1):
    for star in range(line_count,line+1,1):
        print("\u2605",end="")
    for blank in range(0,blank_plus):
        print(" ",end="")
    blank_plus +=1
    print()
