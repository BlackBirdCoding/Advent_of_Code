with open("input_file.txt", "r") as f:
    number_list = f.read().split(',')
#print(number_list)

def check_repition(number_string):
    number = []
    for g in number_string:
        g = g.split()
        number.append(g)
    
   
    if len(set(number_string)) == 1:
        
        return number_string 
    for i in range (2, len(number)):
        
        if len(number)%i ==0:

            split_lists = [number[j::i] for j in range(i)]
            
            count = 0
            for a in split_lists:
                unique_count = len({tuple(x) for x in a})
                if unique_count == 1:
                    count+=1
            if count == len(split_lists):
                
                
                return number_string
    return 0




counter = 0
for rangee in number_list: #flip the clock so both ways get to be the right way (key for this solution)
    range_list = rangee.split('-')

    start = int(range_list[0])
    end = int(range_list[1])
    ##print(start,end,"hiii","byyy")
    
    
    for number in range (int(start),int(end)+1):
        
        number = str(number)
        if int(number) > 9:
            counter += int(check_repition(number))
        # mid = len(number)//2
        # if len(number)%2 ==0:
        #     new_doubbles_a = number[:mid]
        #     new_doubbles_b = number[mid:]

             
        #     if new_doubbles_a == new_doubbles_b: #If we are to dial left we skip counting, but still update the dial      
        #         print(number)   
        #         counter+=int(number)
        
print(counter)
