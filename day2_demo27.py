sales = list('SMLSMLLMSSSSMMMLLLLSSMLSMLSMLSMLSMLSMLMSLMLS')
#sales.append('XL')
print(type(sales), len(sales), sales)
count = {'S': 0, 'M': 0, 'L': 0}
print(type(count))
for sale in sales:
    count[sale] = count[sale] + 1
print(count)