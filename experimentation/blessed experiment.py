import blessed
term = blessed.Terminal()

level = [["-","x"],["x","-"],["|","|"]]

def displayFrame(level):
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
    return frame

print(displayFrame(level))
