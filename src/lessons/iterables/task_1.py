s = str(input())
s_new = [str(i) for i in s]
s_p = []
for j in range(len(s_new)):
    if s_new[j] == '(' or s_new[j] == '[' or s_new[j] == '{':
        s_p.append(s_new[j])
        continue
    if s_new[j] == ')' or s_new[j] == ']' or s_new[j] == '}':
        if s_p[-1] + s_new[j] == '()' or s_p[-1] + s_new[j] == '[]' or s_p[-1] + s_new[j] == '{}':
            s_p.pop()
        else:
            print('no')
if s_p == []:
    print('yes')

