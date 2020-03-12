dict1 = {'name': 'python', 'duration': '35hr',
         'instructor': 'Mark'}
for x in dict1:
    print('iterate as:', x, ', corresponding element as:', dict1[x])
for y in dict1.keys():
    print('[II]iterate as:%s, corresponding element as:%s' % (y, dict1[y]))
for z in dict1.values():
    print(z)
for i in dict1.items():
    print(type(i), '[III]iterate as:{}, corresponding element as:{}'.format(i[0], i[1]))
for key, value in dict1.items():
    print(f'[III]iterate as:{key}, corresponding element as:{value}')