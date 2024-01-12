tab_pos2=[]
pos = 2
tab_pos2 =[[0],[0],1,[0],[0],1,[0],[0],2]
max = 1
x = 0
for index in range(len(tab_pos2)):
    if ((index+1)%3) ==0 and index!=3 and max < tab_pos2[index]:
        print(tab_pos2[index])
