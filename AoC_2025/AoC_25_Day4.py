#Day 4, 2025, star 2
with open("input_file.txt", "r") as f:
    input_as_list = f.read().splitlines()

list_of_lists = []
for row in input_as_list:
    symbol_list = []
    for symbol in row:
        symbol_list.append(symbol)
    list_of_lists.append(symbol_list)

star_two_count = 0

def Roll_Remover(list_of_lists):
    final_counter = 0
    for Row in range(1,len(list_of_lists)-1): #First I check all positions that have 8 neigbours
        for Symbol in range(1,len(list_of_lists[0])-1):
            count = 5
            if list_of_lists[Row][Symbol] == '@':
                count = 0
                if list_of_lists[Row][Symbol-1] == '@':
                    count +=1
                if list_of_lists[Row][Symbol+1] == '@':
                    count +=1
                if list_of_lists[Row-1][Symbol] == '@':
                    count +=1
                if list_of_lists[Row-1][Symbol-1] == '@':
                    count +=1
                if list_of_lists[Row-1][Symbol+1] == '@':
                    count +=1
                if list_of_lists[Row+1][Symbol] == '@':
                    count +=1
                if list_of_lists[Row+1][Symbol-1] == '@':
                    count +=1
                if list_of_lists[Row+1][Symbol+1] == '@':
                    count +=1
            if count < 4:
                list_of_lists[Row][Symbol] = 'X'
                final_counter+=1

    for Symbol in range(1,len(list_of_lists[0])-1): #Then I ckeck the uppermost row
        count = 5
        if list_of_lists[0][Symbol] == '@':
            count = 0
            if list_of_lists[0][Symbol-1] == '@':
                count +=1
            if list_of_lists[0][Symbol+1] == '@':
                count +=1
            if list_of_lists[1][Symbol] == '@':
                count +=1
            if list_of_lists[1][Symbol-1] == '@':
                count +=1
            if list_of_lists[1][Symbol+1] == '@':
                count +=1
        if count < 4:
            list_of_lists[0][Symbol] = 'X'
            final_counter+=1
        count = 5
        if list_of_lists[-1][Symbol] == '@': #Then then Lowest row
            count = 0
            if list_of_lists[-1][Symbol-1] == '@':
                count +=1
            if list_of_lists[-1][Symbol+1] == '@':
                count +=1
            if list_of_lists[-2][Symbol] == '@':
                count +=1
            if list_of_lists[-2][Symbol-1] == '@':
                count +=1
            if list_of_lists[-2][Symbol+1] == '@':
                count +=1
        if count < 4:
            list_of_lists[-1][Symbol] = 'X'
            final_counter+=1

    for Row in range(1,len(list_of_lists)-1): #Then the leftmost side
        count = 5
        if list_of_lists[Row][0] == '@':
            count = 0
            if list_of_lists[Row][1] == '@':
                count +=1
            if list_of_lists[Row-1][0] == '@':
                count +=1
            if list_of_lists[Row-1][1] == '@':
                count +=1
            if list_of_lists[Row+1][0] == '@':
                count +=1
            if list_of_lists[Row+1][1] == '@':
                count +=1
        if count < 4:
            list_of_lists[Row][0] = 'X'
            final_counter+=1
        count = 5
        if list_of_lists[Row][-1] == '@': #Then the rightmost side
            count = 0
            if list_of_lists[Row][-2] == '@':
                count +=1
            if list_of_lists[Row-1][-1] == '@':
                count +=1
            if list_of_lists[Row-1][-2] == '@':
                count +=1
            if list_of_lists[Row+1][-1] == '@':
                count +=1
            if list_of_lists[Row+1][-2] == '@':
                count +=1
        if count < 4:
            list_of_lists[Row][-1] = 'X'
            final_counter+=1

    if list_of_lists[0][0] == '@': #Finally I check the corners
        list_of_lists[0][0] = 'X'
        final_counter +=1
    if list_of_lists[0][-1] == '@':
        list_of_lists[0][-1] = 'X'
        final_counter +=1
    if list_of_lists[-1][0] == '@':
        list_of_lists[-1][0] = 'X'
        final_counter +=1
    if list_of_lists[-1][-1] == '@':
        list_of_lists[-1][-1] = 'X'
        final_counter +=1

    return final_counter

break_point = 0
while break_point < 30: #I loop through it enough times
    Roll_Remover(list_of_lists)
    break_point+=1

total_roll_count = 0 #Then I check how many 'X'es there are
for i in list_of_lists:
    for j in i: 
        if j == 'X':
            total_roll_count +=1
    
print(total_roll_count) #DONE!





