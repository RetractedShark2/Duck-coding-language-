import os
def functionDeclare(file):
    file.index

def main(fileLocation):
    if os.path.isfile(fileLocation) == False:
        return 2, None

    file = open(fileLocation)
    content = file.readlines()
    file.close()

    functionDeclare(file)

