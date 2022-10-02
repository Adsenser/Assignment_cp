year, month, date, time = map(int, input().split(' '))
hour = time//3600
minute = (int(time)%3600)//60
second = ((int(time)%3600)%60)
print("%04d" % year , "%02d" % month, "%02d" % date,sep="-",end="")
print("@",end="")
print("%02d" % hour, "%02d" % minute, "%02d" % second, sep=':')
