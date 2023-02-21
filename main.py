import blessed
import os
import time
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

def makeFrame(level):
    frame = ""
    rows = len(level)
    cols = len(level[1])
    #word = term.brown4('SYSTEM OFFLINE') + term.green('SYSTEM online')
    for i in range(0,rows):
        line = level[i]
        for j in range(0,cols):
            if line[j] in ("-","|"):
                frame += term.brown4(line[j])
            else:
                frame += term.green(line[j])
        frame += "\n"
    print(frame)


#Main program
level = loadLevel()
makeFrame(level)
