import math

with open("input_file.txt", "r") as f:
    list_input = f.read().splitlines()

new_list = []
for line in list_input:
    line = line.split(' ')
    i = 0
    while '' in line:
        line.remove('')
    new_list.append(line)

list_of_problems =[]
list_of_operators=[]

for digit in range (0,len(new_list[0])):
    one_problem = []
    for lists in new_list:
        one_problem.append(lists[digit])
    list_of_operators.append(one_problem[-1])
    one_problem.pop(-1)
    list_of_problems.append(one_problem)

new_problem_list=[]
for items in list_of_problems:
    nums = [int(x) for x in items]
    new_problem_list.append(nums)

print('')
print(new_problem_list)
print('')    

print(len(list_of_operators))
print(len(new_list[0]))


final_sum = 0
for i in range(len(new_problem_list)):
 
    if list_of_operators[i] =='*':
        number = math.prod(new_problem_list[i])  
        print(str(i) + ' ' + str(number) + ' *  ' + str(new_problem_list[i]))
        final_sum += number 
        

    if list_of_operators[i] =='+':
        number = sum(new_problem_list[i])
        print(str(i) + ' ' + str(number) + '  +  ' + str(new_problem_list[i]))
        final_sum += number
    
    


print(final_sum)
#15023655625
#14905911460
#328280640588
#4387670995909