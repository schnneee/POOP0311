#https://asecuritysite.com/forensics/magic
#f = open("data\\image1.png", "rb")
f = open("data\\image1.rar", "rb")
try:
    index = 1
    byte = f.read(1)
    while byte != "" and index < 9:
        x = int.from_bytes(byte, byteorder='little')
        print("%d,%s" % (index, str(hex(x))))
        byte = f.read(1)
        index += 1
finally:
    f.close()