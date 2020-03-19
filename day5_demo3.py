import struct

o1 = open('data\\myfile.bin', "wb")
o2 = open('data\\myfile.asc', "w")

for i in range(0, 100):
    #    print('i=%d, pack=%s' % (i, repr(struct.pack('i', i))))
    o1.write(struct.pack('i', i))
    o2.write("%s\n" % str(i))
o1.close()
o2.close()

i1 = open('data\\myfile.bin', 'rb')
try:
    block = i1.read(400)
    str = ""
    for ch in block:
        str += hex(ch) + '\n'
    print(str)
finally:
    i1.close()