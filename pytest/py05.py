import random as rd

for i in range(6):
    r = int(rd.random()*49)+1
    print("第%d次，隨機值為%2d"%(i+1, r))