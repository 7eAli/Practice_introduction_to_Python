data = open("text.txt", mode='w', encoding='utf-8')

data.write('Новая запись\n')

rows = data.readlines()
data.close()
print(rows)