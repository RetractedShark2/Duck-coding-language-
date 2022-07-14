import sys

command = []
varlist = []
cmdCount = 0

for i in range(32):
    varlist.append(0)

#file input
cdname = input("Filename: ")

#commmand decoding
file = open(cdname, "r+")
Lines = file.readlines()

for i in range(len(Lines)):
    command.append(Lines[i].count("duck"))

file.close()

#program list
while command[cmdCount] != 8 or command[cmdCount] > 9:

    if command[int(cmdCount)] == 1:
        cmdCount += 1

        #beginning of print
        duck0 = ""
        duckinascii = 0
        duck1 = ""
        duck1a = 0

        if (command[cmdCount]) > 0:

            while command[int(cmdCount)] != 0:

                duckinascii = command[cmdCount] 
                duck1 = chr(duckinascii)
                duck0 = duck0 + duck1

                cmdCount += 1
            
            print(duck0)
        
        elif (command[cmdCount]) < 1:
            cmdCount += 1

            duck1a = int(command[cmdCount])

            print(varlist[duck1a])

            cmdCount += 1

        cmdCount += 1
    
    elif command[int(cmdCount)] == 2:
        cmdCount += 1
        duck2a = 0
        duck2b = 0
        duck2c = 0
        duck2deez = 0

        #beginning of addition
        duck2a = command[cmdCount]
        cmdCount += 1
        duck2b = command[cmdCount]

        duck2c = duck2a + duck2b
        cmdCount += 1

        duck2deez = int(command[cmdCount])

        varlist.insert(duck2deez, duck2c)

        cmdCount += 2

    elif command[int(cmdCount)] == 3:
        cmdCount += 1
        duck3a = 0
        duck3b = 0
        duck3c = 0
        duck3deez = 0

        #beginning of subtraction
        duck3a = command[cmdCount]
        cmdCount += 1
        duck3b = command[cmdCount]

        duck3c = duck3a - duck3b
        cmdCount += 1

        duck3deez = int(command[cmdCount])

        varlist.insert(duck3deez, duck3c)

        cmdCount += 2
    
    elif command[int(cmdCount)] == 4:
        cmdCount += 1
        duck4a = 0
        duck4b = 0
        duck4c = 0
        duck4deez = 0

        #beginning of subtraction
        duck4a = command[cmdCount]
        cmdCount += 1
        duck4b = command[cmdCount]

        duck4c = duck4a * duck4b
        cmdCount += 1

        duck4deez = int(command[cmdCount])

        varlist.insert(duck4deez, duck4c)

        cmdCount += 2

    elif command[int(cmdCount)] == 5:
        cmdCount += 1
        duck5a = 0
        duck5A = 0
        duck5B = 0
        duck5C = 0

        #begin hell (load var + usr input)
        if command[int(cmdCount)] == 0:
            cmdCount += 1

            #Usr input

            if command[int(cmdCount)] == 1:
                duck5ans = input("> ")
            elif command[int(cmdCount)] == 0:
                duck5ans = input()

            cmdCount += 1

            duck5a = int(command[cmdCount])

            varlist.insert(duck5a, duck5ans)

        elif command[int(cmdCount)] == 1:
            cmdCount += 1

            #Var loader

            duck5A = command[int(cmdCount)] 

            duck5B = varlist[int(duck5A)]

            cmdCount += 1

            duck5C = int(command[cmdCount])

            varlist.insert(duck5C, duck5B)
            

        cmdCount += 2
    
    elif command[int(cmdCount)] == 6:
        cmdCount += 1

        #jump to places i guess

        duck6 = command[cmdCount]

        if duck6 >= 0:
            cmdCount = duck6
        else:
            sys.exit("INVALID NUMBER")

    elif command[int(cmdCount)] == 7:
        cmdCount += 1

        #Store variables!
        duck7 = int(command[cmdCount])

        cmdCount += 1

        duck7a = int(command[cmdCount])

        varlist.insert(duck7a, duck7)

        cmdCount += 1

    elif command[int(cmdCount)] == 9:
        cmdCount += 1

        duck9a = int(command[cmdCount])

        cmdCount += 1

        duck9op = int(command[cmdCount])
        
        cmdCount += 1

        duck9b = int(command[cmdCount])

        duck9jump = 0

        if duck9op == 0:
            if duck9a == duck9b:
                duck9jump = 1
            else:
                duck9jump = 0
        elif duck9op == 1:
            if duck9a > duck9b:
                duck9jump = 1
            else:
                duck9jump = 0
        elif duck9op == 2:
            if duck9a < duck9b:
                duck9jump = 1
            else:
                duck9jump = 0
        elif duck9op == 3:
            if duck9a != duck9b:
                duck9jump = 1
            else:
                duck9jump = 0
        else:
            sys.exit("Bro u had one job")
    
    elif command[int(cmdCount)] == 10:
        sys.remove(cdname)

