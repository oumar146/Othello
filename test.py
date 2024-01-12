tab_pos2=[]
pos = 2
tab_pos2 =[[0],[0],1,[0],[0],1,[0],[10],2,[0],[7],3]
max = 0
x = 0
max = tab_pos2[pos]
for index in range(len(tab_pos2)):
    if ((index+1)%3) ==0:
        if max < tab_pos2[index]:                  
            pos=index
            max=tab_pos2[index]                
print([tab_pos2[pos-2][0],tab_pos2[pos-1][0]])


            