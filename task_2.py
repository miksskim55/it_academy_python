line = input()
new_word = ''

line = line.replace(' ', '')
for i in line:
    if i not in new_word:
        new_word += i
print(new_word)