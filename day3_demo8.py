obj1 = {'key1': 'value1',
        'key3': 'value3'}
keys = ['key1', 'key2', 'key3', 'key4']
for key in keys:
    print(obj1.get(key) and obj1[key])