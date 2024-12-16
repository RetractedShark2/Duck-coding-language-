def binDef(var): #Handles returning the value of a binary in an Integer form, Returns Value[Int], Length[Int], Exception[Int]
    binary = list(var)
    returnValue = []

    binary.pop(0) #Removing the '0b' tag
    binary.pop(0)

    for i in range(len(binary) - 1): #Format Check
        if (binary[i] != 'd') or (binary[i] != 'g'):
            return None, None, 1
    
    for i in range(len(binary) -1): #Re-Ordering the list while also converting all the values into usable spaces
        if binary[i] == 'd':
            returnValue.append(1)
        elif binary[i] == 'g':
            returnValue.append(0)
        else: #Exception (Partly)
            returnValue.append(0)

        returnValue[i] *= (2^i) #Getting all binary values into a denary form

    return returnValue, len(binary), None
        
print(binDef('0bddgdgg'))