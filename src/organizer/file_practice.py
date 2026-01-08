def writeToFile(text, fileName):
    """
    Writes a list of strings to a file

    Parameters:
        text (list): list of strings
    
    Returns:
        None
    """
    count = 0
    with open(fileName, "a") as file:
        file.write("\n")
        for line in text:
            if count<len(text)-1:
                file.write(line+"\n")
            else:
                file.write(line)
            count+=1


def readAndPrintFile(fileName):
    """
    Reads file and prints each line

    Parameters:
        fileName (str): name of file
    Retrns:
        None
    """
    try:
        with open(fileName, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print('File not found:', fileName)


def countLinesInFile(fileName):
    """
    Counts how many lines are in the file

    Parameters:
        fileName (str): name of file to open
    Returns:
        count (int): count of lines in the file
    """
    count = 0
    try:
        with open(fileName, "r") as file:
            for lines in file:
                count += 1    
        return count

    except FileNotFoundError:
        print('File not found:', fileName)
        return 0
    #could also use: return sum(1 for _ in file)


#readAndPrintFile("C:/Users/Samara/Documents/GitHub/testText.txt")
#countLinesInFile("C:/Users/Samara/Documents/GitHub/testText.txt")

#lines = ['a','b','c']
#writeToFile(lines, "C:/Users/Samara/Documents/GitHub/testText.txt")
