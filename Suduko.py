import random
#生成数独
sud = [[1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ],
       [4 , 5 , 6 , 7 , 8 , 9 , 1 , 2 , 3 ],
       [7 , 8 , 9 , 1 , 2 , 3 , 4 , 5 , 6 ],
       [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 1 ],
       [5 , 6 , 7 , 8 , 9 , 1 , 2 , 3 , 4 ],
       [8 , 9 , 1 , 2 , 3 , 4 , 5 , 6 , 7 ],
       [3 , 4 , 5 , 6 , 7 , 8 , 9 , 1 , 2 ],
       [6 , 7 , 8 , 9 , 1 , 2 , 3 , 4 , 5 ],
       [9 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ]]
#初始化数独种子

def printsud(): #函数-打印当前数独数组
    for i in range(9):
        print('|',end='')
        for j in range(9):
            if sud[i][j] != 0 :
                print (' '+str(sud[i][j])+' |',end='')
            else :
                print ('   |',end='')
        print ("\n")
    return

def switchnum(x,y): #交换数字
    for i in range(9):
        for j in range(9):
            if sud[i][j] == x:
                sud[i][j] = y
                continue
            if sud[i][j] == y:
                sud[i][j] = x
                continue

def switchrow(row): #交换行
    way = int(random.uniform(0,3))
    if way == 0 :
        for i in range(9):
            sud[row*3+0][i],sud[row*3+1][i] = sud[row*3+1][i],sud[row*3+0][i]
    if way == 1 :
        for i in range(9):
            sud[row*3+1][i],sud[row*3+2][i] = sud[row*3+2][i],sud[row*3+1][i]
    if way == 2 :
        for i in range(9):
            sud[row*3+0][i],sud[row*3+2][i] = sud[row*3+2][i],sud[row*3+0][i]
    return

def switchcol(col): #交换列
    way = int(random.uniform(0,3))
    if way == 0 :
        for i in range(9):
            sud[i][col*3+0],sud[i][col*3+1] = sud[i][col*3+1],sud[i][col*3+0]
    if way == 1 :
        for i in range(9):
            sud[i][col*3+1],sud[i][col*3+2] = sud[i][col*3+2],sud[i][col*3+1]
    if way == 2 :
        for i in range(9):
            sud[i][col*3+0],sud[i][col*3+2] = sud[i][col*3+2],sud[i][col*3+0]
    return

def blank(num): #挖空
    js = 0
    while js < num :
        js = js + 1
        i = int(random.uniform(0,9))
        j = int(random.uniform(0,9))
        if sud[i][j] == 0 :
            i = int(random.uniform(0,9))
            j = int(random.uniform(0,9))
        sud[i][j] = 0

def checkthis(inii,inij,inin): #检查当前数字是否合法
    #检查行
    for k in range(9):
        if sud[inii][k] == inin and k != inij :
            return False
    #检查列
    for k in range(9):
        if sud[k][inij] == inin and k != inii :
            return False
    #检查九宫格
    row = int(inii/3)
    col = int(inij/3)
    for i in range(3):
        for j in range(3):
            if sud[row*3+i][col*3+j] == inin and inii != row*3+i :
                return False
    #返回成功
    return True

def solvethis(): #解决数独
    js = 0
    for i in range(9):
        for j in range(9):
            if sud[i][j] == 0:
                js = js + 1
    for o in range(js):
        i = findmin(0)
        j = findmin(1)
        array = [1,2,3,4,5,6,7,8,9]
        for k in range(len(array)):
            if checkthis(i,j,array[k]) == False:
                if k == 8:
                    return False
                continue
            else:
                sud[i][j] = array[k]
                if solvethis() == False:
                    sud[i][j] = 0
                else :
                    return True
    return True

def findmin(typ): #查找最小可能
    mins = [0,0,10]
    for i in range(9):
        for j in range(9):
            if sud[i][j] == 0 :
                array = [1,2,3,4,5,6,7,8,9]
                temp = 0
                for k in range(len(array)):
                    if checkthis(i,j,array[k]) == False:
                        continue
                    else :
                        temp = temp + 1
                if temp < mins[2]:
                    mins[0] = i
                    mins[1] = j
                    mins[2] = temp
    if typ == 0:
        return mins[0]
    if typ == 1:
        return mins[1]

#主程序开始
for i in range(9):
    switchnum(int(random.uniform(1,10)),int(random.uniform(1,10)))

for i in range(3):
    switchrow(i)
    switchcol(i)

blanknum = int(input("请输入挖空数量，最高推荐为60"))

print("------------原始完整数独--------------")
printsud()
blank(blanknum)
print("------------最后生成数独--------------")
printsud()
print("------------尝试解决数独--------------")
if solvethis() == False:
    print("解决失败")
else :
    printsud()
