
def getinput():
    choice1=True
    choice2=True
    "function for get user input,validate and check"
    global selection1,selection2,hold1,hold2,inp1,inp2
    global turncount1, turncount2, turncount3, turncount4, turncount5, turncount6, turncount7, turncount8, turncount9, turncount10, turncount11, turncount12

    #input01 and checking
    choice1 = True
    while choice1:
        print()#print some space
        print("\n".join("\t".join("{:1}".format(item) for item in row) for row in display))#print the list as a grid
        
        userinput1 = input("Select a card: ")
        inp1 = userinput1.upper()#input01
        print()#print some space

        if inp1 not in length_check:#input checking
            print("You cant select previous card")
            continue
            choice1=True

        if inp1 == "1":
            selection1 = cards[0]
            hold1 = "1"
            turncount1 += 1
            choice1 = False

        elif inp1 == "2":
            selection1 = cards[1]
            hold1 = "2"
            turncount2 += 1
            choice1 = False

        elif inp1 == "3":
            selection1 = cards[2]
            hold1 = "3"
            turncount3 += 1
            choice1 = False

        elif inp1 == "4":
            selection1 = cards[3]
            hold1 = "4"
            turncount4 += 1
            choice1 = False

        elif inp1 == "5":
            selection1 = cards[4]
            hold1 = "5"
            turncount5 += 1
            choice1 = False

        elif inp1 == "6":
            selection1 = cards[5]
            hold1 = "6"
            turncount6 += 1
            choice1 = False

        elif inp1 == "7":
            selection1 = cards[6]
            hold1 = "7"
            turncount7 += 1
            choice1 = False

        elif inp1 == "8":
            selection1 = cards[7]
            hold1 = "8"
            turncount8 += 1
            choice1 = False

        elif inp1 == "9":
            selection1 = cards[8]
            hold1 = "9"
            turncount9 += 1
            choice1 = False

        elif inp1 == "10":
            selection1 = cards[9]
            hold1 = "10"
            turncount10 += 1
            choice1 = False

        elif inp1 == "11":
            selection1 = cards[10]
            hold1 = "11"
            turncount11 += 1
            choice1 = False

        elif inp1 == "12":
            selection1 = cards[11]
            hold1 = "12"
            turncount12 += 1
            choice1 = False

        else:
            selection1 = "INVALID_1"
            print("Please enter a valid card")
            choice1 = True

        print("Your selection is ", selection1)#prints the value of selection
        print()  # print some space

    #input02 and checking
    choice2 = True
    while choice2:
        userinput2 = input("Select a card: ")
        inp2 = userinput2.upper()
        print()#print some space

        if inp2 not in length_check:#inputchecking
            print("You cant select previous card")
            continue
            choice2=True

        if inp1 == inp2:
            print("You cant select the same card")
            choice2 = True

        elif inp2 == "1":
            selection2 = cards[0]
            hold2 = "1"
            turncount1 += 1
            choice2 = False

        elif inp2 == "2":
            selection2 = cards[1]
            hold2 = "2"
            turncount2 += 1
            choice2 = False

        elif inp2 == "3":
            selection2 = cards[2]
            hold2 = "3"
            turncount3 += 1
            choice2 = False

        elif inp2 == "4":
            selection2 = cards[3]
            hold2 = "4"
            turncount4 += 1
            choice2 = False

        elif inp2 == "5":
            selection2 = cards[4]
            
            hold2 = "5"
            turncount5 += 1
            choice2 = False

        elif inp2 == "6":
            selection2 = cards[5]
            
            hold2 = "6"
            turncount6 += 1
            choice2 = False

        elif inp2 == "7":
            selection2 = cards[6]
            hold2 = "7"
            turncount7 += 1
            choice2 = False

        elif inp2 == "8":
            selection2 = cards[7]
            hold2 = "8"
            turncount8 += 1
            choice2 = False

        elif inp2 == "9":
            selection2 = cards[8]
            hold2 = "9"
            turncount9 += 1
            choice2 = False

        elif inp2 == "10":
            selection2 = cards[9]
            hold2 = "10"
            turncount10 += 1
            choice2 = False

        elif inp2 == "11":
            selection2 = cards[10]
            hold2 = "11"
            turncount11 += 1
            choice2 = False

        elif inp2 == "12":
            selection2 = cards[11]
            hold2 = "12"
            turncount12 += 1
            choice2 = False

        else:
            selection2 = "INVALID_2"
            print("Please enter a valid cards")
            choice2 = True

        print("Your selection is", selection2)
        print()
    return ()
# ..........................................................................

def inputcheking():
    "This function for check the inputs matching or not.calculating the turn tiles count and marks"
    global current_time,end_time,cards,cards_copy,length_check,selection1, selection2,hold1, hold2, inp1,remaintime
    global turncount1, turncount2, turncount3, turncount4, turncount5, turncount6, turncount7, turncount8, turncount9, turncount10, turncount11, turncount12, marks

    if selection1 == selection2:#matching
        print("Its Matched")
        marks += 20
        print("Your Marks: ", marks)
        print(hold1)
        print(hold2)
        print(length_check)
        length_check.remove(hold1)
        length_check.remove(hold2)
        print(length_check)                         
        grid()
        current_time=int(time.time())
        remaintime = (end_time-current_time)
        print("time remains: ", remaintime, "seconds")

    else:
        print("Its not Matched")
       
        if inp1 == "1":#calculating the count of the turns in tiles
            marks = marks - (turncount1 * 5)
            
        elif inp1 == "2":
            marks = marks - (turncount2 * 5)

        elif inp1 == "3":
            marks = marks - (turncount3 * 5)

        elif inp1 == "4":
            marks = marks - (turncount4 * 5)

        elif inp1 == "5":
            marks = marks - (turncount5 * 5)

        elif inp1 == "6":
            marks = marks - (turncount6 * 5)

        elif inp1 == "7":
            marks = marks - (turncount7 * 5)

        elif inp1 == "8":
            marks = marks - (turncount8 * 5)

        elif inp1 == "9":
            marks = marks - (turncount9 * 5)

        elif inp1 == "10":
            marks = marks - (turncount10 * 5)

        elif inp1 == "11":
            marks = marks - (turncount11 * 5)

        elif inp1 == "12":
            marks = marks - (turncount12 * 5)

        if inp2 == "1":
            marks = marks - (turncount1 * 5)

        elif inp2 == "2":
            marks = marks - (turncount2 * 5)

        elif inp2 == "3":
            marks = marks - (turncount3 * 5)

        elif inp2 == "4":
            marks = marks - (turncount4 * 5)

        elif inp2 == "5":
            marks = marks - (turncount5 * 5)

        elif inp2 == "6":
            marks = marks - (turncount6 * 5)

        elif inp2 == "7":
            marks = marks - (turncount7 * 5)

        elif inp2 == "8":
            marks = marks - (turncount8 * 5)

        elif inp2 == "9":
            marks = marks - (turncount9 * 5)

        elif inp2 == "10":
            marks = marks - (turncount10 * 5)

        elif inp2 == "11":
            marks = marks - (turncount11 * 5)

        elif inp2 == "12":
            marks = marks - (turncount12 * 5)

        print("Your Marks: ", marks)#marks and time
        current_time=int(time.time())
        remaintime = (end_time-current_time)
        print("time remains: ", remaintime, "seconds")
    return ()
# ....................................................................................................

def grid():
    'This function for update the grid after input matches'
    global selection1, selection2,hold1,hold2

    for x in display:
            if hold1 in x:
                if hold1 == "1":
                    x[0] = selection1

                if hold1 == "2":
                    x[1] = selection1

                if hold1 == "3":
                    x[2] = selection1

                if hold1 == "4":
                    x[3] = selection1

                if hold1 == "5":
                    x[0] = selection1

                if hold1 == "6":
                    x[1] = selection1

                if hold1 == "7":
                    x[2] = selection1

                if hold1 == "8":
                    x[3] = selection1

                if hold1 == "9":
                    x[0] = selection1

                if hold1 == "10":
                    x[1] = selection1

                if hold1 == "11":
                    x[2] = selection1

                if hold1 == "12":
                    x[3] = selection1

            if hold2 in x:
                if hold2 == "1":
                    x[0] = selection2

                if hold2 == "2":
                    x[1] = selection2

                if hold2 == "3":
                    x[2] = selection2

                if hold2 == "4":
                    x[3] = selection2

                if hold2 == "5":
                    x[0] = selection2

                if hold2 == "6":
                    x[1] = selection2

                if hold2 == "7":
                    x[2] = selection2

                if hold2 == "8":
                    x[3] = selection2

                if hold2 == "9":
                    x[0] = selection2

                if hold2 == "10":
                    x[1] = selection2

                if hold2 == "11":
                    x[2] = selection2

                if hold2 == "12":
                    x[3] = selection2
    return ()
# .....................................................................................

def continuecheck():
    choice3=True
    choice4=True
    "This function for check the state of play again,exit and level02"
    global length_check,remaintime,marks

    if (remaintime <= 0):#if time over
        print("Time Over")
        print("If want to play again press P")
        print("If want to exit press E")

        while (choice3):
            inp3 = str(input(":"))
            inp3=inp3.upper()

            if (inp3 == "P"):
                main()
                choice3=False

            elif (inp3 == "E"):
                print("You select EXIT")
                sys.exit()
                choice3=False

            else:
                print("Enter a valid command")
                choice3 = True

    if (len(length_check) == 0):#if all selects by the user
        print("Your Marks",marks)
        print("Time Bonus",remaintime)
        print("Total Marks",(marks+remaintime))
        print("Level 02 Succesfully Completed")
        print("To exit press E")

        while (choice4):
            inp4 = str(input(":"))
            inp4=inp4.upper()
                
            if (inp4 == "E"):
                print("You selected EXIT")
                sys.exit()
                choice4=False

            else:
                print("enter a valid command")
                choice4 = True

    return ()
# .......................................................................................................................

def main():
    import random, time, sys
    "This functions for asign the variables,check user choice and start the game"
    global current_time,end_time,maindisplay,cards,cards_copy, selection1, selection2,mainlist,mainlength_check,length_check, display, totaltime,remaintime,marks
    global turncount1, turncount2, turncount3, turncount4, turncount5, turncount6, turncount7, turncount8, turncount9, turncount10, turncount11, turncount12

    marks = 0
 
    turncount1 = 0
    turncount2 = 0
    turncount3 = 0
    turncount4 = 0
    turncount5 = 0
    turncount6 = 0
    turncount7 = 0
    turncount8 = 0
    turncount9 = 0
    turncount10 = 0
    turncount11 = 0
    turncount12 = 0

    choice0 = True

    mainlist = ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"]
    maindisplay = [["1", "2", "3", "4"],["5", "6", "7", "8"],["9", "10", "11", "12"]]
    mainlength_check=["1","2","3","4","5","6","7","8","9","10","11","12"]

    print()
    print(' Welcome to the level 02 in Memory Game.')
    print()
    print(" To start the game enter Y or to exit enter E")
    while(choice0):
        startvalue = str(input("Your choice:"))
        start = startvalue.upper()#
        while (start != "E"): #to exit the game 
            choice0=False
            if (start == "Y" or start == "P"):  # checking the game status
                choice0=False
                current_time=int(time.time())
                end_time=(current_time+50)
                cards = mainlist.copy()
                display = maindisplay.copy()
                length_check = mainlength_check.copy()
                cards = random.sample(cards, len(cards))
                print(cards)#remove
                remaintime = (end_time-current_time)

            else:
                print("Please enter a valid choice")
                choice0=True

            while (len(length_check) != 0) and (remaintime > 0):
                getinput()
                inputcheking()
                continuecheck()
        print("You select EXIT")
        sys.exit()
        return()
