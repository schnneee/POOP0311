def myException(level):
    if level < 1:
        raise Exception("some reason", "some more detail")
# throw Exception

try:
    myException(0)
except Exception as e:
    print("1", e)
else:
    print("2", "run smoothly")
