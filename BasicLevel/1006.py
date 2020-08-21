def unitFormat(n):
    temp = ''
    for i in range(1,n+1):
        temp = temp + str(i)
    return temp

n = int(input())
nbai = n//100
nshi = (n - nbai*100) // 10
nunit = n - nbai*100 - nshi*10

print('B'*nbai + 'S'*nshi + unitFormat(nunit))
