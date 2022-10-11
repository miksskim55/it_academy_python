s = str(input())
s_new = [str(i) for i in s]
s_p = []
for j in range(len(s_new)):
    if s_new[j] in {'(', '{', '['}:
        s_p.append(s_new[j])
        continue
    if s_new[j] in {')', '}', ']'}:
        if len(s_p) >= 1 and s_p[-1] + s_new[j] in {'()', '{}', '[]'}:
            s_p.pop()
        else:
            s_p.append(s_new[j])
            print('no')
            break
if s_p == []:
    print('yes')