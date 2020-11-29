def countLettersFromFile():
    fileName = input("Enter ur repository name:-")
    
    numberOfWords = 0
    
    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words:")
    print(numberOfWords)
    
countLettersFromFile()        