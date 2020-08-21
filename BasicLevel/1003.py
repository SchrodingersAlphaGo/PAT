def cond(strs):
    if len(strs) < 3:
        return False
    
    sdt = ['P', 'A', 'T']
    for x in strs:
        if x not in sdt:
            return False
    
    if 'P' not in strs or 'T' not in strs or 'A' not in strs:
        return False
    
    pindex = strs.index('P')
    tindex = strs.index('T')
    if pindex >= tindex-1:
        return False
    strs0 = strs[:pindex] + strs[pindex+1:tindex] + strs[tindex+1:]
    for x in strs0:
        if not x=='A':
            return False
    na = pindex
    nb = tindex - pindex - 1
    nc = len(strs) - 1 - tindex
    if nb * na == nc:
        return True
    else:
        return False

n = int(input())
str_in = []
for i in range(n):
    str_in.append(input())

#print(str_in)

for x in str_in:
    if cond(x):
        print('YES')
    else:
        print('NO')