line = input()
let_up = 0
let_low = 0
for char in line:
    if char > 'z':
       continue
    if char.islower():
        let_low += 1
    if char.isupper():
        let_up += 1
print(let_low, ' low', let_up, ' capital')