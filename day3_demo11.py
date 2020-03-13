def judge(x):
    if x > 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'FAIL'

# 拍森沒switch...傻眼

scores = [70, 60, 80, 50, 90]
for s in scores:
    print("%d==>%s" % (s, judge(s)))
