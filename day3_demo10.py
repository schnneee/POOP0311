scores = [70, 60, 80, 50, 90]


def judge(x):
    if x < 60:
        return "Fail"
    else:
        return "Pass"


results = []
for s in scores:
    results.append(judge(s))
print(results)

print([judge(s) for s in scores])

for s in scores:
    print("%d==>%s" % (s, judge(s)))