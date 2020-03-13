sales = list('SMLSMLLMSSSSMMMLLLLSSMLSMLSMLSMLSMLSMLMSLMLS')
sales.append('XL')
sales.append('XXS')
sales.append('XXS')
sales.append('XXS')
sales.append('XL')
print(type(sales), len(sales), sales)
# count = {'S': 0, 'M': 0, 'L': 0}
count = {}
print(type(count))
for sale in sales:
    count.setdefault(sale, 0) # 沒有的話就給預設值
    count[sale] = count[sale] + 1
print(count)

sales2 = [('S', 200), ('M', 500), ('S', 300), ('M', 300), ('L', 500)]
count2 = {}
for name, quantity in sales2:
    count2.setdefault(name, 0)
    count2[name] = count2[name] + quantity
print(count2)