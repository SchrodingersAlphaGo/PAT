n = int(input())
list_input = []
for i in range(n):
    list_input.append(input())

data_dict = {}
grade_list = []
for x in list_input:
    temp = x.split()
    data_dict[int(temp[-1])] = temp[0] + ' ' + temp[1]
    grade_list.append(int(temp[-1]))

print(data_dict[max(grade_list)])
print(data_dict[min(grade_list)])