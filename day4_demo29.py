import glob
import os

path = 'c:/Windows' #使用後可用反斜線代替\\
allDlls = os.path.join(path, "*/*.dll")
for d in glob.glob(allDlls):
    print(d)