numbers_dict = {0:'ling', 1:'yi', 2:'er', 3:'san', 4:'si', 5:'wu', 6:'liu', 7:'qi', 8:'ba', 9:'jiu'}
number_str = input()
summ = 0

for x in number_str:
    summ = summ + int(x)

result_str = ''

for x in str(summ):
    result_str = result_str + numbers_dict[int(x)] + ' '

#print(result_str[:-1])
print(result_str.rstrip())