import os

myPath = "c:/windows/system32"

for currentFolder, subFolders, fileNames in os.walk(myPath):
    print(currentFolder, subFolders)
    # for f in subFolders:
    #     print(f)
    for file in fileNames:
        print(file)