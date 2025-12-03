with open("input_file.txt", "r") as f:
    number_list = f.read().splitlines()

def joltage(number):

    listy = []
    for i in number:
        i = int(i)
        listy.append(i)
    

   
    list_joltage = []
    for j in range (0,12):
        start = 0
        for i in range (0,len(listy)-11+j):
            digit = listy[i]
            digit = int(digit)
            if digit>start:
                start = listy[i]
                pos = i
                
        list_joltage.append(start)       
        listy = listy[pos+1:]
        
    joltage = ""
    for i in list_joltage:
        joltage += str(i)
    return int(joltage)
    # for i in range (0,len(listy)):
    #     digit = listy[i]
    #     digit = int(digit)
    #     if digit>end:
    #         end = listy[i]
    #         pos = i

    # start = str(start)
    # end = str(end)
    # joltage = start+end
    # joltage = int(joltage)
count = 0
for row in number_list:
    count+= joltage(row)
print(count)


