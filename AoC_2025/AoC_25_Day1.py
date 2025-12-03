#Day one star 2, 2025
with open("input_file.txt", "r") as f:
    dial_number_list = f.read().splitlines()

counter = 0
for letter in ['L','R']: #flip the clock so both ways get to be the right way (key for this solution)
    old_dial = 50 
    for row in dial_number_list:
        new_dial_instruction = int(row[1:])        
        if row[0]==letter: #If we are to dial left we skip counting, but still update the dial         
            new_dial = old_dial - new_dial_instruction  
        else:
            new_dial = old_dial + new_dial_instruction 
            counter += (new_dial // 100) - (old_dial // 100) #add the diffrence to count        
        old_dial = new_dial 
print(counter)