def judge(inputScore):
    return 'good' if inputScore >= 80 else 'bad'

score = 80
print('%d is %s' % (score, judge(score)))

score2 = 20
print('%d is %s' % (score2, judge(score2)))


def judge2(inputScore):
    return ('bad', 'good')[inputScore >= 80]

score = 80
print('%d is %s' % (score, judge2(score)))

score2 = 20
print('%d is %s' % (score2, judge2(score2)))

# 三種if else 寫法
# if expr :
#     A
# else:
#     B

# A if expr else B

# (B, A)[expr]