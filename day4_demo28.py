fileOut = open("data\\output.txt","w")
linesToWrite=["First to write something\n","add something else\n"]
fileOut.writelines(linesToWrite)
fileOut.close()

for i in range(0,20):
    fileOut2 = open('data\\output2.txt','a')
    fileOut2.writelines(linesToWrite) # 接著寫下去
    fileOut2.close()