import ast

x1 = "None"
# x2 = "None of them"
x2 = "None"
x3 = "None"

y1 = ast.literal_eval(x1)
print(type(x1), type(y1), x1, y1)
y2 = None if x2 == 'None' else x2
print(type(x2), type(y2), x2, y2)
y3 = eval(x3)
print(type(x3), type(y3), x3, y3)
x4 = None
x5 = None
print(x4==x5)