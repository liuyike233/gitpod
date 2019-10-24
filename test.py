import os
os.system("echo helloworld")
# 测试一下WEBIDE的性能


import itertools
import time

#计时开始
timeStart = int(time.strftime("%s"))


# 8个皇后 放在一个 8*8 的象棋格子里，使棋盘每一条斜线、行、列
# 都不会出现两个及以上的皇后，问有多少种解法？
'''
7    O * * * * * * *
6    * O * * * * * *
5    * * O * * * * *
4    * * * O * * * *
3    * * * * O * * *
2    * * * * * O * *
1    * * * * * * O *
0    * * * * * * * O
'''

#方法1、写检测是否符合规则的函数，遍历所有情况，每次都检测是否合格，情况有 8^8 = 16,777,216 种

#方法2、从64个棋格里的第一个开始，先放一枚，则将其斜线、行、列上的点全部置 2 ，落下一枚皇后时只能放为 0 的点

#改进方法 1 ：第一行下一个棋有8种，那么第二行有7种，最后一行则只有一种，
# 那么情况减小为：8！= 40320 种，但是会有对角线的情况存在，只需排除对角即可。


#定义一个 粗略表示棋子位置分布图的函数
def show(alist):
    str1 = ["😁","😁","😁","😁","😁","😁","😁","😁"]
    for i in alist:
        #print("我是i:",i)
        new_str = str1.copy()
        new_str[i[1]] = "😡"
        print(' '.join(new_str))



#定义对角线列表
flod = []
[  [ [2,3],[3,3] ]                                    ]
#根据数学规律，求出 30 条对角线，放入 3 维坐标
def find_point():
    #添加对角线的点，方向为：/ 从 0，7开始
    for i in range(8):
        j = 7
        flod.append([])
        if i < 7 : flod.append([])
        m,n = i,j
        while m>=0 and n>=0:
            flod[len(flod) - 1].append([m,n])
            if i < 7 : flod[len(flod) - 2].append([n,m])
            m,n = m-1,n-1
    #添加对角线的点，方向为：\ 从 0，7开始
    for i in range(8):
        j = 7
        flod.append([])
        if i > 0 : flod.append([])
        m,n = i,j
        while m<=7 and n>=0:
            flod[len(flod) - 1].append([m,n])
            if i >0 : flod[len(flod) - 2].append([m-i,n-i])
            m,n = m+1,n-1
    # for i in range(len(flod)):print(flod[i]) #打印出对角线坐标，每行一条

#按照 列 来下棋，第一列下过的行，第二列则不允许下,这样下出来的棋，只存在斜线不符合条件的情况，再根据斜线坐标进行排除即可。

count = 0                                               #计数变量
find_point()                                            #先把棋盘上的斜线点坐标都找出来
for i in itertools.permutations('01234567', 8):         #进行排列组合
    #print(i)
    addSum = 0
    for xylist in flod:                                 #遍历每条斜线
        temp = 0
        for m in range(8):                              #配上横坐标，形成一个皇后，遍历这 8 个皇后
            if [m,int(i[m])] in xylist:                 #如果皇后在 xylist 上，且线上的皇后少于两个，
                temp += 1                               #那么temp就加一
            if temp == 2:                               #多于两个的话就不用再往下试其他的皇后了
                break                                   #退出本次遍历皇后
        if temp < 2 :                                   #皇后个数小于2，表示这条斜线上有两个以下的皇后，符合条件
            addSum += 1                                 #计次，看看有几条斜线符合
    if addSum == len(flod):                             #addSum等于斜线的个数，表示所有斜线都只有两个以下皇后
        count += 1                                      #说明这8个皇后满足条件
        templist = []                                   #创建临时列表
        for q in range(8):                              #遍历8个皇后坐标
            templist.append([q,int(i[q])])              #把坐标 加入到 临时列表
        show(templist)                                  #调用函数 emoji表情显示
        print("第",count,"种坐标：",templist)                                 #显示这盘棋的皇后坐标
print("共有情况：",count,"种解")                         #显示统计情况

timeEnd = int(time.strftime("%s"))


print("总用时：",timeEnd - timeStart,"s")


