import os

def CalculateFolderSize(folderDir):
    fileSize = 0
    if os.path.isdir(folderDir):
        vlist = os.listdir(folderDir)
        for f in vlist:
            vfile = os.path.join(folderDir, f)
            if os.path.isdir(vfile):
                fileSize += CalculateFolderSize(vfile)
            else:
                print(vfile)
                fileSize += os.path.getsize(vfile)
    #若当前传入参数为文件，返回当前文件大小
    else:
        print(folderDir)
        fileSize += os.path.getsize(folderDir)        
    return fileSize

'''
# test case
print(CalculateFolderSize("/Users/shweze/Samsung"))
'''