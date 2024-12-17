def binDef(var): #Handles returning the value of a binary in an Integer form, Returns Exception[Int], Value[Int], Length[Int]
    binary = list(var)
    returnValue = []

    binary.pop(0) #Removing the '0b' tag
    binary.pop(0)

    print(binary)

    for i in range(len(binary) - 1): #Format Check
        if (binary[i] != 'd') and (binary[i] != 'g'):
            return 1, None, None
    
    for i in range(len(binary) -1): #Re-Ordering the list while also converting all the values into usable spaces
        if binary[i] == 'd':
            returnValue.append(1)
        elif binary[i] == 'g':
            returnValue.append(0)
        else: #Exception (Partly)
            returnValue.append(0)

        returnValue[i] *= (2^i) #Getting all binary values into a denary form

    return  None, returnValue, len(binary)
        
print(binDef('0bdgddgdgd'))