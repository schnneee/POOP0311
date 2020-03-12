import constant.const

print(constant.const.GRAVITY)
print(constant.const.MAX_CONNECTION_COUNT)
print(constant.const.PI)

from constant.const import GRAVITY, MAX_CONNECTION_COUNT, PI
print(GRAVITY, MAX_CONNECTION_COUNT, PI)

import constant.const as c
print(c.GRAVITY, c.PI, c.MAX_CONNECTION_COUNT)

# 都是假的，要改還是改得了
c.GRAVITY += 1
print(c.GRAVITY, c.PI, c.MAX_CONNECTION_COUNT)
