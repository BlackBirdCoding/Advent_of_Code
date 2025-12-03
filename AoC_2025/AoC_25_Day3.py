with open("input_file.txt", "r") as f:
    input_as_list = f.read().splitlines()

def joltage(string_of_digits):

    list_of_digits = []
    for i in string_of_digits:
        i = int(i)
        list_of_digits.append(i)
    
    list_of_joltages = []
    for j in range (0,12):
        highest_number = 0
        for i in range (0,len(list_of_digits)-11+j):
            digit = list_of_digits[i]
            digit = int(digit)
            if digit>highest_number:
                highest_number = list_of_digits[i]
                position = i
                
        list_of_joltages.append(highest_number)       
        list_of_digits = list_of_digits[position+1:]
        
    joltage = ""
    for i in list_of_joltages:
        joltage += str(i)
    return int(joltage)
    
count = 0
for row in input_as_list:
    count+= joltage(row)
print(count)


