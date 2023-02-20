import blessed
term = blessed.Terminal()

def loadLevel(): #reads from a template level and places it into a 2D array
    level = []

    f = open("template.txt","r")
    template = f.readlines()
    f.close()

    cols = len(template[0].strip())
    rows = len(template)
    
    for i in range(0,rows):
        line = template[i]
        tempRow = []
        for j in range(0,cols):
            tempRow.append(line[j])
        level.append(tempRow)
    return level

def displayLevel():
    print("Nothing")


level = loadLevel()
print(level)