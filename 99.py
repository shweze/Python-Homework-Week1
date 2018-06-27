# 9 * 9 打印输出
print("###############  WHILE 方式一： ###############")
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("{0}*{1}={2:<5}".format(j,i,i*j), end = '')
        j = j + 1
    i = i + 1
    #格式换行
    print("")  
print("#################"*5)


print("###############  WHILE 方式二： ###############")
i = 9
while i > 0:
    j = 1
    while j <= i:
        print("{0}*{1}={2:<5}".format(j,i,i*j), end = '')
        j = j + 1
    i = i - 1
    #格式换行
    print("")  
print("#################"*5)


print("###############  WHILE 方式三： ###############")
i = 1
while i < 10:
    j = 9
    while j > 0:
        if j <= i:
            print("{0}*{1}={2:<5}".format(j,i,i*j), end = '')
        else:
            #依据等式位数占位
            print(" "*9, end="")
        j = j - 1
    i = i + 1
    #格式换行
    print("")  
print("#################"*5)


print("###############  WHILE 方式四： ###############")
i = 9
while i > 0:
    j = 9
    while j > 0:
        if j <= i:
            print("{0}*{1}={2:<5}".format(j,i,i*j), end = '')
        else:
            #依据等式位数占位
            print(" "*9, end="")
        j = j - 1
    i = i - 1
    #格式换行
    print("")  
print("#################"*5)


print("###############  FOR .. IN 方式一： ###############")
for i in range(1, 10):
    for j in range(1, i+1):
        print("{0}*{1}={2:<5}".format(j,i,i*j), end = '')
    #格式换行
    print("")  
print("#################"*5)


print("###############  FOR .. IN 方式二： ###############")
for i in range(9, 0, -1):
    for j in range(1, i+1):
        print("{0}*{1}={2:<5}".format(j,i,i*j), end = '')
    #格式换行
    print("")  
print("#################"*5)


print("###############  FOR .. IN 方式三： ###############")
for i in range(1, 10):
    for j in range(9, 0, -1):
        if j <= i:
            print("{0}*{1}={2:<5}".format(j,i,i*j), end = '')
        else:
            #依据等式位数占位
            print(" "*9, end="")
    #格式换行
    print("")  
print("#################"*5)


print("###############  FOR .. IN 方式四： ###############")
for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        if j <= i:
            print("{0}*{1}={2:<5}".format(j,i,i*j), end = '')
        else:
            #依据等式位数占位
            print(" "*9, end="")
    #格式换行
    print("")  
print("#################"*5)
