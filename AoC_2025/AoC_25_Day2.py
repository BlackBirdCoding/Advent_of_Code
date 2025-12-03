#Day 2, star 2, 2025

with open("input_file.txt", "r") as f:
    input_as_list = f.read().split(',')

def check_repition(number_as_string):
    number_as_list = []
    for g in number_as_string:
        g = g.split()
        number_as_list.append(g)
    
   
    if len(set(number_as_string)) == 1:
        
        return number_as_string 
    for i in range (2, len(number_as_list)):
        
        if len(number_as_list)%i ==0:

            split_lists = [number_as_list[j::i] for j in range(i)]
            
            count = 0
            for each_list in split_lists:
                unique_count = len({tuple(x) for x in each_list})
                if unique_count == 1:
                    count+=1
            if count == len(split_lists):
                
                
                return number_as_string
    return 0

counter = 0
for one_range in input_as_list: 
    range_list = one_range.split('-')
    start = int(range_list[0])
    end = int(range_list[1])
        
    for number in range (int(start),int(end)+1):
        
        number = str(number)
        if int(number) > 9:
            counter += int(check_repition(number))       
        
print(counter)
