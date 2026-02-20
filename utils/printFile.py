def printFile(path):
    with open(path, 'r') as file:
        for line in file:
            print(line)
