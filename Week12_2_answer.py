import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = []
for i in range(1000):
    data.append(random.randint(0,100))

#도수분포표 구하기
nbin = 10
bin_title = []
group = []
for i in range(nbin):
    group.append(0)
    if i == nbin-1:
        bin_title.append(str(i*10)+"~"+str((i+1)*10))
    else:
        bin_title.append(str(i*10)+"~"+str((i+1)*10-1))

for i in range(1000):
    if data[i] == 100:
        group[nbin-1] +=1
    else:
        group[data[i]//10] += 1

ftable = pd.DataFrame({"bin":bin_title,"freq":group})
ftable
