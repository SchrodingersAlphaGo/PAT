def list2str(ls):
    temp = ''
    for x in ls:
        temp = temp + str(x) + ' '
    return temp.strip()

def covered_number(n):
    ls = []
    while (n>=1):
        if n == 1:
            break
        elif n%2 == 0:
            n = n / 2
        else:
            n = (3 * n + 1) / 2
        ls.append(int(n))
    return ls

n = int(input())
nums_input = input()
array = [int(x) for x in nums_input.split()]
cover_nums = set()
for x in array:
    cover_nums = cover_nums | set(covered_number(x))

result_list = []
for x in array:
    if x not in cover_nums:
        result_list.append(x)

result_list.sort(reverse=True)
print(list2str(result_list))