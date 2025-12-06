#Day 6, 2025, star two

#I appologise for this code, sorry I got frustrated

import math
with open("input_file.txt", "r") as f:
    list_input = f.read().splitlines()
list_of_lists = []
for i in list_input:
    string_list=[]
    for j in i:
        string_list.append(j)
    list_of_lists.append(string_list)
digits =['1','2','3','4','5','6','7','8','9','0']

row_length = len(list_of_lists[0])


list_of_breakers=[]
list_of_IIII =[]
for a in range(0,row_length):
    count=0
    mini =[]
    for row in list_of_lists:
        mini.append(row[a])
        if row[a]==' ':
     
            count+=1
    list_of_IIII.append(mini)
    if count ==5:###CHANGE
        list_of_breakers.append(int(a))

better_II =[]
for I in range(0,len(list_of_IIII)):

    if I in list_of_breakers:
        better_II.append(['X','X','X','X','X'])
        
    else:
        minione =[]
        for char in list_of_IIII[I]:
            if char in digits:
                minione.append(char)
        better_II.append(minione)


even_better_II =[]
for s in better_II:
    stringy = ''
    for d in s:
        stringy=stringy+d
    even_better_II.append(stringy)



while ' ' in list_of_lists[-1]:
    list_of_lists[-1].remove(' ')
list_of_operators =list_of_lists[-1]

minilisty=[]
bigger_list = []
for i in even_better_II:
    
    if i != "XXXXX":
        minilisty.append(int(i))
    else:
        bigger_list.append(minilisty)
        minilisty = []
bigger_list.append(minilisty)


# for i in even_better_II:
#     if i == 'XXXXX':
#         list_of_operators.pop(0)
#     else:
#         if list_of_operators[0] =='*':
#             number = int(i)

#             print(str(i) + ' ' + str(number) + ' *  ' + str(new_problem_list[i]))
#             final_sum += number 
        

#         if list_of_operators[0] =='+':
#             number = sum(new_problem_list[i])
#             print(str(i) + ' ' + str(number) + '  +  ' + str(new_problem_list[i]))
#             final_sum += number
    
    


final_sum = 0
for i in range(len(bigger_list)):
 
    if list_of_operators[i] =='*':
        number = math.prod(bigger_list[i])  
        #print(str(i) + ' ' + str(number) + ' *  ' + str(bigger_list[i]))
        final_sum += number 
        

    if list_of_operators[i] =='+':
        number = sum(bigger_list[i])
        #print(str(i) + ' ' + str(number) + '  +  ' + str(bigger_list[i]))
        final_sum += number
    
print(final_sum)
    