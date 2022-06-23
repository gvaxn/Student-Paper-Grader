def main():
    infile = open("studentAnswers (1).py")
    answer = infile.readline().strip()

    # Create empty list to append items into later in your while loop

    keyList = []
    keyList = CreateStringList(keyList,"key (1).py", 'X')

    # set count varibles to 0 

    countAll = 0
    sumAll = 0
    highAvg = 0
    lowAvg = 100
    
    while answer != 'END':

        tCount = 0
        fCount = 0
    
        answerList = []
        correctList = []
        wrongList = []

        for i in range(0, len(answer), 1):
            answerList.append(answer[i])
            
    # Creates 2 new list and appends the correct answers

        for i in range(0, len(keyList), 1):
            if keyList[i] == answerList[i]:
                correctList.append(i + 1)

    # Appends the incorrect answers to the incorrect list 
      
            else:
                wrongList.append(i + 1)
            
    # Keeps count of the number of T's or F's

        for i in range(0, len(answerList), 1):
            if answerList[i] == 'T':
                tCount += 1
            else:
                fCount += 1

        mostAnswered = t_or_f(tCount, fCount)

    # Computes the score the student made

        score = float((len(keyList) - len(wrongList)) * 10)

        grade1 = grade(score)

        if score > highAvg:
            highAvg = score

        if score < lowAvg:
            lowAvg = score

        
        print("***************************************")
        print("Student", countAll + 1, "Summary:")

        PrintAnswerHeader(keyList, answerList)

        print ("CORRECT answers: #", end=''), PrintListOnSingleLine(correctList)
        print()
        print("Number correct:", len(correctList))
        print()
        print ("WRONG answers: #", end=''), PrintListOnSingleLine(wrongList)
        print()
        print("Number wrong: ", len(wrongList))
        print()
        print("The student has", tCount, "True Answers")
        print("The student has", fCount, "False Answers")
        print("The student answered", mostAnswered, "the most often.")
        print()
        print("The student's average is", score, '%' )
        print("The letter grade is:", grade1)
        print()

        sumAll += score
        countAll += 1

        answer = infile.readline().strip()
 
    print("***************************************")
    print(format("Students:", '>12s'), format(countAll, '3d'))
    print(format("Class Avg:", '>12s'), format(float(sumAll/countAll), '7.2f'))
    print(format("Highest Avg:", '12s'), format(highAvg, '7.2f'))
    print(format("Lowest Avg:", '>12s'), format(lowAvg, '7.2f'))

# function to calculate if T or F was used more

def t_or_f(tCount, fCount):

    if tCount > fCount:
        mostAnswered = 'T'
    else:
        mostAnswered = 'F'
    return mostAnswered

# function that returns the students letter grade

def grade(score):

    if score >= 90.0:
        grade = 'A'
    elif score >= 80.0:
        grade = 'B'
    elif score >= 70.0:
        grade = 'C'
    elif score >= 60.0:
        grade = 'D'
    else:
        grade = 'F'
    return grade

# function that pretty prints the header chart

def PrintAnswerHeader(keyList, answerList):
    # This function prints to the screen the answer key solutions
    # and the student's answers
    # Inputs:  a list containing the answer key
    #          a list of the student's answers
    # Return:  no value is returned

    # print problem numbers
    print ()
    print ("          ", end = '')
    for i in range (len(keyList)):
        print (i+1, end = '  ')


    #print ("\n----------------------------------------")
    # print the dashed line of varying length, dependent on number
    # of problems to display
    print()
    print ("----------", end="")
    for i in range (len(keyList)):
        print ("---", end="")
    print ()


    # print key answers    
    print ("Key    ", end = '   ')
    for i in range (len(keyList)):
        print (keyList[i], end = '  ')
        

    # print student answers
    print ()
    print ("Student", end = '   ')
    for i in range(len(answerList)):
        print (answerList[i], end = '  ')
    print ()
    print ()

def CreateStringList(theList, filename, sentinelValue):

    infile = open(filename, 'r')

    data = infile.readline().strip()

    while data != sentinelValue:

        theList.append(data)
        data = infile.readline().strip()

    infile.close()

    return theList

def PrintListOnSingleLine(theList):

    print (end = '   ')
    for i in range (len(theList)):
        print (theList[i], end = '  ')
    

main()