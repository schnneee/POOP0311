fileHandler = open("data\\testfile1","w") # 目錄不存在會報exception
fileHandler.write("Hello world")
fileHandler.close()

# 相當於using? 用with as 就不需要自己去close
with open("data\\testfile2","w") as fileHandler2:
    fileHandler2.write("Hello world")

try:
    print("1. before open (may exception)")
    fileHandler = open("dataxx\\testfile1", "w")
    print("2. open succewss, prepare to read")
    fileHandler.write("Hello world")
    print("3. write success")
except NotImplementedError:
    # except IOError as io_e:
    print("got an io error")
# print("reason:", io_e)
except Exception as e:
    print("anyway got some error", e)
else: # 正常做完才進來
    print("T. file will close")
    fileHandler.close()
