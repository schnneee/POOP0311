dict1 = {'name': 'python', 'duration': '35hr'}
dict2 = {'duration': '35hr', 'name': 'python'}
print(type(dict1), type(dict2))
print(dict1 == dict2)
dict3 = dict(name='python', duration='35hr')
print(type(dict3), dict1 == dict3)
dict4 = dict([("name", "python"), ("duration", "35hr")])
print(type(dict4), dict1 == dict4)
print(dict1, dict2, dict3, dict4)
print(dict1['name'])
dict1['instructor']='Mark'
print(dict1)
