#定义全局数据源，用户字典
accountlist = {}

#初始用户方法
def initAccount(userName, passWord, sex, billAccount):
    dic = { userName : {"Password" : passWord, "Sex" : sex, "BillAccount" : billAccount }}
    accountlist.update(dic)
    return accountlist

#验证用户输入用户名和密码是否匹配
def validatePassword(userName, passWord):
    if(accountlist[userName]["Password"] == passWord):
        return True
    return False


#显示当前登录用户余额
def showBillAccount(userName):
    print("查询成功，您的账户余额为:{0}".format(accountlist[userName]["BillAccount"])) 

#存款操作
def storeBillAccount(userName, billAccount):
    accountlist[userName]["BillAccount"] += int(billAccount)
    print("存款成功，您的账户余额为:{0}".format(accountlist[userName]["BillAccount"])) 

#取款操作
def takeOffBillAccount(userName, billAccount):
    if accountlist[userName]["BillAccount"] < int(billAccount):
        print("很抱歉，余额不足")
    else:
        accountlist[userName]["BillAccount"] -= int(billAccount)
        print("取款成功，您的账户余额为{}".format(accountlist[userName]["BillAccount"]))

#修改密码
def updatePassword(userName):
    inputNewPassword = input("请输入新密码(六位数字)：")
    if inputNewPassword == "":
        print("密码不能为空")
        return
    elif len(inputNewPassword) != 6:
        print("密码长度错误")
        return
    inputReNewPassword = input("请输入确认密码：")
    if inputReNewPassword == "":
        print("确认密码不能为空")
        return
    elif len(inputReNewPassword) != 6:
        print("确认密码长度错误")
        return
    elif inputNewPassword != inputReNewPassword:
        print("两次输入密码不一致")
        return
    accountlist[userName]["Password"] = inputNewPassword
    print("密码已经更新成功")


#显示用户信息
def displayInfor():
    for key in accountlist:
        print("|",end=" ")
        print(key, '=>', accountlist[key], end=" |\n")


#初始用户数据
initAccount("Lily","123456","Female",20000)
initAccount("George","123456","Male",50000)
initAccount("Anna","123456","Female",80000)


print("=" * 72)
displayInfor()
print("=" * 72)


while True:
    flag = False
    #用户权限验证
    inputUserName = input("请输入用户名：")
    if inputUserName in accountlist:
        inputPass = input("请输入密码：")
        if validatePassword(inputUserName, inputPass):
            print("{0}, 您好".format(inputUserName))
            flag = True
        else:
            print("密码输入有误")
            flag = False
    else:
        print("当前用户不存在")
        flag = False
    
    #用户业务部分
    while flag:
        print("请选择您需要的服务：")
        print("1. 查询余额")
        print("2. 存款")
        print("3. 取款")
        print("4. 修改密码")
        print("5. 退出")

        inputServiceType = input("请选择：")
        
        if inputServiceType == "1":
            showBillAccount(inputUserName)
            input("按回车键返回上级一菜单： ")
        elif inputServiceType == "2":
            inputBillAccount = input("请输入存入金额：")
            storeBillAccount(inputUserName, inputBillAccount)
            input("按回车键返回上级一菜单： ")
        elif inputServiceType == "3":
            inputBillAccount = input("请输入取款金额：")
            takeOffBillAccount(inputUserName, inputBillAccount)
            input("按回车键返回上级一菜单： ")
        elif inputServiceType == "4":
            updatePassword(inputUserName)
            input("按回车键返回上级一菜单： ")
        elif inputServiceType == "5":
            print("欢迎您下次光临！")
            break
        else:
            print("无效的键盘输入!")
            input("按回车键返回上级一菜单： ")