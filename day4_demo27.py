file1 = open('data\\Python_Introduction.txt', encoding='UTF8')
readme_txt = file1.read()
file1.close()

print(type(readme_txt), len(readme_txt), readme_txt[:50])

with open('data\\clone.txt', 'w', encoding='UTF-8') as file2:
    file2.write(readme_txt)
