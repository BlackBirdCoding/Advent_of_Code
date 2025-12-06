# Day 5, star two, 2025

with open("input_file.txt", "r") as f:
    two_list_input = f.read().split('\n')
ranges = []
for i in range (0,len(two_list_input)):
    if two_list_input[i] == '':
        pos = i
ranges = two_list_input[:pos]
ranges = [tuple(map(int, r.split('-'))) for r in ranges]

def range_merger(ranges): #sorted list of ranges, if the next range ovelaps with the current, merge them
    ranges = list(set(ranges))
    ranges.sort()
    i = 0    
    while ranges[i] != ranges[-1]:
        if ranges[i][1]+2>ranges[i+1][0]:
            if ranges[i][1]>ranges[i+1][1]:
                start = ranges[i][0]
                end = ranges[i][1]
            else:
                start = ranges[i][0]
                end = ranges[i+1][1]
            ranges[i] = (start, end)    
            ranges.pop(i+1)            
            i -=1
        i +=1
    return ranges

ranges = range_merger(ranges)

final_count = 0
ranges = list(set(ranges))
for j in ranges:
    final_count += j[1]-j[0]+1

print(final_count)
